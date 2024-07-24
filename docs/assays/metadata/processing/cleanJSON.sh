#!/bin/bash

# Directory containing markdown files
JS_DIR="./metaJSON"


# Process each markdown file in the directory
for js_file in "$JS_DIR"/*.json; do
  # Prepend the string to the file
  # echo "$STRING_TO_ADD" | cat - "$js_file" > temp.md && mv temp.md "$js_file"
  # echo "$STRING_TO_ADD" | cat - "$js_file" > temp.md && mv temp.md "$js_file"
  jq . $js_file > $js_file.new
done