![alt text](doc/logo/tar-progress-logo.png "tar-progress")
[![Build Status](https://travis-ci.com/henri9813/tar-progress.svg?branch=master)](https://travis-ci.com/henri9813/tar-progress)

This utility is an adaptation from the GNU TAR program, it provide a progress-bar with a simply command : 
`tar-progress [OPTIONS] File`

## Installation

`pip install tar-progress`

This tool is cross-platform, available on Windows ( New ! ) And also Linux". Please note that in Linux, it only launch the `tar` program with a `pv` command

This program can be launched on these plateforms:

    - Linux
    - Windows
    
>Warning: On Windows i used the tarfile module from Python wich is very slow. I'm open to suggest about this performance problem
 
## Usage

`tar-progress -cjf myArchive.tar.bz2 myfiles0`

## Linux

Please install the `pv` package.
