# -*- coding: utf-8 -*-

# Copyright 2016 Paul Durivage <pauldurivage+github@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

from wakeywakey import __version__

setup(
    name='wakeywakey',
    version=__version__,
    url='https://github.com/angstwad/wakeywakey.git',
    license='Apache v2.0',
    author='Paul Durivage',
    author_email='pauldurivage+github@gmail.com',
    description='Continuously mark your Slack presence as active - '
                'never appear away!',
    packages=[
        'wakeywakey'
    ],
    entry_points={
        'console_scripts': [
            'wakeywakey = wakeywakey.app:main'
        ]
    },
    classifiers=[
        'Topic :: Utilities',
        'Topic :: Communications :: Chat',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
