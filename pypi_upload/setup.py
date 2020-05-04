import os
import re
import sys
from pathlib import Path

from setuptools import find_packages, setup
from setuptools.command.install import install

project_root = Path(__file__).parents[1]


class VerifyCommand(install):
    """Custom command to verify module integrity"""

    description = "verify module integrity"

    @staticmethod
    def verify_git_tag():
        tag = os.getenv("CIRCLE_TAG")
        version = get_version()

        if tag != version:
            sys.exit(
                "Git tag: {0} does not match the version of this app: {1}".format(
                    tag, version
                )
            )

    def run(self):
        self.verify_git_tag()


def get_version():
    init_contents = (project_root / "argparse_utils/__init__.py").read_text(encoding="utf-8")

    return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", init_contents, re.M).group(
        1
    )


def get_requirements():
    requirements = (project_root / "requirements.txt").read_text(encoding="utf-8")

    return list(filter(None, requirements.splitlines()))


def get_long_description():
    return (project_root / "README.md").read_text(encoding="utf-8")


setup(
    name='argparse_utils',
    version=get_version(),
    packages=find_packages(include=('argparse_utils', 'argparse_utils.*')),
    install_requires=get_requirements(),
    setup_requires=["wheel"],

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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.5',
    cmdclass={"verify": VerifyCommand},
)
