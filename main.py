import random
from Words import common_nouns


# creating a word that will be guessed by the player
def get_word():
    word = random.choice(common_nouns)
    return word.lower()


print(get_word())


# hangman stages that are shown to the player
def hangman_stages(attempts):
    hangman = [
        """
                  _______
                 |       |
                         |
                         |
                         |
                         |
        """,
        """
                   _______
                  |       |
                  O       |
                          |
                          |
                          |
        """,
        """
                   _______
                  |       |
                  O       |
                  |       |
                          |
                          |
        """,
        """
                   _______
                  |       |
                  O       |
                 /|       |
                          |
                          |
        """,
        """
                   _______
                  |       |
                  O       |
                 /|\\      |
                          |
                          |
        """,
        """
                   _______
                  |       |
                  O       |
                 /|\\      |
                 /        |
                          |
        """,
        """
                   _______
                  |       |
                  O       |
                 /|\\      |
                 / \\      |
                          |
                """
               ]
    return hangman[attempts]


print(hangman_stages(6))
