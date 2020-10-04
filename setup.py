#!/usr/bin/env python3
"The Punsy pip package"

import setuptools


def readme():
    "Return README.md as a string"
    with open("README.md", "r") as istream:
        return istream.read()


setuptools.setup(
    name="structs-py",
    version="0.0.4",
    author="Tom McKeesick",
    author_email="tmck01@gmail.com",
    description="A collection of python Data Structures/Algorithms.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/tmck-code/structs-py",
    packages=setuptools.find_packages(),
    package_data={},
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={},
    install_requires=[],
)
