# f = open('EnglishWords.txt','rt')
# for i in range (4):
#     sample = f.read(5)
#     print(sample)
# f.close    

print("=======================================")

# f = open('EnglishWords.txt','rt')
# sample = f.readlines(5)#.splitlines()
# print(sample)
# f.close    
# def function():
#     import random
#     word = random.choice(open('EnglishWords.txt','rt').read().split())
#     print(word)
#     if input("want another?? (y/n):") == "y":
#         function()
#     else:
#         print("been a pleasure!")


# function()


import random
word = random.choice(open('EnglishWords.txt','rt').read().split()).upper()
wordArray = list(word)

print(word)
print(wordArray)