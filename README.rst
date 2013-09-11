####################
django-messagegroups
####################

.. image:: https://secure.travis-ci.org/dbrgn/django-messagegroups.png?branch=master
    :alt: Build status
    :target: http://travis-ci.org/dbrgn/django-messagegroups

.. image:: https://pypip.in/d/django-messagegroups/badge.png
    :alt: PyPI download stats
    :target: https://crate.io/packages/django-messagegroups

This Django app provides a template tag to render all messages (sent via the
Django messaging framework) and to display them grouped by category.

Since tag v0.2, django-messagegroups is compatible with Bootstrap 1, and since
v0.3, it uses Bootstrap 2/3 markup.


Install
=======

The best way to install ``django-messagegroups`` is using pip::

    pip install django-messagegroups

To get the current development version, you can install the version from
Github::

    pip install -e git://github.com/dbrgn/django-messagegroups.git#egg=messagegroups

Finally add ``messagegroups`` to your INSTALLED\_APPS setting.


Usage
=====

::

    {% load messagegroups %}
    ...
    {% render_messages messages %}


Customize
=========

You can customize the template by overriding the ``messagegroups.html`` template.

The HTML class markup is compatible with the `Bootstrap CSS Framework
<http://twitter.github.com/bootstrap/>`_ (2/3).


Credits
=======

Inspired by Ben Tappin (via `mrben.co.uk
<http://mrben.co.uk/entry/a-nicer-way-of-using-the-Django-messages-framework/>`__).


License
=======

The MIT License (MIT)

Copyright (c) 2011-2013 Danilo Bargen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
