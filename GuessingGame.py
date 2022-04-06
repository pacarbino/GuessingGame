# word variables
word = "alphabet" # "generate" word
wordArray = ['a','l','p','h','a','b','e','t'] # turn word into array (make code later)
wordLen = len(word) #count word length
wordDisp = ("_" * wordLen) # create word display
wordAlert = "Your word has" + str(wordLen) + "letters."
wordDispAlert = "This is what you've got so far: " + str(wordDisp)

# number variables
numGuesses = 7 # statring number of guesses
numGuessesAlert = "You have " + str(numGuesses) + " guesses remaining." # Number of guesses left message

# displays

guessed = []
print(guessed)

while numGuesses > 0:
    print(numGuessesAlert) # tell user number of guesses left
    print(wordDispAlert) # show user progress
    print("These are the letters you've already guessed:" + str(guessed))
    guess = input("What letter would you like to guess?: ") # get user input
        if guess in guessed = True:
            
    print(str("You have guessed " + guess + "!"))#test
    guessed.append(guess)
    print(str(guessed))#test 
    numGuesses += 1

guessed = []