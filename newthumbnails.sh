#!/bin/bash

files=$(git status --porcelain)
for file in $files; do
  if [[ $file == *.jpg ]]; then
    if test -f $file; then
      dir=$(dirname $file)
      subdir=${dir:7}
      if ! test -f "images/thumbnails/$subdir"; then
        mkdir -p "images/thumbnails/$subdir"
      fi
      dest=${file:7}
      magick "$file" -resize 800 -quality 70 "images/thumbnails/$dest"
    fi
  fi
done
