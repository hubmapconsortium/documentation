#!/bin/bash

# Directory containing markdown files
# JS_DIR="./metaJSON"
JS_DIR="./metaJSON/clean"
MD_DIR="./metaMD/"


# Process each markdown file in the directory
for js_file in "$JS_DIR"/*.json; do
  fileMD="$(b=${js_file##*/}; echo ${b%.*})".md
  cat $js_file | jtbl -m > $MD_DIR/$fileMD;

done
