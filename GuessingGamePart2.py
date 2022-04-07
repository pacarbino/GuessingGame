# word variables:
word = "alphabet" # "generate" word ***FIX LATER***
wordArray = list(word)

# number variables:
numGuesses = 7 # statring number of guesses


# guess variables:
guessed = []
correctGuesses = []

#print(wordArray) # TEST
for letter in word:
    correctGuesses.append("_")

print("""



Hello! We're going to play a little word guessing game!
I'm going to pick a word, and you're going to try to guess it.
I'll show you how many letters are in the word, 
and which letters you've guessed.
You have 7 chances to guess.
If you guess wrong, you'll lose one of your guesses.
To win, you have to guess the word before running out of guesses.
To quit at any time, press Ctrl+C.
Seem pretty reasonable? Okay, here we go!!



""")
while numGuesses > 0 and correctGuesses != wordArray and word not in guessed:
    
    print("You have " + str(numGuesses) + " guesses remaining.") # number of guesses left message
    print("Your word has " + str(len(word)) + " letters.")# remind how many letters are in the word
    print("This is what you've got right so far: " + str(correctGuesses)) # show user progress
    print("""
    =============================================
    These are the letters or words you've already guessed:
    """ + str(guessed) + """
    =============================================
    """)
    guess = input("What would you like to guess?: ") # get user input
    checkInput = guess.isalpha()

     # check guess:
    if checkInput == False:
        print("""

        =============================
        Please guess a LETTER or WORD
        =============================

        """)

    # check if word guessed:
    elif guess == word:
        print("""

        =================================================
        Woah! You guessed it! You win!!!
        =================================================

        """)
        guessed.append(guess)
    
    # repeat guess:
    elif guess in guessed:
        print("""

        ====================================================
        Hmmmm, looks like you've guessed that one already... 
        Try again!
        ====================================================

        """)
    
    # correct guess:
    elif guess in wordArray:
        print(str("""

        =================================
        Good Guess!! 
        """ + guess + """ is in the word!
        =================================

        """))
        for place in range(len(wordArray)):
            if wordArray[place] == guess:
                correctGuesses[place] = guess
        guessed.append(guess)
        if correctGuesses == wordArray:
            print("""

            ===================================
            ***Congratulations!!! You win!!!***
            
            The word was """ + str(word) + """!
            ===================================
            
            """)
        
    
    # incorrect guess:
    elif guess not in guessed:
        print(str("""

        ==========================================
        You have guessed """ + guess + """! 
        ...Unfortunately, """ + guess + """ is not 
        part of the word.
        ==========================================

        """))
        guessed.append(guess)
        numGuesses -= 1
        if numGuesses == 0:
            print("""

            ===================================
            OH NO! You're all out of guesses...
            The word was (drumroll please...)

            """ + word + """!

            Better luck next time!
            ===================================

            """)