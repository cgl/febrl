#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages

setup(name='Febrl',
      version='0.4.2',
      description='Febrl (Freely extensible biomedical record linkage)',
      author='Peter Christen, 14 December 2011',
      author_email='',
      url='http://sourceforge.net/projects/febrl/',
      packages=find_packages(exclude=['data', 'tests'])
     )
