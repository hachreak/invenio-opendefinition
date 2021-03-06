# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio module integrating Invenio repositories and OpenDefinition."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'httpretty>=0.8.14',
    'isort>=4.2.2',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.4.2',
    ],
    'sqlite': [
        'invenio-db>=1.0.0a9',
    ],
    'mysql': [
        'invenio-db[mysql]>=1.0.0a9',
    ],
    'postgresql': [
        'invenio-db[postgresql]>=1.0.0a9',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name in ('mysql', 'postgresql', 'sqlite'):
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.7.0',
]

install_requires = [
    'Flask>=0.11.1',
    'click>=6.4',
    'flask-celeryext>=0.2.0',
    'invenio-indexer>=1.0.0a9',
    'invenio-jsonschemas>=1.0.0a3',
    'invenio-pidstore>=1.0.0b1',
    'invenio-records>=1.0.0b1',
    'invenio-records-rest>=1.0.0a18',
    'invenio-search>=1.0.0a9',
    'jsonref>=0.1',
    'jsonresolver>=0.2.1',
    'jsonschema>=2.5.1',
    'requests>=2.9.1',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_opendefinition', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-opendefinition',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio TODO',
    license='GPLv2',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-opendefinition',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.apps': [
            'invenio_opendefinition = '
            'invenio_opendefinition:InvenioOpenDefinition',
        ],
        'invenio_i18n.translations': [
            'messages = invenio_opendefinition',
        ],
        'invenio_records.jsonresolver': [
            'invenio_opendefinition = invenio_opendefinition.resolvers',
        ],
        'invenio_celery.tasks': [
            'invenio_opendefinition = invenio_opendefinition.tasks',
        ],
        'invenio_jsonschemas.schemas': [
            'invenio_opendefinition = invenio_opendefinition.jsonschemas',
        ],
        'invenio_search.mappings': [
            'licenses = invenio_opendefinition.mappings',
        ],
        'invenio_pidstore.fetchers': [
            'opendefinition_license_fetcher = '
            'invenio_opendefinition.fetchers:license_fetcher',
        ],
        'invenio_pidstore.minters': [
            'opendefinition_license_minter = '
            'invenio_opendefinition.minters:license_minter',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 1 - Planning',
    ],
)
