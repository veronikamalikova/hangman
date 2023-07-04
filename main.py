from Word import Word
from HangmanStages import HangmanStages


LIVES = 6


def print_lives(errors):
    print("Lives remaining: " + str(LIVES - errors) + ".")


word = Word().get_random_word()
guessed = []
errors = 0

print("Guess the word! It has " + str(len(word)) + " letters: " + Word().get_hidden_word(word, guessed))
print_lives(errors)

while errors < LIVES:
    letter = input("Enter a character: ")
    if Word().is_letter_in_word(letter, word):
        guessed.append(letter)

        if Word().is_winner(word, guessed):
            print("Wow! You've guessed it and won!")
            break

        print(Word().get_hidden_word(word, guessed))
    else:
        guessed.append(letter)
        errors += 1
        print(HangmanStages().get_stage(errors))
        print("Oops, that was wrong! You've just lost 1 life.")
        print_lives(errors)
        print(Word().get_hidden_word(word, guessed))

if errors >= LIVES:
    print(HangmanStages().get_stage(6))
    print("The correct word was: " + word + "!")
    print("GAME OVER - Try again?!")