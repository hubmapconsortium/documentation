#!/bin/bash

# Directory containing markdown files
MD_DIR="./metadataCopy"

# String to add
STRING_TO_ADD="---
layout: page
---
"

# Process each markdown file in the directory
for md_file in "$MD_DIR"/*.md; do
  # Prepend the string to the file
  echo "$STRING_TO_ADD" | cat - "$md_file" > temp.md && mv temp.md "$md_file"
done