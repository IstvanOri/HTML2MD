import unittest

from html2md.commands import CommandConfigurationError
from html2md.commands.CommandConfigurationError import CommandConfigurationError
from html2md.commands.Wrap import Wrap


class WrapTest(unittest.TestCase):

    def runTest(self):
        self.test_missconfiguration1()
        self.test_missconfiguration4()
        self.test_wrap()
        self.test_wrap_empty_if_allowed()
        self.test_wrap_empty_if_not_allowed()

    def test_missconfiguration1(self):
        with self.assertRaises(CommandConfigurationError):
            Wrap(("a"))

    def test_missconfiguration4(self):
        with self.assertRaises(CommandConfigurationError):
            Wrap(("a", "b", "c", "d"))

    def test_wrap(self):
        cmd = Wrap(("pre","suff"))
        cmd.data = "x"
        self.assertEqual("prexsuff", cmd.execute())

    def test_wrap_empty_if_allowed(self):
        cmd = Wrap(("pre","suff", "True"))
        cmd.data = ""
        self.assertEqual("presuff", cmd.execute())

    def test_wrap_empty_if_not_allowed(self):
        cmd = Wrap(("pre","suff"))
        cmd.data = ""
        self.assertEqual("", cmd.execute())