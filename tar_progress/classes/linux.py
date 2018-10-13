"""
tar-progress: Classes
"""
from __future__ import print_function
from .interface import Archiver, os


class LinuxArchiver(Archiver):
    """
    Linux Archiver: using GNU tar command
    """
    platform = "Linux"

    def __init__(self):
        Archiver.__init__(self)
        import platform
        if platform.system() != self.platform:
            exit("Linux archiver enabled on non Linux system")

        import subprocess
        try:
            subprocess.check_output(["which", "pv"]).rstrip()
        except subprocess.CalledProcessError:
            exit("ERROR: pv package is not installed, install it: https://pkgs.org/download/pv")

    @classmethod
    def create(cls, filename, compression, sources):
        import subprocess
        files = ' '.join(sources)
        size = subprocess.check_output("du -sb --apparent-size --total "
                                       + files
                                       + " | tail -n1 | awk '{printf $1}'",
                                       shell=True)
        if compression == "gz":
            command = "tar -cf - " + files + " | pv -s " + size + " | gzip > " + filename
        elif compression == "bz2":
            command = "tar -cf - " + files + " | pv -s " + size + " | bzip2 > " + filename
        elif compression == "xz":
            command = "tar -cf - " + files + " | pv -s " + size + " | xz > " + filename
        else:
            command = "tar -cf - " + files + " | pv -s " + size + " > " + filename
        os.system(command)

    @classmethod
    def list(cls, filename, compression=""):
        os.system("tar -tf" + compression + " " + filename)

    @classmethod
    def extract_all(cls, filename, compression, destination='.'):
        if compression == "gz":
            command = "(pv " + filename + " | tar -xzf - -C " + destination + " )"
        elif compression == "bz2":
            command = "(pv " + filename + " | tar -xjf - -C " + destination + " )"
        elif compression == "xz":
            command = "(pv " + filename + " | tar -xJf - -C " + destination + " )"
        else:
            command = "(pv " + filename + " | tar -xf - -C " + destination + " )"
        os.system(command)

    @classmethod
    def extract(cls, filename, compression, sources, destination='.'):

        print("Not implemented at this time..")
