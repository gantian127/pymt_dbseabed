#! /usr/bin/env python
import os
import sys

from setuptools import Extension, find_packages, setup

entry_points = {
    "pymt.plugins": [
        "DbSeabedData=pymt_dbseabed.bmi:DbSeabedData",
    ]
}


def read(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.read()


long_description = "\n\n".join(
    [read("README.rst"), read("CREDITS.rst"), read("CHANGES.rst")]
)


setup(
    name="pymt_dbseabed",
    author="Tian Gan",
    author_email="gantian127@gmail.com",
    description="PyMT plugin for pymt_dbseabed",
    long_description=long_description,
    version="0.1",
    url="https://github.com/gantian127/pymt_dbseabed",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=["bmi", "pymt"],
    install_requires=open("requirements.txt", "r").read().splitlines(),
    packages=find_packages(),
    entry_points=entry_points,
    include_package_data=True,
)