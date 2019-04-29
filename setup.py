#!/usr/bin/python

import os
from setuptools import setup, find_packages

# Get MAJOR.MIN.PATCH version from version.info file. The 'version.info' file is coming from code
version_info_file_name = 'VERSION.info'
version_info_path_abs = os.path.join(os.path.dirname(__file__), version_info_file_name)
if os.path.exists(version_info_path_abs):
    version_semantic = open(version_info_path_abs).read().strip()
else:
    raise FileNotFoundError("'{filename}' not found. This file is mandatory to define MAJOR.MIN.PATCH value of semantic version".format(filename=version_info_file_name))

setup(
    name='monkfreemobile',
    version=version_semantic,
    description='FreeMobile Library for Monkeys',
    long_description='Python module for Monkeys who needs to control some services of the French mobile network provider named "Free Mobile" (ex. SMS API)',
    long_description_content_type='text/plain',
    url='https://github.com/MonkeySynapse/Monk_FreeMobile',
    author='Monkey Synapse',
    author_email='monkey.synapse@gmail.com',
    license='MIT',

    # HELP - Classifier List: https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Telephony',
    ],
    keywords='MonK MonkeySynapse Free Mobile FreeMobile API SMS',
    project_urls={
    #     'Documentation': 'No documentation yet',
    #     'Funding': 'No budget',
    #     'Say Thanks!': 'Thanks',
        'Source': 'https://github.com/MonkeySynapse/Monk_FreeMobile',
        'Pipeline': 'https://dev.azure.com/monkeysynapse/MonK_FreeMobile/_apis/build/status/MonK_FreeMobile-Python%20package-CI?branchName=master',
    #     'Tracker': 'No tracker',
    },
    packages=find_packages(),
    install_requires=[
        'requests>=2.21.0',
    ],
    python_requires='>=2.7,!=3.0.*,!=3.1.*',
)
