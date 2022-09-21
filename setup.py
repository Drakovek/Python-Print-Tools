#!/usr/bin/env python3

"""Setuptools setup file."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Python-Print-Tools",
    version="0.1.0",
    author="Drakovek",
    author_email="DrakovekMail@gmail.com",
    description="Utility for printing to console",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Drakovek/Python-Print-Tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.0'
)