# Problem 1
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0

    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES:
            score += SCRABBLE_LETTER_VALUES[letter]
        else:
            score = 0
    
    score *= len(word)

    if len(word) == n:
        score += 50
    
    return score

# Problem 2

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    
    for x in word:
        new_hand[x] = new_hand.get(x) - 1

    return new_hand

# Problem 3

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if not word in wordList:
        return False
    
    copy = hand.copy()
    
    for x in word:
        if x not in copy:
            return False
        if copy[x] > 0:
            copy[x] = copy.get(x) - 1
        else:
            return False
    
    return True

# Problem 4

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    count = 0
    
    for key in hand:
        count += hand[key]
        
    return count

# Problem 5

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
        # As long as there are still letters left in the hand:
    score = 0
    total_score = 0
    
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        print("Current Hand: ", end="")
        displayHand(hand)
        
        # Ask user for input
        word = input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if word == ".":
                    
            # End the game (break out of the loop)
            break

            
        # Otherwise (the input is not a single period):
        else:
        
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):            
                        
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print("")

            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(word, n)
                total_score += score
                print('"%s" earned %i points. Total: %i points' % (word, score, total_score))
                print("")
                
                # Update the hand
                hand = updateHand(hand, word)
                
                
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print("Goodbye! Total score: %i points." % total_score)

# Problem 6

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    hand = {}
    action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
    
    while action != "e":    
        while action == "r" and not hand:
            print("You have not played a hand yet. Please play a new hand first!")
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
        
        while action == "n":
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
        
        while action == "r":
            playHand(hand, wordList, HAND_SIZE)
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
            
        while action not in ["e", "r", "n"]:
            print("Invalid command")
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")

# Problem 6

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    hand = {}
    action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
    
    while action != "e":    
        while action == "r" and not hand:
            print("You have not played a hand yet. Please play a new hand first!")
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
        
        while action == "n":
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
        
        while action == "r":
            playHand(hand, wordList, HAND_SIZE)
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
            
        while action not in ["e", "r", "n"]:
            print("Invalid command")
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")

# Problem 7

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {}
    action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
     
    while action != "e":    
        while action == "r" and not hand:
            print("You have not played a hand yet. Please play a new hand first!")
            print("")
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
            
        while action == "n":
            action_2 = input("Enter u to have yourself play, c to have the computer play: ")
            print("")
            if action_2 == "u":
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
                action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
            elif action_2 == "c":
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)
                action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
            else:
                print("Invalid command")
        
        while action == "r":
            action_2 = input("Enter u to have yourself play, c to have the computer play: ")
            print("")
            if action_2 == "u":
                playHand(hand, wordList, HAND_SIZE)
                action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
            elif action_2 == "c":
                compPlayHand(hand, wordList, HAND_SIZE)
                action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
            else:
                print("Invalid input")
        
        while action not in ["e", "r", "n"]:
            print("Invalid command")
            print("")
            action = input("Enter n to deal new hand, r to replay the last hand, or e to end game: ")
        
