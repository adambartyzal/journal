#!/bin/bash
echo Converting raw files to markdown...
for file in *.raw; do
  python replace.py $file
done
echo Done

echo Generating thumbnails...
cd images
./makethumbnails.sh
cd ..
echo Done

git stage *
git status
read -p "Enter commit message: " message
git commit -m "$message"
git push
