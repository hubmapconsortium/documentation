#!/usr/bin/env python3
"""Clean generator for assay JSON files (renamed from generate_json_clean).

This file is the same generator but renamed to `generate_markdown_clean.py`.
It produces per-assay JSON files and accompanying markdown in the
configured output directories.
"""
import os
import re
import csv
import json
import glob
import yaml
import time
from pathlib import Path
import argparse
import shutil

# Config (paths from project)
RSOURCE_DIR = '/home/birdie/Documents/hubmap/documentation/scripts/newMeta2/source/reharmonize-legacy-metadata/metadata'
JSONLD_SOURCE = '/home/birdie/Documents/hubmap/documentation/scripts/newMeta2/source/dataset-metadata-spreadsheet'
IVT_SOURCE = os.path.join(os.path.dirname(__file__), 'source', 'IVT_table_meta')
OUTPUT_DIR = '/home/birdie/Documents/hubmap/documentation/scripts/newMeta2/JSON/'
MARKDOWN_DIR = '/home/birdie/Documents/hubmap/documentation/scripts/newMeta2/markdown'

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MARKDOWN_DIR, exist_ok=True)


def _normalize_attr_key(s):
	if not s:
		return ''
	return re.sub(r'\s+', ' ', str(s)).strip().lower()


def normalize_type(t):
	"""Normalize type strings into human-friendly canonical values."""
	if not t:
		return ''
	s = str(t).strip().lower()
	mapping = {
		'controlled-term-field': 'Allowable value',
		'radio-field': 'Radio',
		'numeric-field': 'Numeric',
		'text-field': 'Textfield',
		'link-field': 'Textfield'
	}
	if s in mapping:
		return mapping[s]
	# Treat 'assigned value' (and variants) as allowable values
	if s.replace('-', ' ') in ('assigned value', 'assignedvalue'):
		return 'Allowable value'
	if s.endswith('-field'):
		base = s[:-6]
		return base.capitalize()
	return str(t).capitalize()


def _determine_type(item):
	"""Decide the final `type` for an item.

	If allowable values are exclusively Yes/No (case-insensitive), prefer `Radio`.
	Otherwise normalize the existing type string.
	"""
	t = item.get('type') or ''
	allowable = item.get('allowable values') or []
	if isinstance(allowable, (list, tuple)) and allowable:
		low = set([str(x).strip().lower() for x in allowable if x is not None])
		if low and (low.issubset({'yes', 'no'}) or low.issubset({'true', 'false'})):
			return 'Radio'
	return normalize_type(t)


def _format_allowable_values(vals):
	"""Format allowable values for markdown output.

	Wrap each value in triple backticks and join with spaces (no commas).
	"""
	if not isinstance(vals, (list, tuple)):
		return ''
	wrapped = [f"```{v}```" for v in vals]
	return ' '.join(wrapped)


def generate_markdown_from_json(assay, section, out_dir=MARKDOWN_DIR):
	"""Generate a markdown file for an assay section containing `main` and `deprecated`.

	Produces `<out_dir>/<assay>.md`.
	"""
	# Use AssayName (from section) for filename and title when available
	assay_name = None
	if isinstance(section, dict):
		assay_name = section.get('AssayName')
	# Replace spaces with dashes for the filename (keep title unchanged)
	safe_name = re.sub(r"\s+", '-', (assay_name or assay))
	fname = f"{safe_name}.md"
	path = os.path.join(out_dir, fname)

	# Build table body strings for template replacement
	def esc(s):
		return str(s).replace('|', '\\|')

	def render_rows(rows, deprecated=False):
		out = []
		for it in rows:
			term = it.get('attribute') or ''
			try:
				if it.get('required'):
					color = '#00000061' if deprecated else 'red'
					term = f"{term} <span style=\"color:{color}\" title=\"Required\" aria-label=\"Required\">*</span>"
			except Exception:
				pass
			typ = it.get('type') or ''
			if typ is None or (isinstance(typ, str) and typ.strip() == ''):
				typ = _determine_type(it)
			desc = it.get('description') or ''
			av = it.get('allowable values') or []
			avs = _format_allowable_values(av) if av else ''
			out.append(f"| {esc(term)} | {esc(typ)} | {esc(desc)} | {avs} |\n")
		return ''.join(out)

	main_rows = render_rows(section.get('main', []) if isinstance(section, dict) else [])
	classic_rows = render_rows(section.get('deprecated', []) if isinstance(section, dict) else [], deprecated=True)

	# Load template and substitute
	tpl_path = os.path.join(os.path.dirname(__file__), 'Template.md')
	if os.path.exists(tpl_path):
		try:
			tpl = open(tpl_path, 'r', encoding='utf-8').read()
			title = assay_name or assay
			content = tpl.replace('{AssayNameHere}', title).replace('{Main Table}', main_rows).replace('{Classic Table}', classic_rows)
			with open(path, 'w', encoding='utf-8') as mf:
				mf.write(content)
			return path
		except Exception:
			pass

	# Fallback to previous simple writer if template missing
	lines = []
	lines.append(f"# {assay_name or assay}\n\n")
	lines.append("| Attribute | Type | Description | Allowable Values |\n")
	lines.append("|---|---|---|---|\n")
	lines.append(main_rows)
	if classic_rows:
		lines.append('\n')
		lines.append('## Deprecated / Classic Attributes\n\n')
		lines.append("| Attribute | Type | Description | Allowable Values |\n")
		lines.append("|---|---|---|---|\n")
		lines.append(classic_rows)
	with open(path, 'w', encoding='utf-8') as mf:
		mf.writelines(lines)
	return path


