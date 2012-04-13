Django-Messagegroups
====================

This Django app provides a template tag to render all messages (sent via the Django messaging
framework) and to display them grouped by category.

Since tag v0.2, django-messagegroups is compatible with Bootstrap 1, and since v0.3, it uses
Bootstrap 2 markup.


Install
-------

The best way to install `django-messagegroups` is using pip:

    pip install django-messagegroups

To get the current development version, you can install the version from Github:

    pip install -e git://github.com/FactorAG/django-messagegroups.git#egg=messagegroups

Finally add `messagegroups` to your INSTALLED\_APPS setting.


Usage
-----

    {% load messagegroups %}
    ...
    {% render_messages messages %}


Customize
---------

You can customize the template by overriding the `messagegroups.html` template.

The HTML class markup is compatible with the [Bootstrap CSS Framework](http://twitter.github.com/bootstrap/) (v2).


Credits
-------

Inspired by Ben Tappin (via [mrben.co.uk](http://mrben.co.uk/entry/a-nicer-way-of-using-the-Django-messages-framework/)).


License
-------

Copyright 2011-2012 Factor AG (http://factor.ch/)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.html>.
