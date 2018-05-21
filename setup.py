from setuptools import setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tar-progress',
    author='Henri Devigne',
    author_email='henri.devigne@bonkgaming.fr',
    url='https://github.com/henri9813/tar-progress',
    version='0.0.1',
    description="This utility offer a progress-bar to the GNU tar program, and provide it on Windows",
    long_description=long_description,
    packages=['tar_progress'],
    install_requires=['tqdm'],
    entry_points={
        'console_scripts': [
            'tar-progress=tar_progress.__main__:main'
        ]
    }
)
