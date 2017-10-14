#!/usr/bin/env python

from distutils.core import setup

setup(
    name='cidr',
    version='0.1',
    description='CIDR ranges helper',
    license='GPLv3',
    author='deadc0de6',
    url='https://github.com/deadc0de6/cidr',
    py_modules=['cidr'],
    scripts=['cidr.py'],
    install_requires=['docopt',	'netaddr','ipaddress'],
)
