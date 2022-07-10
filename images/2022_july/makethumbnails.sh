#!/bin/bash

for filename in *$1*.jpg; do

convert "$filename" -resize 700 "./thumbnails/$filename"

done
