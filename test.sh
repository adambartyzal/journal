#!/bin/bash

if connmanctl state | grep -q "  State = online"; then
  echo not online
fi