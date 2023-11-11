import random

class Hangman:

    def __init__(self, word_list, num_lives=5):

        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.num_letters = len(set(self.word))
        self.word_guessed = ['_'] * len(self.word)
        self.list_of_guesses = []

    def check_guess(self, guess):
        lower_case_guess = guess.lower()
        if lower_case_guess in word:
            print(f"Good guess! {guess} is in the word.")

        pass

    def ask_for_input(self):
        while True:
            guess = input("pick a letter \n")
            if guess.isalpha() == False and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
                self.list_of_guesses.append(guess)
            print("Invalid letter. Please, enter a single alphabetical character.")


# Printing attributes
'''
word_list = ['mango', 'lychee', 'orange', 'apple', 'strawberry']
hangman = Hangman(word_list)
print(hangman.word_list)
print(hangman.word)
print(hangman.num_letters)
print(hangman.word_guessed)
print(hangman.num_lives)
print(hangman.list_of_guesses)
'''