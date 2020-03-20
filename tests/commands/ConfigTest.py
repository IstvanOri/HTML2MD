import unittest

from commands.Command import Command
from commands.CommandConfigurationError import CommandConfigurationError
from commands.Config import Config


class ConfigTest(unittest.TestCase):

    def test_missconfiguration(self):
        with self.assertRaises(CommandConfigurationError):
            Config(("a", "b", "c"))

    def test_reset_after_execution(self):
        Config(("_bullet", "x")).execute()
        self.assertEqual(" * ", Command._bullet)
