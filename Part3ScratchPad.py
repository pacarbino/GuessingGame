# # f = open('EnglishWords.txt','rt')
# # for i in range (4):
# #     sample = f.read(5)
# #     print(sample)
# # f.close    

# print("=======================================")

# # f = open('EnglishWords.txt','rt')
# # sample = f.readlines(5)#.splitlines()
# # print(sample)
# # f.close    
# # def function():
# #     import random
# #     word = random.choice(open('EnglishWords.txt','rt').read().split())
# #     print(word)
# #     if input("want another?? (y/n):") == "y":
# #         function()
# #     else:
# #         print("been a pleasure!")


# # function()


# import random
# from tkinter import Y
# word = random.choice(open('EnglishWords.txt','rt').read().split()).upper()
# wordArray = list(word)

# print(word)
# print(wordArray)
# def game():
#     print("::plays game::")

# # ask to play again:
# def wannaPlay():
#     playAgain = input("Would you like to play again? (Y/N): ").upper()
#     if playAgain == "Y":
#         game()
#     elif playAgain == "N":
#         print("Well, it has been a pleaseure. Have a great day!")
#     else:
#         print("(Pssssst, you have to guess either 'Y' or 'N')")
#         wannaPlay()
# wannaPlay()

# keep track of used words: (part 4)
usedWords = [] ##okay, now it's updating from game to game. that's good.


def wannaPlay():
    playAgain = input("Would you like to play again? (Y/N): ").upper()
    if playAgain == "Y":
        game()
    elif playAgain == "N":
        print("Well, it has been a pleaseure. Have a great day!")    
    else:
        print("(Pssssst, you have to guess either 'Y' or 'N')")
        wannaPlay()  

def game():    
    
    #### NEEDS WORK!!! should be a function you can call whenever... 
    # random word generator:
    
    import random
    word = random.choice(open('EnglishWords.txt','rt').read().split()).upper()
    wordArray = list(word)

    # keep track of used words: (part 4)
    usedWords.append(word)

    ####TEST!!!!
    print(word)
    print(usedWords)

    # starting number of guesses:
    numGuesses = 7

    # all guessed array:
    guessed = []

    # correctly guessed array:
    correctGuesses = []

    for letter in word:
        correctGuesses.append("_")

    print("""

    ==================================================================
    Hello! We're going to play a little word guessing game!
    I'm going to pick a word, and you're going to try to guess it.
    I'll show you how many letters are in the word, 
    and which letters you've guessed.
    You have 7 chances to guess.
    If you guess wrong, you'll lose one of your guesses.
    To win, you have to guess the word before running out of guesses.
    To quit at any time, press Ctrl+C.
    Seem pretty reasonable? Okay, here we go!!
    ===================================================================

    """)

    while numGuesses > 0 and correctGuesses != wordArray and word not in guessed:
        
        print("You have " + str(numGuesses) + " guesses remaining.") # number of guesses left message
        print("Your word has " + str(len(word)) + " letters.")# remind how many letters are in the word
        print("This is what you've got right so far: " + str(correctGuesses)) # show user progress
        print("""

        ======================================================
        These are the letters or words you've already guessed:
        """ + str(guessed) + """
        ======================================================

        """)

        # get user input
        guess = input("What would you like to guess?: ").upper()
        # check input is letter:
        checkInput = guess.isalpha()

        # check guess:
        if checkInput == False:
            print("""

            ======================================================
            Please guess either a LETTER or a WORD with """ + str(len(word)) + """ letters.
            ======================================================

            """)

        # check if word guessed:
        elif guess == word:
            print("""

            ====================================================================
            Woah! You guessed it! The word was """ + str(word) + """! You win!!!

                                ***Congratulations!!!***

            ====================================================================

            """)
            # ask to play again:
            guessed.append(guess)
            wannaPlay()
        
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
            print("""

                =================================
                Good Guess!! 
                """ + str(guess) + """ is in the word!
                =================================

            """)
            for place in range(len(wordArray)):
                if wordArray[place] == guess:
                    correctGuesses[place] = guess
            guessed.append(guess)
            if correctGuesses == wordArray:
                print("""

                ====================================================================
                Woah! You guessed it! The word was """ + str(word) + """! You win!!!

                                    ***Congratulations!!!***

                ====================================================================

                """)
                # ask to play again:
                wannaPlay()
                
            
        
        # incorrect guess:
        elif guess not in guessed:
            print("""

            ==========================================
            You have guessed """ + str(guess) + """! 
            ...Unfortunately, """ + str(guess) + """ is wrong...
            ==========================================

            """)
            guessed.append(guess)
            numGuesses -= 1
            if numGuesses == 0:
                print("""

                ===================================
                OH NO! You're all out of guesses...
                The word was (drumroll please...)

                        """ + str(word) + """!

                Better luck next time!
                ===================================

                """)

                wannaPlay()
                
game()                