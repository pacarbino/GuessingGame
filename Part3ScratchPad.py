# f = open('EnglishWords.txt','rt')
# for i in range (4):
#     sample = f.read(5)
#     print(sample)
# f.close    

# print("=======================================")

# f = open('EnglishWords.txt','rt')
# sample = f.readlines(5)#.splitlines()
# print(sample)
# f.close    

from tkinter import Y


guess = input("What would you like to guess?: ") # get user input



# check guess:
#if guess.isaplha() == False:  # *******DOES NOT WORK*****
print(guess.isalpha())