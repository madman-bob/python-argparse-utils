from setuptools import setup, find_packages
from os import path

import re

project_root = path.join(path.abspath(path.dirname(__file__)), '..')


def get_version():
    with open(path.join(project_root, 'argparse_utils', '__init__.py'), encoding='utf-8') as init_file:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", init_file.read(), re.M).group(1)


def get_long_description():
    with open(path.join(project_root, 'README.md'), encoding='utf-8') as readme_file:
        return readme_file.read()


setup(
    name='argparse_utils',
    version=get_version(),
    packages=find_packages(include=('argparse_utils', 'argparse_utils.*')),
    install_requires=[],

    author='Robert Wright',
    author_email='madman.bob@hotmail.co.uk',

    description='A collection of utilities for the Python standard-library argparse module',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/madman-bob/python-argparse-utils',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    python_requires='>=2.7'
)
