#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io

from setuptools import setup


setup(name='django-messagegroups',
      version='0.4.5',
      description='Render grouped messages with the Django messaging framework.',
      long_description=io.open('README.rst').read(),
      author='Danilo Bargen',
      author_email='mail@dbrgn.ch',
      url='https://github.com/dbrgn/django-messagegroups',
      license='MIT',
      packages=['messagegroups', 'messagegroups.templatetags'],
      package_dir={'messagegroups': 'messagegroups'},
      package_data={'messagegroups': ['templates/*']},
      platforms=['any'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
)
