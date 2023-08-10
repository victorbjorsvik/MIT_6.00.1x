# Problem 1
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
    
# Problem 2

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

# Problem 3

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string

    letters = string.ascii_lowercase
    copy = ""

    for letter in letters:
        if not letter in lettersGuessed:
            copy = copy + letter
            
    return copy

# Problem 4
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
    
        print("--------------")
        
        print("You have %i guesses left." % guesses)
        print("Available letters: %s" % availableLetters)
        guess = input("Please guess a letter: ")
        while guess in lettersGuessed:
            print("Oops! You've already guessed that letter: %s" % (getGuessedWord(secretWord, lettersGuessed)))        
            print("--------------")
            print("You have %i guesses left." % guesses)
            print("Available letters: %s" % availableLetters)
            guess = input("Please guess a letter: ")

        while guess not in string.ascii_lowercase:
            print("Oops! Please insert a lowercase letter: %s" % (getGuessedWord(secretWord, lettersGuessed)))
            print("--------------")
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
            print("---------------")
            print("Congratulations, you won!")
            return
    print("--------------")
    print("Sorry, you ran out of guesses. The word was %s" % secretWord)

hangman()