from .interface import *
import tarfile


class WindowsArchiver(Archiver):
    plateform = "Windows"

    @classmethod
    def create(cls, filename, compression, files):
        import tqdm
        tar = tarfile.open(filename, "w:" + compression)

        toCompressSize = 0
        toCompress = list()
        for source in files:
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

    @classmethod
    def list(cls, filename, compression=""):
        tar = tarfile.open(filename, "r:" + compression)
        for file in tar:
            print(file)
    @classmethod
    def extractAll(cls, filename, compression, destination='.'):
       print("In progress...")

