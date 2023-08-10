# =============================================================================
# HANGMAN
# =============================================================================

import random
import string


WORDLIST_FILENAME = r"C:\Users\victo\OneDrive\Dokumenter\MIT\Hangman\words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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
    
    if not False in status:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    status = ""
    for letter in secretWord:
        if not letter in lettersGuessed:
            status = status + (" _ ")
        else:
            status = status + letter
    
    return status



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    letters = string.ascii_lowercase
    copy = ""
    
    for letter in letters:
        if not letter in lettersGuessed:
            copy = copy + letter
    
    return copy


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = ['']
    mistakesMade = 0
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %i letters long." % len(secretWord))
    guesses = 8
    
    while guesses > 0:

        availableLetters = getAvailableLetters(lettersGuessed)
    
        print("-"*50)
        
        print("You have %i guesses left." % guesses)
        print("Available letters: %s" % availableLetters)
        guess = input("Please guess a letter: ")
        while guess in lettersGuessed:
            print("Oops! You've already guessed that letter: %s" % (getGuessedWord(secretWord, lettersGuessed)))        
            print("-"*50)
            print("You have %i guesses left." % guesses)
            print("Available letters: %s" % availableLetters)
            guess = input("Please guess a letter: ")

        while guess not in string.ascii_lowercase:
            print("Oops! Please insert a lowercase letter: %s" % (getGuessedWord(secretWord, lettersGuessed)))
            print("-"*50)
            print("You have %i guesses left." % guesses)
            print("Available letters: %s" % availableLetters)         
            guess = input("Please guess a letter: ")
        
        lettersGuessed.append(guess)
        
        if guess in secretWord:
            print("Good guess: %s" % (getGuessedWord(secretWord, lettersGuessed)))
        else:
            mistakesMade += 1
            guesses -= 1
            print("Oops! That letter is not in my word: %s" % (getGuessedWord(secretWord, lettersGuessed)))
        
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("-"*50)
            print("Congratulations, you won!")
            return
    print("-"*50)
    print("Sorry, you ran out of guesses. The word was %s" % secretWord)

# =============================================================================
# run the program
# =============================================================================

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)