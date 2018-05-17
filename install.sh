#!/bin/bash

#Installing the deps
distrib=$(lsb_release -i | cut -f 2-)
echo $distrib


if [ $distrib == "Ubuntu" or $ditrib == "Debian" ]; then
	apt-get install pv
fi
if [ $distrib == "Fedora" or $distrib == "CentOS" ]; then

#Compiling the python project
pyinstaller tar-progress.py --onefile

#Installing the project
mv ./dist/tar-progress /usr/bin
chmod +x /usr/bin

