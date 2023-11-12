# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Purpose/Aim of project
This aim of this project is to help me practise my python programming skills

## Installation
No installations or external modules are required to be installed.

## Structure of Project
In this project there are five python files. The first three python files milestone2,3,4 are used to practise different aspects of code. The milestone5 file is the final hangman python file. The hangman_template file is a template.

Milestone2 contains code that displays the very basics of hangman. Having a word to be guessed, taking an input from the user and finally comapring it to the word.

Milestone3 extends milestone2 through the use of functions and a while loop. In this file we create a function for asking the user for a letter and a function to check if thier letter is in the word to be guessed. The while loop is added to keep asking for a valid input  (only one letter) if the user keeps entering a invalid input(e.g numbers, multiple letter, punctuation).

Milestone4 focuses on object oriented programming. A hangman class is made with attributes containing the same variables in milestone2 and 3 such as guess and word. There are also additional attributes which reprsesnts number of lives and list of guessed letters. Methods for asking the user for input and checking their guess are also defined

Milestone5 combines all the things practised in the other milestone python files and also uses the the hangman_template as a template.