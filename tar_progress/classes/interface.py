"""
tar-progress: Classes
"""

import os


class Archiver(object):
    """
    Archiver interface
    """
    platform = "AnotherOS"

    EXTENSIONS = {
        ".gz": "gz",
        ".bz2": "bz2",
        ".xz": "xz",
        ".lzma": "xz",
        ".lz": "xz",
        ".tar": ""
    }

    def __init__(self):
        pass

    @classmethod
    def create(cls, filename, compression, sources):
        """
        Create the archive
        :param filename: name of the archive
        :type filename: str
        :param compression: compression mode
        :type compression: str
        :param sources: files to be archived
        :type sources: list
        """
        raise NotImplementedError

    @classmethod
    def extract(cls, filename, compression, sources, destination='.'):
        """
        Extract files from a tar archive
        :param filename: name of the archive
        :type filename: str
        :param compression: compression mode
        :type compression: str
        :param sources: file to be extracted
        :type sources: list
        :param destination: final destination of extracted files
        :type destination: str
        """
        raise NotImplementedError

    @classmethod
    def extract_all(cls, filename, compression, destination='.'):
        """
        Extract whole file from an archive
        :param filename: name of the archive
        :type filename: str
        :param compression: compression mode
        :type compression: str
        :param destination: final destination of extracted files
        :type destination: str
        """
        raise NotImplementedError

    @classmethod
    def list(cls, filename, compression=""):
        """
        List the content from an archive
        :param filename: name of the archive
        :type filename: str
        :param compression: compression mode
        :type compression: str
        """
        raise NotImplementedError

    @classmethod
    def detect_compression_from_file(cls, filename):
        """
        Get compression mode from archive extension
        :param filename: name of the archive
        :return: str
        """
        extension = os.path.splitext(filename)
        if len(extension) < 2:
            exit("You must specify an extension to use the automatic resolver option.")
        return cls.EXTENSIONS[extension[1]]
