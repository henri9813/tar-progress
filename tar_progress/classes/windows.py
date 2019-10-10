"""
tar-progress: Classes
"""
from __future__ import print_function

import platform
import sys
import tarfile
import tqdm

from .interface import Archiver, os


class WindowsArchiver(Archiver):
    """
    Windows archiver: using tarfile module from python
    """
    platform = "Windows"

    def __init__(self):
        Archiver.__init__(self)
        if platform.system() != self.platform:
            sys.exit("Windows archiver enabled on non windows system")

    @classmethod
    def open(cls, filename, compression="", mode="r"):
        """
        Open a tarfile
        :param filename: name of the file to open
        :type filename: str
        :param compression: type of compression ( cf tarfile.py:1520 open method )
        :type compression: str
        :param mode: read/write
        :type mode: str
        :return: TAR file
        :rtype: TarFile
        """
        if compression is None:
            compression = cls.detect_compression_from_file(filename)
        return tarfile.open(filename, mode + ":" + compression)

    @classmethod
    def create(cls, filename, compression, sources):
        tar = cls.open(filename, compression, mode="w")

        to_compress, to_compress_size = cls.get_files(sources)

        progress_bar = tqdm.tqdm(total=to_compress_size, unit="B")
        for path in to_compress:
            tar.add(path)
            if not os.path.isdir(path):
                progress_bar.update(os.path.getsize(path))
        progress_bar.close()
        tar.close()

    @classmethod
    def get_files(cls, sources):
        """
        Return the files and the size of sources paths including subdirectory etc...
        :param sources: files and directory to analyse
        :type sources: list
        :return: list of files and the total size of files
        :rtype: list and int
        """
        size = 0
        paths = list()
        for source in sources:
            if os.path.isfile(source):
                paths.append(os.path.abspath(source))
                size += os.path.getsize(source)
            else:
                for root, dirs, files in os.walk(source):
                    for directory in dirs:
                        if not os.listdir(os.path.join(root, directory)):
                            paths.append(os.path.join(root, directory))
                    for name in files:
                        paths.append(os.path.join(root, name))
                        size += os.path.getsize(os.path.join(root, name))
        return paths, size

    @classmethod
    def list(cls, filename, compression=""):
        tar = tarfile.open(filename, "r:" + compression)
        for path in tar:
            print(path)

    @classmethod
    def extract_all(cls, filename, compression, destination='.'):
        tar = cls.open(filename=filename, mode="r", compression=compression)
        for member in tqdm.tqdm(tar.getmembers()):
            tar.extract(member)

    @classmethod
    def extract(cls, filename, compression, sources, destination='.'):
        print("Not implemented at this time..")