def get_version_folders(assay_path):
	if not os.path.isdir(assay_path):
		return []
	folders = [f for f in os.listdir(assay_path) if os.path.isdir(os.path.join(assay_path, f))]
	latest = [f for f in folders if f == 'latest']
	versions = [f for f in folders if re.match(r'^v?\d+(?:\.\d+)*$', f)]
	versions_sorted = sorted(versions, key=lambda v: list(map(int, re.findall(r'\d+', v))), reverse=True)
	return latest + versions_sorted


def process_fmdata(csv_path):
	"""Return (main_list, deprecated_list) with canonical fields populated.
	Leftmost column -> main; if leftmost empty use rightmost non-empty -> deprecated.
	"""
	main = []
	deprecated = []
	with open(csv_path, newline='', encoding='utf-8') as cf:
		reader = csv.DictReader(cf)
		cols = reader.fieldnames
		if not cols:
			return main, deprecated
		left_col = cols[0]
		for row in reader:
			left_val = (row.get(left_col) or '').strip()
			if left_val:
				obj = {
					'attribute': left_val,
					'type': '',
					'description': '',
					'allowable values': [],
					'required': False,
				}
				main.append(obj)
				continue
			# rightmost non-empty
			found = None
			for c in reversed(cols):
				if c == left_col:
					continue
				v = (row.get(c) or '').strip()
				if v:
					found = v
					break
			if found:
				obj = {
					'attribute': found,
					'type': '',
					'description': '',
					'allowable values': [],
					'required': False,
				}
				deprecated.append(obj)
	return main, deprecated


def load_glossary_for_assay(assay):
	mapping = {}
	gdir = os.path.join(RSOURCE_DIR, assay, 'glossary')
	if not os.path.isdir(gdir):
		return mapping
	for fn in os.listdir(gdir):
		if not fn.lower().endswith('.csv'):
			continue
		path = os.path.join(gdir, fn)
		try:
			with open(path, newline='', encoding='utf-8') as cf:
				r = csv.reader(cf)
				rows = list(r)
				if not rows:
					continue
				header = rows[0]
				if len(header) > 1 and any(h.strip() for h in header):
					cf.seek(0)
					for d in csv.DictReader(open(path, newline='', encoding='utf-8')):
						keys = list(d.keys())
						if not keys:
							continue
						name_key = None
						for candidate in ('attribute', 'term', 'name', 'label'):
							for k in keys:
								if k.lower() == candidate:
									name_key = k
									break
							if name_key:
								break
						if not name_key:
							name_key = keys[0]
						desc_key = None
						for candidate in ('description', 'def', 'definition', 'term_definition'):
							for k in keys:
								if k.lower() == candidate:
									desc_key = k
									break
							if desc_key:
								break
						term = (d.get(name_key) or '').strip()
						desc = (d.get(desc_key) or '').strip() if desc_key else ''
						if term and desc:
							mapping[_normalize_attr_key(term)] = desc
				else:
					for row in rows:
						if not row:
							continue
						term = row[0].strip() if len(row) > 0 else ''
						desc = row[1].strip() if len(row) > 1 else ''
						if term and desc:
							mapping[_normalize_attr_key(term)] = desc
		except Exception:
			continue
	return mapping


