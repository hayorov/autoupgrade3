# coding=utf-8

from distutils.core import setup

__version__ = "unknown"
exec(open('autoupgrade3/version.py').read())
print("autoupgrade3 version: " + __version__)

setup(name='autoupgrade3',
      version=__version__,
      author='Jörgen Karlsson',
      author_email='jorgen@karlsson.com',
      description='Automatic upgrade of python modules and packages',
      long_description=open('README.txt').read(),
      packages=['autoupgrade3'],
      url="https://bitbucket.org/jorkar/autoupgrade3",
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
          "Topic :: System :: Software Distribution"
      ]
      )
