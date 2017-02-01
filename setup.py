#!/usr/bin/env python

from comps import meta

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=meta.name,
    version=meta.version,
    packages=('comps',),
    description="Components - numerical expressions game for children",
    long_description=meta.long_description,
    url=meta.url,
    author=meta.author,
    author_email=meta.author_email,
    license='MIT',
    install_requires=('py_expression_eval>=0.3.4'),
    classifiers=[
        'Topic :: Education',
        'pic :: Games/Entertainment',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3 :: Only'
    ],
)
