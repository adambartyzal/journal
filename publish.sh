#!/bin/bash
if git status | grep -q "nothing to commit"; then
  echo Nothing to publish.
else
  echo Converting raw files to markdown...
  for file in *.raw; do
    python replace.py $file
  done
  echo Done

  echo Generating thumbnails...
  ./newthumbnails.sh
  echo Done

  git stage *
  git status
  read -p "Enter commit message: " message
  git commit -m "$message"
fi

if connmanctl state | grep -q "online"; then
  git push
else
  echo Offline, not pushing to remote.
fi
  echo Finished.
