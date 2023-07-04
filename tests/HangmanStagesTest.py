import unittest
from HangmanStages import HangmanStages


class HangmanStagesTest(unittest.TestCase):
    def test_get_stage(self):
        self.assertEqual(
        """
                   _______
                  |       |
                  O       |
                 /|\\      |
                 / \\      |
                          |
        """,
        HangmanStages().get_stage(6))

    def test_get_stage_value_error(self):
        self.assertRaises(ValueError, HangmanStages().get_stage, -1)
        self.assertRaises(ValueError, HangmanStages().get_stage, 7)