def process_assay_yaml(yaml_path):
	try:
		with open(yaml_path, 'r', encoding='utf-8') as yf:
			data = yaml.safe_load(yf) or {}
	except Exception:
		return {}
	res = {}
	children = data.get('children', []) if isinstance(data, dict) else []
	def _value_label(v):
		if not isinstance(v, dict):
			return None
		return v.get('termLabel') or v.get('label') or v.get('prefLabel') or v.get('name')
	for child in children:
		if not isinstance(child, dict):
			continue
		attr = child.get('key')
		if not attr:
			continue
		typ = child.get('type') or ''
		desc = child.get('description') or ''
		config = child.get('configuration') or {}
		required = bool(config.get('required', False))
		allowable = []
		if typ == 'controlled-term-field':
			vals = child.get('values') or []
			labels = set()
			for v in vals:
				lbl = _value_label(v)
				if lbl:
					labels.add(lbl)
			allowable = sorted(labels)
		res[_normalize_attr_key(attr)] = {
			'attribute': attr,
			'type': typ,
			'description': desc,
			'allowable values': allowable,
			'required': required,
		}
	return res


def load_yaml_map_for_assay(assay):
	assay_path = os.path.join(JSONLD_SOURCE, assay)
	if not os.path.isdir(assay_path):
		return {}
	folders = get_version_folders(assay_path)
	merged = {}
	for v in reversed(folders):
		vp = os.path.join(assay_path, v)
		if not os.path.isdir(vp):
			continue
		for f in os.listdir(vp):
			if f.endswith('.yml') or f.endswith('.yaml'):
				path = os.path.join(vp, f)
				m = process_assay_yaml(path)
				for k, v in m.items():
					existing = merged.get(k, {})
					merged[k] = {**existing, **{kk: vv for kk, vv in v.items() if vv not in (None, '', [], {})}}
	return merged


def load_jsonld_map_for_assay(assay):
	assay_path = os.path.join(JSONLD_SOURCE, assay)
	if not os.path.isdir(assay_path):
		return {}
	folders = get_version_folders(assay_path)
	merged = {}
	for v in reversed(folders):
		vp = os.path.join(assay_path, v)
		if not os.path.isdir(vp):
			continue
		for f in os.listdir(vp):
			if not f.endswith('.jsonld'):
				continue
			path = os.path.join(vp, f)
			try:
				with open(path, 'r', encoding='utf-8') as jf:
					jd = json.load(jf)
			except Exception:
				continue
			ui_pd = jd.get('_ui', {}).get('propertyDescriptions', {}) if isinstance(jd.get('_ui', {}), dict) else {}
			props = jd.get('properties', {}) if isinstance(jd.get('properties', {}), dict) else {}
			for pname, pval in props.items():
				if not pname:
					continue
				key = _normalize_attr_key(pname)
				entry = merged.get(key, {})
				desc = ui_pd.get(pname)
				if desc and not entry.get('description'):
					entry['description'] = desc
				t = None
				if isinstance(pval.get('_ui', {}), dict):
					t = pval.get('_ui', {}).get('inputType')
				if t and not entry.get('type'):
					entry['type'] = t
				vc = pval.get('_valueConstraints', {}) or {}
				branches = vc.get('branches') or []
				vals = []
				for b in branches:
					if isinstance(b, dict) and 'label' in b:
						vals.append(b.get('label'))
				if vals and not entry.get('allowable values'):
					entry['allowable values'] = vals
				if not entry.get('attribute'):
					entry['attribute'] = pname
				merged[key] = entry
	return merged


