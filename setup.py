##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.app.apidoc package

"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

static_requires = [
    'mechanize >= 0.1.8',
    'zope.securitypolicy',
    'zope.app.securitypolicy',
]

tests_require = [
    'zope.app.securitypolicy',
    'zope.browserpage >= 4.1.0',
    'zope.securitypolicy',
    'zope.login',
    'zope.testing',
    'zope.testrunner',
    'zope.principalannotation',
    'zope.app.http',
    'zope.app.rotterdam >= 4.0.0',
    'zope.app.principalannotation',
    'zope.app.folder >= 4.0.0',
    'zope.applicationcontrol >= 4.0.0',
    'zope.app.wsgi',
] + static_requires

setup(
    name='zope.app.apidoc',
    version='3.7.6dev',
    author='Zope Corporation and Contributors',
    author_email='zope-dev@zope.org',
    description='API Documentation and Component Inspection for Zope 3',
    long_description=(
        read('README.rst')
        + '\n\n.. contents::\n\n' +
        read('src', 'zope', 'app', 'apidoc', 'README.rst')
        + '\n\n' +
        read('src', 'zope', 'app', 'apidoc', 'component.rst')
        + '\n\n' +
        read('src', 'zope', 'app', 'apidoc', 'interface.rst')
        + '\n\n' +
        read('src', 'zope', 'app', 'apidoc', 'presentation.rst')
        + '\n\n' +
        read('src', 'zope', 'app', 'apidoc', 'utilities.rst')
        + '\n\n' +
        read('src', 'zope', 'app', 'apidoc', 'classregistry.rst')
        + '\n\n' +
        read('CHANGES.rst')
    ),
    license="ZPL 2.1",
    keywords="zope3 api documentation",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3',
    ],
    url='http://github.com/zopefoundation/zope.app.apidoc',
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    namespace_packages=['zope', 'zope.app'],
    install_requires=[
        'persistent',
        'ZODB',
        'setuptools',
        'zope.annotation',
        'zope.app.appsetup >= 4.0.0',
        'zope.app.basicskin >= 4.0.0',
        'zope.app.exception >= 4.0.0',
        'zope.app.onlinehelp >= 4.0.0.dev0',
        'zope.app.preference >= 4.0.0.dev0',
        'zope.app.publisher',
        'zope.app.renderer >= 4.0.0.dev0',
        'zope.app.tree >= 4.0.0',
        'zope.cachedescriptors',
        'zope.component>=3.8.0',
        'zope.configuration',
        'zope.container',
        'zope.deprecation',
        'zope.hookable',
        'zope.i18n',
        'zope.interface',
        'zope.location >= 4.0.3',
        'zope.proxy',
        'zope.publisher >= 4.3.1',
        'zope.schema',
        'zope.security',
        'zope.site',
        'zope.testbrowser',
        'zope.testing',
        'zope.traversing >= 4.1.0',
    ],
    extras_require={
        'test': tests_require,
        'static': static_requires,
    },
    entry_points="""
        [console_scripts]
        static-apidoc = zope.app.apidoc.static:main
    """,
    zip_safe=False,
)
