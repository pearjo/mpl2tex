#!/usr/bin/env python
from mpl2tex import __version__
from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name='mpl2tex',
      version=__version__,
      author='J. Pearson',
      url='https://github.com/pearjo/mpl2tex',
      description='Matplotlib to TeX',
      packages=['mpl2tex'],
      license='GNU General Public License 3',
      long_description=long_description,
      requires=['matplotlib'],)
