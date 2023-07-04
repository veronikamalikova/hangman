import unittest
from Word import Word


class WordTest(unittest.TestCase):
    def test_get_random_word(self):
        word = Word().get_random_word()
        self.assertLessEqual(3, len(word))

    def test_is_letter_in_word(self):
        self.assertEqual(False, Word().is_letter_in_word("s", "time"))
        self.assertEqual(True, Word().is_letter_in_word("i", "time"))

    def test_get_hidden_word(self):
        self.assertEqual("_ _ _", Word().get_hidden_word("air", []))
        self.assertEqual("_ i _", Word().get_hidden_word("air", ["i"]))

    def test_is_winner(self):
        self.assertFalse(Word().is_winner("air", ["a"]))
        self.assertTrue(Word().is_winner("air", ["a", "i", "r"]))
        self.assertTrue(Word().is_winner("air", ["a", "i", "r", "d"]))


if __name__ == '__main__':
    unittest.main()
