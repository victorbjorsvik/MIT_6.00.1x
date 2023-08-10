# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# The Guessing Game:

print("Please think of a number between 0 and 100!")

print("Is your secret number 50?")

low = 0
guess = 50
high = 100
response = ""

while response != 'c':
    resonse = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response == 'h':
        print(f"Is your secret number {(guess + high)/2}?")
        guess = (guess + high)/2
    else:
        print(f"Is your secret number {(guess + low)/2}?")
    
        