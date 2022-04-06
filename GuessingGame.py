# word variables:
word = "alphabet" # "generate" word
wordArray = ('a','l','p','h','a','b','e','t') # turn word into array (make code later)
wordLen = len(word) #count word length
wordDisp = ("_" * wordLen) # create word display
wordAlert = "Your word has" + str(wordLen) + "letters."
wordDispAlert = "This is what you've got so far: " + str(wordDisp)

# number variables:
numGuesses = 7 # statring number of guesses
numGuessesAlert = "You have " + str(numGuesses) + " guesses remaining." # Number of guesses left message


# guess variables:
guessed = []
correctGuesses = []


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

while numGuesses > 0:
    print(numGuessesAlert) # tell user number of guesses left ******NOT SUBTRACTING from string, but working in code******
    print(wordDispAlert) # show user progress
    print("These are the letters you've already guessed:" + str(guessed))
    guess = input("What letter would you like to guess?: ") # get user input
    
    # check guess:
    if type(guess) != str:
        print("""
        =============================
        Please guess a LETTER or Word
        =============================
        """)

    
    # repeat guess:
    elif guess in guessed:
        print("""
        ====================================================
        Hmmmm, looks like you've guessed that one already... 
        Try again!
        ====================================================
        """)
    
    # repat guess:
    elif guess in wordArray:
        print(str("""
        =================================
        Good Guess!! 
        """ + guess + """ is in the word!
        =================================
        """))
        guessed.append(guess)
        correctGuesses.append(guess)
    
    # new guess:
    elif guess not in guessed:
        print(str("""
        ==========================================
        You have guessed """ + guess + """! 
        ...Unfortunately, """ + guess + """ is not 
        part of the word.
        ==========================================
        """))
        guessed.append(guess)
        numGuesses = numGuesses - 1

print("""OH NO! You're all out of guesses... 
Better luck next time!

""")