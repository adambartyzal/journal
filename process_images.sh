#!/bin/bash

echo Moving IMG files to temp_directory.

temp_directory="./images/temp"

if [ ! -d "$temp_directory" ]; then
  mkdir -p "$temp_directory"
  echo "temp_directory created: $temp_directory"
else
  echo "temp_directory already exists."
fi

mv ~/downloads/IMG* $temp_directory

echo Renaming files and appending names to current raw markdown file.

raw_date=$(date +"%Y_%B")
formatted_date=${raw_date,,}
echo "Current date: $formatted_date"

current_markdown_file="$formatted_date.raw"
current_image_directory="images/$formatted_date"

python3 rename.py images/temp/ >> $current_markdown_file 2>&1

echo Moving renamed files to the correct directory.

mv images/temp/* $current_image_directory
