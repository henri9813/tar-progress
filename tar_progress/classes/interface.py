import os


class Archiver:
    plateform = "AnotherOS"

    EXTENSIONS = {
        ".gz": "gz",
        ".bz2": "bz2",
        ".xz": "xz",
        ".lzma": "xz",
        ".lz": "xz"
    }

    @classmethod
    def create(cls, filename, compression, files): raise NotImplementedError
    @classmethod
    def extract(cls, filename, compression, files, destination='.'): raise NotImplementedError
    @classmethod
    def extractAll(cls, filename, compression, destination='.'): raise NotImplementedError
    @classmethod
    def list(cls, filename): raise NotImplementedError
    @classmethod
    def detectCompressionFromFile(cls, filename):
        extension = os.path.splitext(filename)
        if len(extension) < 2:
            exit("You must specify an extension to use the automatic resolver option.")
        return cls.EXTENSIONS[extension[1]]
