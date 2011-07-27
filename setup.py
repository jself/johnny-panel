#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test


setup(
    name='johnny-panel',
    version='0.1.0',
    author='Jeremy',
    author_email='',
    url='http://github.com/streeter/johnny-panel',
    description = 'A Django Debug Toolbar panel for Johnny Cache',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
    ],
    test_suite = 'johnny_panel.tests',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
