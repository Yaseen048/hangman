import random

class Hangman:

    def __init__(self, word_list, num_lives=5):

        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.num_letters = len(set(self.word))
        self.word_guessed = ['_'] * len(self.word)
        self.list_of_guesses = []


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