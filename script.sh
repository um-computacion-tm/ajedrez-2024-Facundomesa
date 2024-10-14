#!/bin/bash

rm -rf .git
git clone git@github.com:um-computacion-tm/ajedrez-2024-Facundomesa tempdir
cd tempdir
git checkout Develop
cd ..
cp -r tempdir/.git .
rm -rf tempdir
