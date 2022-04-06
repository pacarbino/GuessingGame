# word variables
word = "alphabet" # "generate" word
wordLen = len(word)
wordDisp = ("_" * wordLen) # create word display
wordAlert = "Your word has" + str(wordLen) + "letters."
wordDispAlert = "This is what you've got so far: " + str(wordDisp)

# number variables
numGuesses = 7 # statring number of guesses
numGuessesAlert = "You have " + str(numGuesses) + " left." # Number of guesses left message

print(numGuessesAlert) # test print

print(wordDispAlert) # test print

