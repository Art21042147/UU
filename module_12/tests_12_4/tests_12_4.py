import unittest
import logging
from rt_with_exceptions import *


logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class RunnerTests(unittest.TestCase):

    def test_walk(self):
        try:
            johnnie_walker = Runner("TestWalker", speed=-5)
            for _ in range(10):
                johnnie_walker.walk()
            self.assertEqual(johnnie_walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            blade_runner = Runner({"TestRunner": 10})
            for _ in range(10):
                blade_runner.run()
            self.assertEqual(blade_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

    def test_challenge(self):
        walker = Runner("ChallengeWalker")
        runner = Runner("ChallengeRunner")
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)
        logging.info('"test_challenge" выполнен успешно')


if __name__ == "__main__":
    unittest.main()
