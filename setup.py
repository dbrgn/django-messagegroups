#!/usr/bin/env python

from distutils.core import setup

setup(name='django-messagegroups',
      version='0.4.0',
      description='Render grouped messages with the Django messaging framework',
      long_description=open('README.rst').read(),
      author='Danilo Bargen',
      author_email='gezuru@gmail.ch',
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
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
    )
