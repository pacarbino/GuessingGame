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

import random
word = random.choice(open('EnglishWords.txt','rt').read().split())
print(word)