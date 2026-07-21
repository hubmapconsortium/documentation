#!/usr/bin/env python3
"""Generate HuBMAP assay metadata documentation from GitHub issues.

Issue format:
  * Title: assay name
  * Body: assay description and exactly one ingest-validation-tools URL

Usage:
  python3 scripts/metadata-generator/generate.py 70 71
  python3 scripts/metadata-generator/generate.py https://github.com/OWNER/REPO/issues/70
  python3 scripts/metadata-generator/generate.py --dry-run 70
  python3 scripts/metadata-generator/generate.py --self-test

The generator uses the public HRA Knowledge Graph for HRAVS allowable values.
It has no third-party Python dependencies and requires no API key.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlencode, urlparse
from urllib.request import Request, urlopen


IVT_HOST = "hubmapconsortium.github.io"
IVT_PATH_PREFIX = "/ingest-validation-tools/"
CEDAR_OPEN_HOST = "open.metadatacenter.org"
OPENVIEW_HOST = "openview.metadatacenter.org"
HRA_SPARQL_URL = "https://lod.humanatlas.io/sparql"
HRAVS_GRAPH = "https://purl.humanatlas.io/vocab/hravs"
HRAVS_CONCEPT_PATTERN = re.compile(
    r"https://purl\.humanatlas\.io/vocab/hravs#[A-Za-z0-9_]+"
)
METADATA_DIR = Path("docs/assays/metadata")
INDEX_PATH = METADATA_DIR / "index.md"

TEXT_ICON = '<i class="fa-solid fa-font" title="Textfield" aria-label="Textfield"></i>'
RADIO_ICON = '<i class="fa-solid fa-circle-dot" title="Radio" aria-label="Radio"></i>'
VALUE_ICON = (
    '<i class="fa-solid fa-circle-nodes" title="Allowable Value" '
    'aria-label="Allowable Value"></i>'
)


class GeneratorError(RuntimeError):
    """An expected, user-actionable generator failure."""


@dataclass(frozen=True)
class Issue:
    number: int
    title: str
    body: str
    url: str
    repo: str


@dataclass(frozen=True)
class Assay:
    name: str
    description: str
    schema_index_url: str
    slug: str


@dataclass(frozen=True)
class SchemaLink:
    url: str
    version: str


@dataclass(frozen=True)
class Field:
    attribute: str
    description: str
    required: bool
    kind: str
    allowable_values: tuple[str, ...] = ()


def http_get(url: str, *, headers: dict[str, str] | None = None) -> bytes:
    request_headers = {"User-Agent": "HuBMAP-documentation-metadata-generator/1.0"}
    request_headers.update(headers or {})
    request = Request(url, headers=request_headers)
    try:
        with urlopen(request, timeout=45) as response:
            return response.read()
    except HTTPError as exc:
        raise GeneratorError(f"HTTP {exc.code} while fetching {url}") from exc
    except URLError as exc:
        raise GeneratorError(f"Could not fetch {url}: {exc.reason}") from exc


def detect_repo(root: Path) -> str:
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise GeneratorError("Could not determine the GitHub repository from git remote 'origin'.")
    remote = result.stdout.strip()
    match = re.search(r"github\.com[/:]([^/]+/[^/]+?)(?:\.git)?$", remote)
    if not match:
        raise GeneratorError(f"The origin remote is not a recognizable GitHub repository: {remote}")
    return match.group(1)


def parse_issue_reference(reference: str, default_repo: str) -> tuple[str, int]:
    if reference.isdigit():
        return default_repo, int(reference)
    match = re.fullmatch(
        r"https?://github\.com/([^/]+/[^/]+)/issues/(\d+)/?", reference
    )
    if not match:
        raise GeneratorError(
            f"Invalid issue reference {reference!r}; use an issue number or full GitHub issue URL."
        )
    return match.group(1), int(match.group(2))


def fetch_issue(reference: str, default_repo: str, root: Path) -> Issue:
    repo, number = parse_issue_reference(reference, default_repo)
    result = subprocess.run(
        [
            "gh",
            "issue",
            "view",
            str(number),
            "--repo",
            repo,
            "--json",
            "number,title,body,url",
        ],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise GeneratorError(f"Could not read {repo} issue #{number} with gh: {detail}")
    return issue_from_gh_data(json.loads(result.stdout), repo, number)


def issue_from_gh_data(data: dict[str, Any], repo: str, number: int) -> Issue:
    issue_url = str(data["url"])
    if re.search(r"/pull/\d+/?$", urlparse(issue_url).path):
        raise GeneratorError(
            f"{repo}#{number} is a pull request, not an issue; "
            "check the assay issue number or pass its full issue URL."
        )
    return Issue(
        number=int(data["number"]),
        title=data["title"].strip(),
        body=data.get("body", ""),
        url=issue_url,
        repo=repo,
    )


def parse_assay(issue: Issue) -> Assay:
    url_matches = list(re.finditer(r"https?://[^\s)>]+", issue.body))
    if not url_matches:
        raise GeneratorError(
            f"Issue #{issue.number} contains no URLs; check the issue number and "
            "repository, then place its ingest-validation-tools URL at the bottom."
        )

    final_match = url_matches[-1]
    schema_url = final_match.group().rstrip(".,")
    parsed_schema_url = urlparse(schema_url)
    if (
        parsed_schema_url.netloc != IVT_HOST
        or not parsed_schema_url.path.startswith(IVT_PATH_PREFIX)
    ):
        raise GeneratorError(
            f"The final link in issue #{issue.number} must be an "
            "ingest-validation-tools URL."
        )

    parts = [part for part in urlparse(schema_url).path.split("/") if part]
    if len(parts) < 2:
        raise GeneratorError(f"Could not derive an assay slug from {schema_url}")
    slug = parts[-2] if parts[-1] == "current" else parts[-1]

    body_without_url = issue.body[: final_match.start()] + issue.body[final_match.end() :]
    raw_blocks = [
        block.strip()
        for block in re.split(r"\n\s*\n", body_without_url)
        if block.strip()
    ]
    description_blocks: list[str] = []
    if raw_blocks:
        first_lines = [line.strip() for line in raw_blocks[0].splitlines() if line.strip()]
        if first_lines and first_lines[0].casefold() == issue.title.casefold():
            first_lines.pop(0)
        if first_lines:
            description_blocks.append(" ".join(first_lines))
        description_blocks.extend(raw_blocks[1:])
    description = " ".join(
        re.sub(r"\s+", " ", block).strip()
        for block in description_blocks
        if block.strip()
    ).strip()
    if not issue.title or not description:
        raise GeneratorError(
            f"Issue #{issue.number} must provide an assay name and description before the URL."
        )
    return Assay(
        name=issue.title,
        description=description,
        schema_index_url=schema_url,
        slug=slug,
    )


class MetadataSchemaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_heading = False
        self.heading_level = ""
        self.heading_text: list[str] = []
        self.in_section = False
        self.current_href: str | None = None
        self.current_text: list[str] = []
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h1", "h2", "h3"}:
            self.in_heading = True
            self.heading_level = tag
            self.heading_text = []
        elif self.in_section and tag == "a":
            self.current_href = dict(attrs).get("href")
            self.current_text = []

    def handle_data(self, data: str) -> None:
        if self.in_heading:
            self.heading_text.append(data)
        if self.current_href is not None:
            self.current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.current_href is not None and tag == "a":
            self.links.append((self.current_href, "".join(self.current_text).strip()))
            self.current_href = None
            self.current_text = []
        if self.in_heading and tag == self.heading_level:
            heading = " ".join("".join(self.heading_text).split()).casefold()
            self.in_section = heading == "metadata schema"
            self.in_heading = False


def find_current_schema(page: bytes, source_url: str) -> SchemaLink:
    parser = MetadataSchemaParser()
    parser.feed(page.decode("utf-8", errors="replace"))
    matches = [
        (href, text)
        for href, text in parser.links
        if "use this one" in text.casefold()
        and urlparse(href).netloc == OPENVIEW_HOST
    ]
    if len(matches) != 1:
        raise GeneratorError(
            f"Expected one '(use this one)' OpenView link under Metadata schema at "
            f"{source_url}; found {len(matches)}."
        )
    href, text = matches[0]
    version = re.sub(
        r"\s*\(\s*use this one\s*\)\s*", "", text, flags=re.I
    ).strip()
    return SchemaLink(url=href, version=version or "Current version")


def cedar_api_url(openview_url: str) -> str:
    parsed = urlparse(openview_url)
    if parsed.netloc != OPENVIEW_HOST or not parsed.path.startswith("/templates/"):
        raise GeneratorError(f"Unsupported OpenView template URL: {openview_url}")
    template_uri = unquote(parsed.path.removeprefix("/templates/"))
    if not re.fullmatch(
        r"https://repo\.metadatacenter\.org/templates/[0-9a-f-]+", template_uri
    ):
        raise GeneratorError(f"Could not extract a CEDAR template ID from {openview_url}")
    return f"https://{CEDAR_OPEN_HOST}/templates/{quote(template_uri, safe='')}"


class HraValueSource:
    """Read and cache HRAVS narrower values from the public HRA SPARQL endpoint."""

    def __init__(
        self,
        getter: Callable[..., bytes] = http_get,
    ) -> None:
        self.getter = getter
        self.cache: dict[str, tuple[str, ...]] = {}

    def query(self, sparql: str) -> dict[str, Any]:
        url = f"{HRA_SPARQL_URL}?{urlencode({'query': sparql})}"
        data = self.getter(
            url, headers={"Accept": "application/sparql-results+json"}
        )
        return json.loads(data)

    def narrower_values(self, branch: dict[str, Any]) -> tuple[str, ...]:
        acronym = branch.get("acronym") or "HRAVS"
        uri = branch.get("uri")
        if acronym != "HRAVS" or not isinstance(uri, str):
            raise GeneratorError(
                "Only HRAVS controlled-value branches are supported by the keyless HRA lookup."
            )
        if not HRAVS_CONCEPT_PATTERN.fullmatch(uri):
            raise GeneratorError(f"Unsupported HRAVS concept URI: {uri}")
        if uri in self.cache:
            return self.cache[uri]

        sparql = f"""
