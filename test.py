import unittest
import test_reporter
import test_parser

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_reporter))
suite.addTests(loader.loadTestsFromModule(test_parser))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)