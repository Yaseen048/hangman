import random



'''
while True:
    guess = input("pick a letter \n")
    if guess.isalpha() == True and len(guess) == 1:
        if guess in word:
            print("Good guess! {guess} is in the word.")
        else:
            print("Sorry, {guess} is not in the word. Try again.S")

        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
'''

def check_guess(guess):
    guess_lower = guess.lower()
    if guess_lower in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("pick a letter \n")
        if guess.isalpha() == True and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    return guess

word_list = ['mango', 'lychee', 'orange', 'apple', 'strawberry']
print(word_list)

word = random.choice(word_list)
print(word)

guess = ask_for_input()
check_guess(guess)