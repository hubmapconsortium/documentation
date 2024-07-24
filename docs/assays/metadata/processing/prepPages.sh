#!/bin/bash

# Directory containing markdown files
# JS_DIR="./metaJSON"
# JS_DIR="./metaJSON/clean"
MD_DIR="./metaMD/"


# Process each markdown file in the directory
for md_file in "$MD_DIR"/*.md; do
ATTNAME=$(basename $md_file .md)
TOPSTR="--- 
layout: page 
---
# $ATTNAME 

## Current Metadata Attributes 

"

## Current Metadata Attributes'

  echo "$TOPSTR" | cat - "$md_file" > temp.md && mv temp.md "$md_file"

done