def build_ivt_maps():
	assay_map = {}
	includes_map = {}
	if not os.path.isdir(IVT_SOURCE):
		return assay_map, includes_map
	for root, dirs, files in os.walk(IVT_SOURCE):
		for fn in files:
			if not fn.endswith('.yaml') and not fn.endswith('.yml'):
				continue
			path = os.path.join(root, fn)
			if 'includes' in Path(path).parts:
				try:
					with open(path, 'r', encoding='utf-8') as yf:
						docs = list(yaml.safe_load_all(yf))
				except Exception:
					continue
				for doc in docs:
					if isinstance(doc, dict):
						name = doc.get('name') or doc.get('attribute') or doc.get('key')
						desc = doc.get('description') or doc.get('def') or ''
						typ = doc.get('type') or ''
						if name:
							includes_map[_normalize_attr_key(name)] = {'description': desc, 'type': typ}
				continue
			m = re.match(r'^([a-zA-Z0-9_\-]+)-', fn)
			if not m:
				continue
			assay_name = m.group(1)
			try:
				with open(path, 'r', encoding='utf-8') as yf:
					docs = list(yaml.safe_load_all(yf))
			except Exception:
				continue
			merged = assay_map.setdefault(assay_name, {})
			for doc in docs:
				if isinstance(doc, list):
					for d in doc:
						if isinstance(d, dict):
							n = d.get('name') or d.get('attribute') or d.get('key')
							if not n:
								continue
							k = _normalize_attr_key(n)
							merged.setdefault(k, {})
							if d.get('description') and not merged[k].get('description'):
								merged[k]['description'] = d.get('description')
							if d.get('type') and not merged[k].get('type'):
								merged[k]['type'] = d.get('type')
				elif isinstance(doc, dict):
					n = doc.get('name') or doc.get('attribute') or doc.get('key')
					if not n:
						continue
					k = _normalize_attr_key(n)
					merged.setdefault(k, {})
					if doc.get('description') and not merged[k].get('description'):
						merged[k]['description'] = doc.get('description')
					if doc.get('type') and not merged[k].get('type'):
						merged[k]['type'] = doc.get('type')
			assay_map[assay_name] = merged
	return assay_map, includes_map


def load_docs_index(docs_base):
	"""Build a lightweight docs index mapping normalized attribute -> (type, description).
	Scans markdown and HTML files under `docs_base` for table rows containing attribute names.
	"""
	mapping = {}
	if not os.path.isdir(docs_base):
		return mapping
	for root, dirs, files in os.walk(docs_base):
		for fn in files:
			if not (fn.endswith('.md') or fn.endswith('.markdown') or fn.endswith('.html')):
				continue
			path = os.path.join(root, fn)
			try:
				text = open(path, 'r', encoding='utf-8').read()
			except Exception:
				continue
			# Simple markdown table rows: | attr | Type | Description | Allowable Values | Required |
			for line in text.splitlines():
				if not line.strip().startswith('|'):
					continue
				parts = [p.strip() for p in line.split('|')[1:-1]]
				if len(parts) < 2:
					continue
				attr = parts[0]
				typ = parts[1]
				if not attr:
					continue
				key = _normalize_attr_key(attr)
				# only record non-blank types
				if typ and typ.lower() not in ('', '-', 'none'):
					mapping.setdefault(key, {})
					mapping[key].setdefault('type', typ)
					# description if available
					if len(parts) > 2 and parts[2].strip():
						mapping[key].setdefault('description', parts[2].strip())
					# attempt to parse allowable values presented like "[a, b, c]"
					# search both type, description and allowable-values column for bracketed lists
					candidate_text = ' '.join(p for p in (typ, parts[2] if len(parts) > 2 else '', parts[3] if len(parts) > 3 else '') if p)
					# 1) Python/list-like brackets: [a, b, c] or ['a','b']
					mvals = re.search(r"\[([^\]]+)\]", candidate_text)
					vals = []
					if mvals:
						raw = mvals.group(1)
						for v in raw.split(','):
							vv = v.strip().strip('\"\'')
							if vv:
								vals.append(vv)
					# 2) backticked tokens like ```nm``` or `nm`
					bt = re.findall(r"`{1,3}([^`]+)`{1,3}", candidate_text)
					for b in bt:
						bb = b.strip()
						if bb and bb not in vals:
							vals.append(bb)
					if vals:
						mapping[key].setdefault('allowable values', vals)
					# parse Required column if present (e.g. 'True', 'Yes') in column 5 (index 4)
						if len(parts) > 4 and parts[4].strip():
							raw_req = parts[4].strip().lower()
							if raw_req in ('true', 'yes', 'required', 'y'):
								mapping[key]['required'] = True
			# HTML tables: look for <td>attr</td> followed by <td>type</td>
			try:
				import re as _re
				for m in _re.finditer(r'<td[^>]*>([^<]+)</td>\s*<td[^>]*>([^<]+)</td>\s*(?:<td[^>]*>([^<]+)</td>)?\s*(?:<td[^>]*>([^<]+)</td>)?', text, _re.IGNORECASE):
					attr = m.group(1).strip()
					typ = m.group(2).strip()
					# optional third and fourth cells (description/allowable values and required)
					third = m.group(3).strip() if m.lastindex and m.lastindex >= 3 and m.group(3) else ''
					fourth = m.group(4).strip() if m.lastindex and m.lastindex >= 4 and m.group(4) else ''
					if not attr:
						continue
					key = _normalize_attr_key(attr)
					if typ and typ.lower() not in ('', '-', 'none'):
						mapping.setdefault(key, {})
						mapping[key].setdefault('type', typ)
						# try to parse allowable values from the type cell
						vals = []
						mvals = re.search(r"\[([^\]]+)\]", ' '.join((typ, third)))
						if mvals:
							raw = mvals.group(1)
							for v in raw.split(','):
								vv = v.strip().strip('"\'')
								if vv:
									vals.append(vv)
						# backticked tokens (search both type and third column)
						bt = re.findall(r"`{1,3}([^`]+)`{1,3}", ' '.join((typ, third)))
						for b in bt:
							bb = b.strip()
							if bb and bb not in vals:
								vals.append(bb)
						if vals:
							mapping[key].setdefault('allowable values', vals)
						# parse required from fourth column when present (only set True)
						if fourth:
							r = fourth.strip().lower()
							if r in ('true', 'yes', 'required', 'y'):
								mapping[key]['required'] = True
			except Exception:
				pass
	return mapping


