#!/usr/bin/env python3
"""Clean generated markdown files after generateMarkdow.py runs.

Cleaning tasks performed (in order):
  1. Remove "Allowable Values" cell content for fields whose Type is NOT an
     Allowable Value type (e.g. preparation_protocol_doi is a Textfield but
     sometimes carries stale allowable-values data).

Usage:
    python3 scripts/templateConverstion/clean_md.py [--dry-run] [--dir DIR]
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

# The icon fragment that marks a field as Allowable Value type
ALLOWABLE_VALUE_MARKER = 'title="Allowable Value"'

# Regex that matches a single markdown table row with 4 pipe-delimited cells.
# Groups: (1) attribute cell, (2) type cell, (3) description cell, (4) allowable values cell
ROW_RE = re.compile(
    r'^\|'
    r'([^|]*)'   # cell 1 – attribute
    r'\|'
    r'([^|]*)'   # cell 2 – type icon
    r'\|'
    r'([^|]*)'   # cell 3 – description
    r'\|'
    r'([^|]*)'   # cell 4 – allowable values
    r'\|[ \t]*$',
    re.MULTILINE,
)


def _is_header_or_separator(row: str) -> bool:
    """Return True for table header/separator rows that should be left alone."""
    stripped = row.strip('| \t\n')
    # separator row: cells are only dashes/colons/spaces
    if re.match(r'^[-: |]+$', stripped):
        return True
    # header row: contains 'Attribute' or 'allowable values' as plain text labels
    low = stripped.lower()
    if 'attribute' in low and 'description' in low:
        return True
    return False


def clean_allowable_values(text: str) -> tuple[str, int]:
    """Return (cleaned_text, number_of_cells_cleared)."""
    cleared = 0

    def _replace(m: re.Match) -> str:
        nonlocal cleared
        full = m.group(0)

        if _is_header_or_separator(full):
            return full

        type_cell = m.group(2)
        av_cell = m.group(4)

        # Nothing to do if AV cell is already empty
        if not av_cell.strip():
            return full

        # Only clear when type is NOT an allowable-value type
        if ALLOWABLE_VALUE_MARKER not in type_cell:
            cleared += 1
            # Preserve surrounding whitespace of the cell for tidy output
            return f'|{m.group(1)}|{m.group(2)}|{m.group(3)}|  |\n'

        return full

    cleaned = ROW_RE.sub(_replace, text)
    return cleaned, cleared


def process_file(path: Path, dry_run: bool) -> int:
    original = path.read_text(encoding='utf-8')
    cleaned, count = clean_allowable_values(original)
    if count == 0:
        return 0
    if dry_run:
        print(f'  [dry-run] would clear {count} AV cell(s) in {path.name}')
    else:
        path.write_text(cleaned, encoding='utf-8')
        print(f'  Cleared {count} AV cell(s) in {path.name}')
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true',
                        help='Report changes without writing files')
    parser.add_argument('--dir', default=None,
                        help='Directory of converted markdown files '
                             '(default: scripts/templateConverstion/converted)')
    args = parser.parse_args()

    md_dir = Path(args.dir) if args.dir else (
        Path(__file__).resolve().parent / 'converted'
    )

    if not md_dir.exists():
        print(f'Directory not found: {md_dir}')
        return 2

    md_files = sorted(md_dir.glob('*.md'))
    if not md_files:
        print(f'No markdown files found in {md_dir}')
        return 0

    total = 0
    for md in md_files:
        total += process_file(md, dry_run=args.dry_run)

    action = 'Would clear' if args.dry_run else 'Cleared'
    print(f'\n{action} {total} stale Allowable Values cell(s) across {len(md_files)} file(s).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