SELECT DISTINCT ?label
WHERE {{
  GRAPH <{HRAVS_GRAPH}> {{
    <{uri}> <http://www.w3.org/2004/02/skos/core#narrower> ?child .
    ?child <http://www.w3.org/2004/02/skos/core#prefLabel> ?label .
    FILTER(LANG(?label) = "" || LANGMATCHES(LANG(?label), "en"))
  }}
}}
ORDER BY LCASE(STR(?label))
""".strip()
        data = self.query(sparql)
        bindings = data.get("results", {}).get("bindings", [])
        values = tuple(
            str(binding["label"]["value"]).strip()
            for binding in bindings
            if isinstance(binding, dict)
            and isinstance(binding.get("label"), dict)
            and binding["label"].get("value")
        )
        if not values:
            raise GeneratorError(f"HRA returned no narrower values for {uri}")
        self.cache[uri] = values
        return values

    def version(self) -> str:
        sparql = f"""
SELECT ?version
WHERE {{
  GRAPH <{HRAVS_GRAPH}> {{
    <{HRAVS_GRAPH}> <http://schema.org/version> ?version .
  }}
}}
LIMIT 1
""".strip()
        data = self.query(sparql)
        bindings = data.get("results", {}).get("bindings", [])
        if not bindings or not bindings[0].get("version", {}).get("value"):
            raise GeneratorError("HRA did not report its current HRAVS graph version.")
        return str(bindings[0]["version"]["value"])


def cedar_value_is_required(field_name: str, prop: dict[str, Any]) -> bool:
    """Return the required-value flag OpenView displays for a CEDAR field."""
    constraints = prop.get("_valueConstraints") or {}
    raw_value = constraints.get("requiredValue", False)
    if isinstance(raw_value, bool):
        return raw_value
    if isinstance(raw_value, str) and raw_value.casefold() in {"true", "false"}:
        return raw_value.casefold() == "true"
    raise GeneratorError(
        f"Field {field_name} has an invalid CEDAR requiredValue: {raw_value!r}"
    )


def fields_from_template(
    template: dict[str, Any],
    narrower_fetcher: Callable[[dict[str, Any]], tuple[str, ...]],
) -> list[Field]:
    properties = template.get("properties", {})
    order = template.get("_ui", {}).get("order", [])
    names = list(order) + [name for name in properties if name not in order]
    value_required_names = {
        name
        for name, prop in properties.items()
        if isinstance(prop, dict) and cedar_value_is_required(name, prop)
    }
    fields: list[Field] = []
    ignored = {"@context", "@id", "@type", "schema:name", "schema:description"}
    for name in names:
        if name in ignored:
            continue
        prop = properties.get(name)
        if not isinstance(prop, dict) or "schema:name" not in prop:
            continue
        constraints = prop.get("_valueConstraints", {})
        branches = constraints.get("branches") or []
        literals = constraints.get("literals") or []
        kind = "text"
        values: tuple[str, ...] = ()
        if branches:
            if len(branches) != 1:
                raise GeneratorError(
                    f"Field {name} has {len(branches)} allowable-value branches; expected one."
                )
            kind = "allowable"
            values = narrower_fetcher(branches[0])
        elif literals:
            kind = "radio"
            values = tuple(
                str(item.get("label") or item.get("value") or item.get("prefLabel"))
                if isinstance(item, dict)
                else str(item)
                for item in literals
            )
        # Numeric and link controls intentionally use the documentation text-field icon.
        fields.append(
            Field(
                attribute=str(prop.get("schema:name") or name),
                description=str(prop.get("schema:description") or ""),
                # CEDAR's template-level `required` array is structural: it says
                # the field object must exist. OpenView's required-value marker is
                # specifically `_valueConstraints.requiredValue` on the field.
                required=name in value_required_names,
                kind=kind,
                allowable_values=values,
            )
        )
    if not fields:
        raise GeneratorError("The selected CEDAR template contains no metadata fields.")
    return fields


def clean_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().replace("|", "\\|")


def render_page(assay: Assay, fields: list[Field]) -> str:
    lines = [
        "---",
        "layout: page-triary",
        "---",
        "",
        f"# {assay.name} Metadata Attributes",
        "",
        f"Fields that are collected for {assay.name} data, available at ```dataset.metadata.<attribute>```",
        "&nbsp;",
        "",
        '<span style="color:red" title="Required">*</span><span class="requiredNote"> indicates a required field</span>',
        "",
        "| Attribute | Type | Description | Allowable Values |",
        "|------|------|-------------|-------------------|",
    ]
    for field in fields:
        attribute = clean_cell(field.attribute)
        if field.required:
            attribute += ' <span class="requiredMark">*</span>'
        icon = {"allowable": VALUE_ICON, "radio": RADIO_ICON}.get(
            field.kind, TEXT_ICON
        )
        values = " ".join(
            f"```{clean_cell(value)}```" for value in field.allowable_values
        )
        lines.append(
            f"| {attribute} | {icon} | {clean_cell(field.description)} | {values} |"
        )
    return "\n".join(lines) + "\n"


def index_row(assay: Assay) -> str:
    name = clean_cell(assay.name)
    description = clean_cell(assay.description)
    return (
        f'| [{name}]({assay.schema_index_url}) '
        f'[<img src="info3.png" width="14">]({assay.slug} "Attribute description")'
        f" | {description} |\n"
    )


def row_sort_name(row: str) -> str:
    cell = row.split("|", 2)[1].strip()
    match = re.match(r"\[([^]]+)]", cell)
    if match:
        cell = match.group(1)
    return re.sub(r"[^a-z0-9]+", "", cell.casefold())


def row_metadata_slug(row: str) -> str | None:
    match = re.search(r'\]\(([^ )]+)\s+"Attribute description"\)', row)
    return match.group(1) if match else None


def update_index(content: str, assay: Assay) -> str:
    lines = content.splitlines(keepends=True)
    header = next(
        (i for i, line in enumerate(lines) if line.startswith("| Dataset Type |")),
        None,
    )
    if header is None or header + 1 >= len(lines):
        raise GeneratorError("Could not find the assay metadata index table.")
    start = header + 2
    end = start
    while end < len(lines) and lines[end].lstrip().startswith("|"):
        end += 1
    rows = [row for row in lines[start:end] if row_metadata_slug(row) != assay.slug]
    new_row = index_row(assay)
    new_name = row_sort_name(new_row)
    insert_at = next(
        (index for index, row in enumerate(rows) if row_sort_name(row) > new_name),
        len(rows),
    )
    rows.insert(insert_at, new_row)
    lines[start:end] = rows
    return "".join(lines)


def repository_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise GeneratorError("Run this command from inside the documentation git repository.")
    return Path(result.stdout.strip())


def prepare_issue(
    issue: Issue, value_source: HraValueSource
) -> tuple[Assay, SchemaLink, list[Field]]:
    assay = parse_assay(issue)
    schema_link = find_current_schema(
        http_get(assay.schema_index_url), assay.schema_index_url
    )
    template = json.loads(http_get(cedar_api_url(schema_link.url)))
    fields = fields_from_template(template, value_source.narrower_values)
    return assay, schema_link, fields


def report_results(
    prepared: list[tuple[Issue, Assay, SchemaLink, list[Field]]],
    hravs_version: str,
    *,
    prefix: str,
) -> None:
    for issue, assay, schema_link, fields in prepared:
        print(
            f"{prefix} docs/assays/metadata/{assay.slug}.md from "
            f"{issue.repo}#{issue.number} "
            f"({schema_link.version}, {len(fields)} fields, "
            f"{sum(field.required for field in fields)} required, "
            f"HRAVS {hravs_version})"
        )


def write_results(
    prepared: list[tuple[Issue, Assay, SchemaLink, list[Field]]],
    root: Path,
    hravs_version: str,
) -> list[Path]:
    index_path = root / INDEX_PATH
    index_content = index_path.read_text(encoding="utf-8")
    for _, assay, _, _ in prepared:
        index_content = update_index(index_content, assay)

    output_paths = []
    for _, assay, _, fields in prepared:
        output_path = root / METADATA_DIR / f"{assay.slug}.md"
        output_path.write_text(render_page(assay, fields), encoding="utf-8")
        output_paths.append(output_path)
    index_path.write_text(index_content, encoding="utf-8")
    report_results(prepared, hravs_version, prefix="Generated")
    return output_paths


def run_self_tests() -> bool:
    import unittest

    class GeneratorTests(unittest.TestCase):
        def setUp(self) -> None:
            self.issue = Issue(
                number=70,
                title="DNA Methylation",
                body=(
                    "DNA Methylation\n"
                    "DNA methylation adds a methyl group to DNA.\n\n"
                    "https://hubmapconsortium.github.io/ingest-validation-tools/"
                    "dna-methylation/current/"
                ),
                url="https://github.com/hubmapconsortium/documentation/issues/70",
                repo="hubmapconsortium/documentation",
            )

        def test_issue_body(self) -> None:
            assay = parse_assay(self.issue)
            self.assertEqual(assay.name, "DNA Methylation")
            self.assertEqual(
                assay.description, "DNA methylation adds a methyl group to DNA."
            )
            self.assertEqual(assay.slug, "dna-methylation")

        def test_issue_body_without_repeated_title(self) -> None:
            issue = Issue(
                71,
                "New Assay",
                "Description only.\n\nhttps://hubmapconsortium.github.io/"
                "ingest-validation-tools/new-assay/current/",
                "https://github.com/hubmapconsortium/documentation/issues/71",
                "hubmapconsortium/documentation",
            )
            self.assertEqual(parse_assay(issue).description, "Description only.")

        def test_final_link_selects_schema_with_other_links_present(self) -> None:
            issue = Issue(
                72,
                "Linked Assay",
                "Linked Assay\nSee https://example.org/protocol for context.\n\n"
                "https://hubmapconsortium.github.io/ingest-validation-tools/"
                "old-assay/current/\n\n"
                "https://hubmapconsortium.github.io/ingest-validation-tools/"
                "linked-assay/current/",
                "https://github.com/hubmapconsortium/documentation/issues/72",
                "hubmapconsortium/documentation",
            )
            assay = parse_assay(issue)
            self.assertEqual(assay.slug, "linked-assay")
            self.assertIn("https://example.org/protocol", assay.description)

        def test_issue_references(self) -> None:
            self.assertEqual(
                parse_issue_reference("70", "hubmapconsortium/documentation"),
                ("hubmapconsortium/documentation", 70),
            )
            self.assertEqual(
                parse_issue_reference(
                    "https://github.com/somewhere/else/issues/12", "ignored/repo"
                ),
                ("somewhere/else", 12),
            )

        def test_pull_request_number_is_rejected_as_an_issue(self) -> None:
            with self.assertRaisesRegex(GeneratorError, "is a pull request"):
                issue_from_gh_data(
                    {
                        "number": 110,
                        "title": "package-lock update",
                        "body": "",
                        "url": "https://github.com/hubmapconsortium/documentation/pull/110",
                    },
                    "hubmapconsortium/documentation",
                    110,
                )

        def test_current_schema_section(self) -> None:
            page = b"""
            <h2>Metadata schema</h2>
            <a href="https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fd70bfe24-e82a-46cb-9369-28ae03660d97">Version 2 (use this one)</a>
            <h2>Directory schemas</h2>
            <a href="https://openview.metadatacenter.org/templates/wrong">Version 3 (use this one)</a>
            """
            link = find_current_schema(page, "https://example.test")
            self.assertEqual(link.version, "Version 2")
            self.assertIn("d70bfe24-e82a-46cb-9369-28ae03660d97", link.url)

        def test_hra_values_are_keyless_and_cached(self) -> None:
            calls = []

            def fake_get(url: str, *, headers: dict[str, str] | None = None) -> bytes:
                calls.append((url, headers))
                return json.dumps(
                    {
                        "results": {
                            "bindings": [
                                {"label": {"value": "Alpha"}},
                                {"label": {"value": "Beta"}},
                            ]
                        }
                    }
                ).encode()

            source = HraValueSource(fake_get)
            branch = {
                "acronym": "HRAVS",
                "uri": "https://purl.humanatlas.io/vocab/hravs#HRAVS_1000401",
            }
            self.assertEqual(source.narrower_values(branch), ("Alpha", "Beta"))
            self.assertEqual(source.narrower_values(branch), ("Alpha", "Beta"))
            self.assertEqual(len(calls), 1)
            self.assertIn("lod.humanatlas.io", calls[0][0])
            self.assertEqual(calls[0][1]["Accept"], "application/sparql-results+json")

        def test_hra_rejects_non_hravs_branch(self) -> None:
            source = HraValueSource(lambda *args, **kwargs: b"{}")
            with self.assertRaisesRegex(GeneratorError, "Only HRAVS"):
                source.narrower_values(
                    {"acronym": "OTHER", "uri": "https://example.test/value"}
                )

        def test_field_types(self) -> None:
            template = {
                "_ui": {"order": ["count", "doi", "choice", "controlled"]},
                "required": ["doi"],
                "properties": {
                    "count": {
                        "schema:name": "count",
                        "schema:description": "A number",
                        "_ui": {"inputType": "numeric"},
                        "_valueConstraints": {"requiredValue": True},
                    },
                    "doi": {
                        "schema:name": "doi",
                        "schema:description": "A link",
                        "_ui": {"inputType": "link"},
                        "_valueConstraints": {},
                    },
                    "choice": {
                        "schema:name": "choice",
                        "schema:description": "Yes or no",
                        "_valueConstraints": {
                            "literals": [{"label": "Yes"}, {"label": "No"}]
                        },
                    },
                    "controlled": {
                        "schema:name": "controlled",
                        "schema:description": "Pick one",
                        "_valueConstraints": {
                            "branches": [
                                {
                                    "acronym": "HRAVS",
                                    "uri": "https://purl.humanatlas.io/vocab/hravs#HRAVS_1000401",
                                }
                            ]
                        },
                    },
                },
            }
            fields = fields_from_template(template, lambda branch: ("A", "B"))
            self.assertEqual(
                [field.kind for field in fields],
                ["text", "text", "radio", "allowable"],
            )
            self.assertTrue(fields[0].required)
            self.assertFalse(fields[1].required)
            self.assertFalse(fields[2].required)
            self.assertFalse(fields[3].required)
            self.assertEqual(fields[2].allowable_values, ("Yes", "No"))
            self.assertEqual(fields[3].allowable_values, ("A", "B"))

        def test_cedar_required_value_flag(self) -> None:
            self.assertTrue(
                cedar_value_is_required(
                    "parent_sample_id",
                    {"_valueConstraints": {"requiredValue": True}},
                )
            )
            self.assertFalse(
                cedar_value_is_required(
                    "lab_id", {"_valueConstraints": {"requiredValue": False}}
                )
            )
            self.assertFalse(cedar_value_is_required("optional", {}))
            self.assertTrue(
                cedar_value_is_required(
                    "legacy", {"_valueConstraints": {"requiredValue": "true"}}
                )
            )
            with self.assertRaisesRegex(GeneratorError, "invalid CEDAR"):
                cedar_value_is_required(
                    "broken", {"_valueConstraints": {"requiredValue": 1}}
                )

        def test_page_rendering(self) -> None:
            assay = parse_assay(self.issue)
            page = render_page(
                assay,
                [
                    Field("count", "A number", True, "text"),
                    Field(
                        "choice",
                        "Pick one",
                        False,
                        "allowable",
                        ("A", "B"),
                    ),
                ],
            )
            self.assertIn("# DNA Methylation Metadata Attributes", page)
            self.assertIn('count <span class="requiredMark">*</span>', page)
            self.assertIn(TEXT_ICON, page)
            self.assertIn("```A``` ```B```", page)
            self.assertNotIn("fa-arrow-up-right-from-square", page)

        def test_index_replacement_is_idempotent(self) -> None:
            assay = parse_assay(self.issue)
            index = """before
