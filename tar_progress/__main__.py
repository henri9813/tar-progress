#!/usr/bin/python

import platform, argparse
from tar_progress.classes import interface, linux, windows


def main():
    parser = argparse.ArgumentParser(description='tar-progress by Henri Devigne')

    actions = parser.add_mutually_exclusive_group()
    actions.add_argument('-c', '--create', action="store_true",
                         help="Create archive")
    actions.add_argument('-x', '--extract', action="store_true",
                         help="Extract from archive")
    actions.add_argument('-t', '--list', action="store_true",
                         help="List content of archive")

    parser.add_argument('-z', '--gzip', action="store_const", dest="compressor", const="gz",
                        help="Use the GZIP compressor")
    parser.add_argument('-j', '--bzip2', action="store_const", dest="compressor", const="bz2",
                        help="Use the BZIP2 compressor")
    parser.add_argument('-J', '--lzma', action="store_const", dest="compressor", const="xz",
                        help="Use LZMA compressor")
    parser.add_argument('-A', '--auto-compress', action="store_const", dest="compressor", const=-1,
                        help="Automatically detect compressor from the archive name")

    parser.add_argument('-f', '--file', action="store", type=str)
    parser.add_argument('-C', '--directory', action="store", type=str)
    parser.add_argument('files', action="store", type=str, nargs="*")

    arguments = parser.parse_args()
    archiver = interface.Archiver()

    """
        Create the archiver object depending on the OS
    """

    if platform.system() == "Linux":
        archiver = linux.LinuxArchiver()
    elif platform.system() == "Windows":
        archiver = windows.WindowsArchiver()

    if arguments.create:
        if arguments.compressor is not None:
            if arguments.compressor == -1:
                arguments.compressor = archiver.detectCompressionFromFile(arguments.file)

        archiver.create(arguments.file, arguments.compressor, arguments.files)
    if arguments.list:
        archiver.list(arguments.file)
    if arguments.extract:
        archiver.extractAll(arguments.file, arguments.compressor)


if __name__ == '__main__':
    main()
