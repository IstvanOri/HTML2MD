import unittest

from tests.commands import suite

runner = unittest.TextTestRunner()
result = runner.run(suite())
