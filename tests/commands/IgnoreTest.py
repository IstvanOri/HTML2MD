import unittest

from html2md.commands.Ignore import Ignore


class IgnoreTest(unittest.TestCase):

    def test_execution(self):
        self.assertEqual("", Ignore(()).execute())
