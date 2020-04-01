import unittest

from html2md.commands.Command import Command
from html2md.commands.CommandConfigurationError import CommandConfigurationError
from html2md.commands.Config import Config
from html2md.commands.Level import Level


class LevelTest(unittest.TestCase):

    def runTest(self):
        self.test_missconfiguration0()
        self.test_missconfiguration2()
        self.test_with_default_level()
        self.test_with_data_level2()
        self.test_with_data_level3()

    def test_missconfiguration0(self):
        with self.assertRaises(CommandConfigurationError):
            Level(())

    def test_missconfiguration2(self):
        with self.assertRaises(CommandConfigurationError):
            Level(("a", "b"))

    def test_with_default_level(self):
        self.assertEqual("", Level(("--",)).execute())

    def test_with_data_level2(self):
        Command._level = 2
        cmd = Level(("    ",))
        cmd.data = "asd"
        self.assertEqual("    asd", cmd.execute())

    def test_with_data_level3(self):
        Command._level = 3
        cmd = Level(("    ",))
        cmd.data = "asd"
        self.assertEqual("        asd", cmd.execute())
