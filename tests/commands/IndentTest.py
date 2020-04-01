import unittest

from html2md.commands.CommandConfigurationError import CommandConfigurationError
from html2md.commands.Indent import Indent


class IndentTest(unittest.TestCase):

    def test_missconfiguration0(self):
        with self.assertRaises(CommandConfigurationError):
            Indent(())

    def test_missconfiguration2(self):
        with self.assertRaises(CommandConfigurationError):
            Indent(("a", "b"))

    def test_with_empty_data(self):
        self.assertEqual("--", Indent(("--",)).execute())

    def test_with_data(self):
        cmd = Indent(("  ",))
        cmd.data = "asd"
        self.assertEqual("  asd", cmd.execute())
