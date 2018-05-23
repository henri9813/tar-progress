from setuptools import setup, find_packages
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

setup(
    name='tar-progress',
    author='Henri Devigne',
    author_email='henri.devigne@bonkgaming.fr',
    url='https://github.com/henri9813/tar-progress',
    version='1.0',
    description="This utility offer a progress-bar to the GNU tar program, and provide it on Windows",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['tqdm'],
    entry_points={
        'console_scripts': [
            'tar-progress=tar_progress.__main__:main'
        ]
    }
)