def load_assay_display_name_from_docs(assay, docs_base):
	"""Find transformation-summary.html under docs_base for the assay and extract the prefix
	from the <title> tag up to ' - Metadata Transformation Summary'. Returns None if not found.
	"""
	if not os.path.isdir(docs_base):
		return None
	# Prefer file under docs_base/<assay>/transformation-summary.html
	candidate = os.path.join(docs_base, assay, 'transformation-summary.html')
	if os.path.exists(candidate):
		try:
			txt = open(candidate, 'r', encoding='utf-8').read()
			m = re.search(r'<title>\s*(.*?)\s*-\s*Metadata Transformation Summary\s*</title>', txt, re.IGNORECASE)
			if m:
				return m.group(1).strip()
		except Exception:
			pass
	# fallback: search any transformation-summary.html under docs_base
	for root, dirs, files in os.walk(docs_base):
		for fn in files:
			if fn != 'transformation-summary.html':
				continue
			path = os.path.join(root, fn)
			try:
				txt = open(path, 'r', encoding='utf-8').read()
			except Exception:
				continue
			m = re.search(r'<title>\s*(.*?)\s*-\s*Metadata Transformation Summary\s*</title>', txt, re.IGNORECASE)
			if m:
				# prefer files whose path contains assay name
				if assay in path:
					return m.group(1).strip()
				# otherwise first match
				return m.group(1).strip()

	# Additional fallback: look for markdown/html files with H1/title and try to match by filename or title
	for root, dirs, files in os.walk(docs_base):
		for fn in files:
			if not (fn.endswith('.md') or fn.endswith('.markdown') or fn.endswith('.html')):
				continue
			path = os.path.join(root, fn)
			try:
				text = open(path, 'r', encoding='utf-8').read()
			except Exception:
				continue
			# markdown H1
			m = re.search(r'^\s*#\s*(.+)$', text, re.MULTILINE)
			title = None
			if m:
				title = m.group(1).strip()
			else:
				m2 = re.search(r'<title>\s*(.*?)\s*</title>', text, re.IGNORECASE)
				if m2:
					title = m2.group(1).strip()
			if not title:
				continue
			bn = os.path.splitext(fn)[0].lower()
			# normalize strings for matching
			n_assay = str(assay).lower()
			n_title = title.lower()
			# match by filename containing assay or vice-versa, or title containing assay
			if n_assay in bn or bn in n_assay or n_assay in n_title or n_title in n_assay:
				return title

	return None


