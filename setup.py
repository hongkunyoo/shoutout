import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
# def read(fname):
#     return open(os.path.join(os.path.dirname(__file__), fname)).read()

try:
   with open('README.md') as f:
       readme = f.read()
except IOError:
   readme = ''


setup(
    name = "shoutout",
    version = "0.0.1",
    author = "Hongkun Yoo",
    author_email = "hongkunyoo@gmail.com",
    description = "Shout out loud",
    license = "MIT",
    py_modules=['shoutout'],
    keywords = ["Large letters", "large letter printer", "Shout out loud"],
    url = "https://github.com/hongkunyoo/shoutout",
    download_url = "https://github.com/hongkunyoo/shoutout",
    packages=find_packages(),
    long_description=readme
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: MIT License",
    # ],
)