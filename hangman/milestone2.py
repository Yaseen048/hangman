import random

word_list = ['mango', 'lychee', 'orange', 'apple', 'strawberry']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("enter a letter\n")
if guess.isalpha() == True and len(guess) == 1:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")
#print(guess)