def generate_all(use_ivt=False, use_jsonld=False):
	start = time.time()
	assays = [d for d in os.listdir(RSOURCE_DIR) if os.path.isdir(os.path.join(RSOURCE_DIR, d))]
	if use_ivt:
		ivt_assay_map, ivt_includes_map = build_ivt_maps()
	else:
		ivt_assay_map, ivt_includes_map = {}, {}
	docs_base = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'docs', 'assays', 'metadata')
	docs_index = load_docs_index(docs_base)
	for assay in assays:
		fm_pattern = os.path.join(RSOURCE_DIR, assay, '*-field-mappings.csv')
		files = glob.glob(fm_pattern)
		if not files:
			continue
		main_all = []
		deprecated_all = []
		for f in files:
			m, d = process_fmdata(f)
			main_all.extend(m)
			deprecated_all.extend(d)

		glossary = load_glossary_for_assay(assay)
		yaml_map = load_yaml_map_for_assay(assay) if use_jsonld else {}
		jsonld_map = load_jsonld_map_for_assay(assay) if use_jsonld else {}
		ivt_assay_entries = ivt_assay_map.get(assay) or {}

		def fill_item(item):
			key = _normalize_attr_key(item.get('attribute'))
			if not item.get('description') and glossary.get(key):
				item['description'] = glossary.get(key)
			y = yaml_map.get(key) or {}
			if y:
				# Prefer filling values from YAML/JSON-LD (y contains processed YAML entries)
				if y.get('type'):
					item['type'] = item.get('type') or y.get('type')
				if y.get('description'):
					item['description'] = item.get('description') or y.get('description')
				if y.get('allowable values'):
					if not item.get('allowable values'):
						item['allowable values'] = y.get('allowable values')
				# If YAML explicitly provides a required flag, respect True only
				if y.get('required'):
					item['required'] = True
				return
			j = jsonld_map.get(key) or {}
			if j:
				if j.get('type'):
					item['type'] = item.get('type') or j.get('type')
				if j.get('description'):
					item['description'] = item.get('description') or j.get('description')
				if j.get('allowable values'):
					if not item.get('allowable values'):
						item['allowable values'] = j.get('allowable values')
				# Respect explicit required flag from JSON-LD when present (only set True)
				if j.get('required'):
					item['required'] = True
				return
			# Docs (added search path)
			d = docs_index.get(key) or {}
			if d:
				if d.get('type'):
					item['type'] = item.get('type') or d.get('type')
				# If docs provide allowable values (e.g. [a, b, c]) and item lacks them, use them
				if d.get('allowable values'):
					if not item.get('allowable values'):
						item['allowable values'] = d.get('allowable values')
				if d.get('description'):
					item['description'] = item.get('description') or d.get('description')
				# If docs explicitly indicate requiredness, respect True only
				if d.get('required'):
					item['required'] = True
				return
			ivt = ivt_assay_entries.get(key) or {}
			if ivt:
				if ivt.get('description'):
					item['description'] = item.get('description') or ivt.get('description')
				if ivt.get('type'):
					item['type'] = item.get('type') or ivt.get('type')
				if ivt.get('required'):
					item['required'] = True
				return
			inc = ivt_includes_map.get(key) or {}
			if inc:
				if inc.get('description'):
					item['description'] = item.get('description') or inc.get('description')
				if inc.get('type'):
					item['type'] = item.get('type') or inc.get('type')
				if inc.get('required'):
					item['required'] = True


		for itm in main_all + deprecated_all:
			fill_item(itm)

		# Normalize/finalize types for all items (detect radios from allowable values,
		# and canonicalize type strings).
		for itm in main_all + deprecated_all:
			try:
				itm['type'] = _determine_type(itm)
			except Exception:
				# fallback: preserve whatever was present
				itm['type'] = itm.get('type') or ''

		# Add AssayName from the transformation-summary.html <title> when available;
		# otherwise fall back to the assay folder name.
		section = {'main': main_all, 'deprecated': deprecated_all}
		assay_display = load_assay_display_name_from_docs(assay, docs_base)
		# If not found in the docs site path, also check the source transformation-summary
		if not assay_display:
			src_candidate = os.path.join(RSOURCE_DIR, assay, 'transformation-summary.html')
			if os.path.exists(src_candidate):
				try:
					txt = open(src_candidate, 'r', encoding='utf-8').read()
					m = re.search(r'<title>\s*(.*?)\s*-\s*Metadata Transformation Summary\s*</title>', txt, re.IGNORECASE)
					if m:
						assay_display = m.group(1).strip()
				except Exception:
					assay_display = None
		if assay_display:
			section['AssayName'] = assay_display
		else:
			section['AssayName'] = assay
		out = {assay: section}
		out_path = os.path.join(OUTPUT_DIR, f"{assay}.json")
		with open(out_path, 'w', encoding='utf-8') as outf:
			json.dump(out, outf, indent=2)
		print(f'Wrote {out_path}')
		# Also generate markdown for this assay
		try:
			md_path = generate_markdown_from_json(assay, section)
			print(f'Wrote {md_path}')
		except Exception:
			pass

	print(f'Done. Elapsed: {time.time() - start:.2f}s')


