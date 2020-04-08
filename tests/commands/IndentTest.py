import unittest

from html2md.commands.CommandConfigurationError import CommandConfigurationError
from html2md.commands.Indent import Indent


class IndentTest(unittest.TestCase):

    def test_missconfiguration0(self):
        with self.assertRaises(CommandConfigurationError):
            Indent(())

    def test_missconfiguration3(self):
        with self.assertRaises(CommandConfigurationError):
            Indent(("a", "b", "c"))

    def test_with_empty_data(self):
        self.assertEqual("--", Indent(("--",)).execute())

    def test_with_data_and_first_line_indent(self):
        indent = Indent(("--",))
        indent.data = "asd"
        self.assertEqual("--asd", indent.execute())

    def test_with_data_and_first_line_does_not_indent(self):
        indent = Indent(("--", "False"))
        indent.data = "asd"
        self.assertEqual("asd", indent.execute())

    def test_with_multiline_data_and_first_line_does_not_indent(self):
        indent = Indent(("--", "False"))
        indent.data = "asd\\ndsa"
        self.assertEqual("asd\\n--dsa", indent.execute())

    def test_with_data(self):
        cmd = Indent(("  ",))
        cmd.data = "asd"
        self.assertEqual("  asd", cmd.execute())
