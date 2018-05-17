#!/bin/bash

pyinstaller tar-progress.py --onefile
mv ./dist/tar-progress /usr/bin