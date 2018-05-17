#!/usr/bin/python
import platform

if platform.system() != "Linux":
    exit("This script is only runnable on Linux")

action = False
ACTION = {
    'c': 'w:',
    'x': 'r:',
    't': 'r:'
}
compression = False
COMPRESSSION = {
    'z': 'gz',
    'j': 'bz2',
    'J': 'xz',
    False: "*"
}

others = []
OTHERS_FLAGS = [
    'v'
]

target = False
sources = list()

import os, sys

for key, argument in enumerate(sys.argv[1:]):
    if argument[0] == '-':
        for letter in argument[1:]:
            if letter in COMPRESSSION.keys():
                compression = letter
                continue
            elif letter in ACTION.keys():
                action = letter
                continue
            elif letter == "f":
                try:
                    target = sys.argv[key + 2]
                    continue
                except IndexError:
                    exit("The target must be defined after -f")
            elif letter in OTHERS_FLAGS:
                others.append(letter)
            else:
                exit("This flag: "+ letter +" doesn't exit !")
    elif argument == target:
        continue
    else:
        sources.append(argument)

if action == False or (action == "c" and compression == False):
    exit("An action or a compression mode must be defined ( compress or extract )")


mode = ACTION[action]+COMPRESSSION[compression]

import tarfile, tqdm
import subprocess

if ACTION[action] == "w:":
    if platform.system() == "Linux":
        files = ' '.join(sources)
        size = subprocess.check_output("du -sb --apparent-size --total " + files + " | tail -n1 | awk '{printf $1}'", shell=True)
        if COMPRESSSION[compression] == "bz2":
            command = "tar -cf - " + files + " | pv -s " + size + " | bzip2 > " + target
        else:
            command = "tar -cf - " + files + " | pv -s " + size + " | gzip > " + target
        os.system(command)
    else:
        tar = tarfile.open(target, mode)

        toCompressSize = 0
        toCompress = list()
        for source in sources:
            if os.path.isfile(source):
                toCompress.append(os.path.abspath(source))
                toCompressSize += os.path.getsize(source)
            else:
                for root, dirs, files in os.walk(source):
                    for dir in dirs:
                        if os.listdir(os.path.join(root, dir)) == []:
                            toCompress.append(os.path.join(root, dir))
                    for name in files:
                        toCompress.append(os.path.join(root, name))
                        toCompressSize += os.path.getsize(os.path.join(root, name))
        progressBar = tqdm.tqdm(total=toCompressSize, unit="B")
        for path in toCompress:
            tar.add(path)
            if not os.path.isdir(path):
                progressBar.update(os.path.getsize(path))
        progressBar.close()
        tar.close()

else:
    tar = tarfile.open(target, mode)
    if platform.system() == "Linux":
        if action == 't':
            command = "tar -tf " + target

        if action == 'x':
            print("Waitting implementation...")
        os.system(command)
    else:
        if action == 't':

            for file in tar:
                print(file)
        if action == 'x':
            for file in tar:
                tar.extract(file)