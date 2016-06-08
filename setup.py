# -*- coding: utf-8 -*-

import os
import sys 
import warnings
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

def read(fname):
	return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "sf_express"

PACKAGES = ["sf_express",]

DESCRIPTION = "this is a non official sdk of sf-express"

LONG_DESCRIPTION = read("README.md")

KEYWORDS = "sf python package"

URL	= ''

AUTHOR = "yinjia"

AUTHOR_EMAIL = "yinjia08@sina.com"

VERSION = "1.0"

LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)


