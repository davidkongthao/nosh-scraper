#!/bin/bash
find . -type f -name "*.jpg" -exec rm -f {} \;
find . -type f -name "*.jpeg" -exec rm -f {} \;
find . -type f -name "*.png" -exec rm -f {} \;
find . -type f -name "*.gif" -exec rm -f {} \;