from runner_and_tournament import *
import unittest


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.usain = Runner("Usain", 10)
        self.andrei = Runner("Andrei", 9)
        self.nick = Runner("Nick", 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_1_usain_vs_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_1_usain_vs_nick"] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    def test_2_andrei_vs_nick(self):
        tournament = Tournament(90, self.andrei, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_2_andrei_vs_nick"] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    def test_3_usain_andrei_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        result = tournament.start()
        TournamentTest.all_results["test_3_usain_andrei_and_nick"] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    def test_4_time_result(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        result = tournament.start()
        slower = result[max(result.keys())]
        expected = {
            "Usain": 90 / 10,
            "Andrei": 90 / 9,
            "Nick": 90 / 3,
        }
        expected_slower = max(expected, key=expected.get)
        TournamentTest.all_results["test_4_time_result"] = slower, expected_slower
        self.assertEqual(slower, expected_slower)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)


if __name__ == "__main__":
    unittest.main()
