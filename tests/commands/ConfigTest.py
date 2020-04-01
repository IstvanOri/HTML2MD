import unittest

from html2md.commands.Command import Command
from html2md.commands.CommandConfigurationError import CommandConfigurationError
from html2md.commands.Config import Config


class ConfigTest(unittest.TestCase):

    def runTest(self):
        self.test_missconfiguration()
        self.test_reset_after_execution()

    def test_missconfiguration(self):
        with self.assertRaises(CommandConfigurationError):
            Config(("a", "b", "c"))

    def test_reset_after_execution(self):
        Config(("_bullet", "x")).execute()
        self.assertEqual(" * ", Command._bullet)
