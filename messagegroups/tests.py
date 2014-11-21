# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import unittest

from django.contrib.messages import DEFAULT_TAGS
from django.contrib.messages import constants

from templatetags.messagegroups import render_messages


class MessagegroupsTest(unittest.TestCase):

    class FakeMessage(object):
        def __init__(self, level, tags, message):
            self.level = level
            self.tags = tags
            self.message = message

    def test_messagegroups(self):
        """Test whether the grouping of messages has been done correctly."""
        e1 = self.FakeMessage(constants.ERROR, DEFAULT_TAGS[constants.ERROR], 'error1')
        e2 = self.FakeMessage(constants.ERROR, DEFAULT_TAGS[constants.ERROR], 'error2')
        i1 = self.FakeMessage(constants.INFO, DEFAULT_TAGS[constants.INFO], 'info1')
        other = self.FakeMessage(99, 'crazy', 'crazy1')

        groups = render_messages([e1, e2, i1, other])
        self.assertEqual(groups, {'messages': {
            (20, 'alert-info info'): set(['info1']),
            (40, 'alert-danger error'): set(['error1', 'error2']),
            (99, 'alert-level99 crazy'): set(['crazy1']),
        }})


if __name__ == '__main__':
    unittest.main()
