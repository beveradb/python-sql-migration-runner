#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "click-log>=0.3.2",
    "mysql-connector-python>=8.0.15",
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'tox', 'flake8', 'coverage', 'coveralls']

setup(
    author="Andrew Beveridge",
    author_email='andrew@beveridge.uk',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Run MySQL migration scripts sequentially from a specified "
                "directory, keeping track of current version in the database.",
    entry_points={
        'console_scripts': [
            'migration_runner=migration_runner.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='migration_runner',
    name='migration_runner',
    packages=find_packages(include=['migration_runner']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/beveradb/migration_runner',
    version='0.3.0',
    zip_safe=False,
)
