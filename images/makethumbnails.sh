#!/bin/bash

if [ $# -lt 1 ]; then
	echo usage $0 dir_of_month
	exit 1
fi

thumbnails_dir="./thumbnails/$1"

if ! test -f $thumbnails_dir; then
  mkdir -p $thumbnails_dir
fi

for file in $1*.jpg; do
  convert "$file" -resize 800 -quality 70 "./thumbnails/$file"
done
