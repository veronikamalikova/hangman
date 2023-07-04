class HangmanStages:
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

    def get_stage(self, errors):
        if errors < 0 or errors >= len(self.hangman):
            raise ValueError("Value Error")
        return self.hangman[errors]