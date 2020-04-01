import unittest

from tests.commands.ConfigTest import ConfigTest
from tests.commands.IgnoreTest import IgnoreTest
from tests.commands.IndentTest import IndentTest
from tests.commands.LevelTest import LevelTest
from tests.commands.WrapTest import WrapTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ConfigTest())
    suite.addTest(IgnoreTest())
    suite.addTest(IndentTest())
    suite.addTest(LevelTest())
    suite.addTest(WrapTest())
    return suite