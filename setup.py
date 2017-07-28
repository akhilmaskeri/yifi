import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()

setup(
    name = "yifi",
    version = "0.0.2",
    author = "vitaminC",
    author_email = "dmakhil@gmail.com",
    description = ("browse yifi on your command line"),
    entry_points={'console_scripts':['yifi=yifi.command_line:main']},
    license = "GPLv3",
    keywords = "yifi torrent download",
    packages = ['yifi'],
    long_description = read('help.txt'),
    classifiers=[
        "Development status :: Alpha",
        "Topic :: Utilites",
        "License :: GPLv3 License"
    ],
)

