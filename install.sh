#!/bin/bash

#Installing the deps
distrib=$(lsb_release -i | cut -f 2-)
echo $distrib


if [ $distrib = "Ubuntu" ] || [ $ditrib = "Debian" ]; then
	apt-get install pv
fi
if [ $distrib = "Fedora" ] || [ $distrib = "CentOS" ]; then
	yum install pv
fi

#Compiling the python project
pyinstaller tar-progress.py --onefile

#Installing the project
mv ./dist/tar-progress /usr/bin
chmod +x /usr/bin