| Dataset Type | Description |
|--------------|-------------|
| Alpha [<img src="info3.png" width="14">](alpha "Attribute description") | Alpha |
| Old DNA [<img src="info3.png" width="14">](dna-methylation "Attribute description") | Old |
| Zebra [<img src="info3.png" width="14">](zebra "Attribute description") | Zebra |
{: .assay-metadata-index }
after
"""
            once = update_index(index, assay)
            twice = update_index(once, assay)
            self.assertEqual(once, twice)
            self.assertEqual(
                once.count('dna-methylation "Attribute description"'), 1
            )
            self.assertIn("DNA methylation adds a methyl group to DNA.", once)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(GeneratorTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return result.wasSuccessful()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate assay metadata pages and index entries from GitHub issues."
    )
    parser.add_argument(
        "issues",
        nargs="*",
        help="Issue numbers from this repo and/or full GitHub issue URLs",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and render everything without writing pages or the index",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run the generator's offline test suite",
    )
    args = parser.parse_args(argv)

    if args.self_test:
        if args.issues:
            parser.error("--self-test does not accept issue references")
        return 0 if run_self_tests() else 1
    if not args.issues:
        parser.error("provide at least one issue number or URL")

    try:
        root = repository_root()
        repo = detect_repo(root)
        value_source = HraValueSource()
        issues = [fetch_issue(reference, repo, root) for reference in args.issues]
        # Complete every network read before writing so a failed item cannot leave a
        # partially generated batch in the working tree.
        prepared = [
            (issue, *prepare_issue(issue, value_source)) for issue in issues
        ]
        hravs_version = value_source.version()
        if args.dry_run:
            report_results(prepared, hravs_version, prefix="Would generate")
        else:
            write_results(prepared, root, hravs_version)
    except (GeneratorError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
