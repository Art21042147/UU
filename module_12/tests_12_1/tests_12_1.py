from runner import *
import unittest


class RunnerTests(unittest.TestCase):
    def test_walk(self):
        johnnie_walker = Runner("TestWalker")
        for _ in range(10):
            johnnie_walker.walk()
        self.assertEqual(johnnie_walker.distance, 50)

    def test_run(self):
        blade_runner = Runner("TestRunner")
        for _ in range(10):
            blade_runner.run()
        self.assertEqual(blade_runner.distance, 100)

    def test_challenge(self):
        walker = Runner("ChallengeWalker")
        runner = Runner("ChallengeRunner")
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)


if __name__ == "__main__":
    unittest.main()
