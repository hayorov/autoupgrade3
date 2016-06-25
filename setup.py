# coding=utf-8

from setuptools import setup

__version__ = "unknown"

exec(open('autoupgrade3/version.py').read())
print("autoupgrade3 version: " + __version__)

setup(name='autoupgrade3',
      version=__version__,
      author='Alexander Khaerov',
      author_email='i@hayorov.ru',
      description='Python 3 friendly automatic upgrade of python modules and packages',
      long_description=open('README.txt').read(),
      packages=['autoupgrade3'],
      url="https://github.com/hayorov/autoupgrade3",
      install_requires=[
          "pip",
          "BeautifulSoup4",
          "six"
      ],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.5",
          "Topic :: System :: Software Distribution"
      ]
      )
