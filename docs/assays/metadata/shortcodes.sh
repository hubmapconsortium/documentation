#!/bin/bash

# Loop through each Markdown file in the current directory
for file in *.md; do
  # Create a temporary file to store the modified content
  temp_file=$(mktemp)

  # Read the file line by line
  while IFS= read -r line; do
    # Check if the line starts with "|"
    if [[ $line == \|* ]]; then
      # Extract the content between the first and second "|"
      before=$(echo "$line" | cut -d'|' -f1)
      middle=$(echo "$line" | cut -d'|' -f2 | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -d '?')
      after=$(echo "$line" | cut -d'|' -f3-)
      
      # Reconstruct the line with the modified middle part
      modified_line="$before|$middle|$after"
      
      # Write the modified line to the temporary file
      echo "$modified_line" >> "$temp_file"
    else
      # If the line does not start with "|", write it as is
      echo "$line" >> "$temp_file"
    fi
  done < "$file"

  # Replace the original file with the modified content
  mv "$temp_file" "$file"
done