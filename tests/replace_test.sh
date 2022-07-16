#!/bin/bash

python ../replace.py sample.raw || { echo "python failed"; exit 1;}

if diff sample.md template.md; then
  echo "OK"
else
  echo "FAIL"
fi
