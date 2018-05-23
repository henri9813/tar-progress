from .interface import *


class LinuxArchiver(Archiver):
    plateform = "Linux"

    @classmethod
    def create(cls, filename, compression, files):
        import subprocess
        files = ' '.join(files)
        size = subprocess.check_output("du -sb --apparent-size --total " + files + " | tail -n1 | awk '{printf $1}'", shell=True)
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
    def extractAll(cls, filename, compression, destination='.'):
        if compression == "gz":
            command = "(pv " + filename + " | tar -xzf - -C " + destination + " )"
        elif compression == "bz2":
            command = "(pv " + filename + " | tar -xjf - -C " + destination + " )"
        elif compression == "xz":
            command = "(pv " + filename + " | tar -xJf - -C " + destination + " )"
        else:
            command = "(pv " + filename + " | tar -xf - -C " + destination + " )"
        os.system(command)

