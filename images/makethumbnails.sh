#!/bin/bash

for file in */*$1*.jpg; do
  dir=$(dirname $file)
  if ! test -f "thumbnails/$dir"; then
    mkdir -p "thumbnails/$dir"
  fi
  convert "$file" -resize 700 -quality 50 "./thumbnails/$file"
done
