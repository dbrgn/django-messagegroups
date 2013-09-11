# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from collections import defaultdict

from django import template
from django.contrib.messages.constants import DEBUG, INFO, SUCCESS, WARNING, ERROR

register = template.Library()

TAGS = {  # Bootstrap error constant mappings
    DEBUG: 'info',
    INFO: 'info',
    SUCCESS: 'success',
    WARNING: 'warning',
    ERROR: 'danger',
}


@register.inclusion_tag('messagegroups.html')
def render_messages(messages):
    grouped = defaultdict(set)
    for m in messages:
        tags = 'alert-{0} {1}'.format(TAGS[m.level], m.tags)
        grouped[(m.level, tags)].add(m.message)
    return {'messages': dict(grouped)}
