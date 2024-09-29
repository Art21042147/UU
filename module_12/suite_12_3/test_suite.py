import unittest
from tests_12_1 import RunnerTests
from tests_12_2 import TournamentTest

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(RunnerTests))
test_suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