if __name__ == '__main__':
	p = argparse.ArgumentParser()
	p.add_argument('--sources', nargs='*', choices=['ivt', 'jsonld'], help='Enable optional sources. Example: --sources ivt jsonld')
	p.add_argument('--apply', action='store_true', help='If set, run markdown postprocessing and copy files to docs/assays/metadata/testing')
	args = p.parse_args()
	sources = args.sources or []
	use_ivt = 'ivt' in sources
	use_jsonld = 'jsonld' in sources
	print(f'Enabled sources: ivt={use_ivt}, jsonld={use_jsonld}')
	generate_all(use_ivt=use_ivt, use_jsonld=use_jsonld)

	def _map_type_to_icon(typ):
		if not typ:
			return ''
		s = str(typ).strip().lower()
		# normalize common synonyms
		if s in ('link', 'email'):
			s = 'textfield'
		if s.startswith('controlled') or 'allowable' in s:
			s = 'allowable value'
		icons = {
			'textfield': '<i class="icon-textfield" aria-hidden="true"></i> Textfield',
			'text': '<i class="icon-textfield" aria-hidden="true"></i> Textfield',
			'allowable value': '<i class="icon-allowable" aria-hidden="true"></i> Allowable Value',
			'radio': '<i class="icon-radio" aria-hidden="true"></i> Radio',
			'numeric': '<i class="icon-numeric" aria-hidden="true"></i> Numeric',
			'checkbox': '<i class="icon-checkbox" aria-hidden="true"></i> Checkbox',
			'date': '<i class="icon-date" aria-hidden="true"></i> Date',
		}
		return icons.get(s, typ)

	def _postprocess_markdown(md_dir, deploy_target):
		# Process markdown files in-place then optionally copy to deploy_target
		if not os.path.isdir(md_dir):
			print(f'Markdown dir not found: {md_dir}')
			return
		files = [f for f in os.listdir(md_dir) if f.endswith('.md')]
		for fn in files:
			path = os.path.join(md_dir, fn)
			try:
				text = open(path, 'r', encoding='utf-8').read()
			except Exception:
				print(f'Could not read {path}')
				continue
			lines = []
			for line in text.splitlines():
				if not line.strip().startswith('|'):
					lines.append(line)
					continue
				parts = line.split('|')
				# parts: ['', ' Attribute ', ' Type ', ' Description ', ' Allowable Values ', ''] typically
				if len(parts) >= 4:
					typ_cell = parts[2].strip()
					mapped = _map_type_to_icon(typ_cell)
					parts[2] = f' {mapped} '
					line = '|'.join(parts)
				lines.append(line)
			new_text = '\n'.join(lines)
			try:
				with open(path, 'w', encoding='utf-8') as wf:
					wf.write(new_text)
			except Exception:
				print(f'Could not write processed markdown to {path}')
		# Copy to deploy target
		if deploy_target:
			os.makedirs(deploy_target, exist_ok=True)
			for fn in files:
				if fn == 'index.md':
					continue
				src = os.path.join(md_dir, fn)
				dst = os.path.join(deploy_target, fn)
				try:
					shutil.copy2(src, dst)
					print(f'Copied {src} -> {dst}')
				except Exception:
					print(f'Failed to copy {src} -> {dst}')

	# If requested, run postprocessing and deploy
	if getattr(args, 'apply', False):
		docs_target = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'docs', 'assays', 'metadata', 'testing')
		print(f'Postprocessing markdown in {MARKDOWN_DIR} and copying to {docs_target}')
		_postprocess_markdown(MARKDOWN_DIR, docs_target)
