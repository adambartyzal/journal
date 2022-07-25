#!/bin/bash

files=$(git status --porcelain)
for file in $files; do
  if [[ $file == *.jpg ]]; then
    dir=$(dirname $file)
    if ! test -f "images/thumbnails/$dir"; then
      mkdir -p "images/thumbnails/$dir"
    fi
    dest=${file:7}
    convert "$file" -resize 700 -quality 50 "images/thumbnails/$dest"
  fi
done
