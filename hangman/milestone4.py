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
        lower_case_guess = guess.lower()#turning guess into lowercase
        if lower_case_guess in self.word:
            print(f"Good guess! {lower_case_guess} is in the word.")
            for letter in self.word:
                #replacing undercore with correct letter
                if guess == letter:
                    letter_index = self.word.index(letter)
                    self.word_guessed[letter_index] = guess
            self.num_letters -= 1
        else:#if incorrect letter guess, number of lives reduces by 1
            self.num_lives -= 1
            print(f"Sorry, {lower_case_guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")



    def ask_for_input(self):
        while True:
            guess = input("pick a letter \n")
            if guess.isalpha() == False or len(guess) != 1:#checks for valid input
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:#if user has repeated guess
                print("You already tried that letter!")
            else:
                self.check_guess(guess)#for new guess
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)
            
            if self.num_letters == 0:
                break
            



# Printing attributes
'''

print(hangman.word_list)
print(hangman.word)
print(hangman.num_letters)
print(hangman.word_guessed)
print(hangman.num_lives)
print(hangman.list_of_guesses)
'''
word_list = ['mango', 'lychee', 'orange', 'apple', 'strawberry']
hangman = Hangman(word_list)
hangman.ask_for_input()

