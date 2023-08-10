# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:30:44 2023

@author: victo
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    status = []
    for letter in secretWord:
        if not letter in lettersGuessed:
            status.append(False)
        else:
            status.append(True)
    if status == True:
        return True
    else:
        return False

isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])