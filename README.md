Django-Messagegroups
====================

This Django app provides a template tag to render all messages (sent via the Django messaging
framework) and to display them grouped by category.


Install
-------

Copy the messagegroups folder to your project and add 'messagegroups' to your INSTALLED\_APPS
setting.

Usage
-----

    {% load messagegroups %}
    ...
    {% render_messages messages %}


Customize
---------

You can customize the template by overriding the `messagegroups.html` template.


Credits
-------

Inspired by Ben Tappin (via [mrben.co.uk](http://mrben.co.uk/entry/a-nicer-way-of-using-the-Django-messages-framework/)).


License
-------

Copyright 2011 Factor AG (http://factor.ch/)

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
