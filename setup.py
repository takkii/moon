#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='geturin',
    packages=['geturin'],
    version='1.0.0.1',
    url='https://github.com/takkii/moon',
    author='takkii',
    author_email='karuma.reason@gmail.com',
    license='MIT',
    #packages=find_packages(exclude=('tests')),
    #install_requires=['', ''],é
    #entry_points={
    #    "console_scripts": [
    #        "moon=moon.__init__:main",
    #    ],
    #},
    description='Bignyanco clone deoplete dictionary list.',
    long_description=long_description,
    keywords='geturin',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
