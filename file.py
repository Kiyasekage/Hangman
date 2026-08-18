#first three sequence
print(f"    +{"-"*3}+")
print(f"{"    |\n"*3}    |")
print("="*10)
#program

import random
word = ["UDEMY","LOVER"]
secret = random.choice(word)
longity = len(secret)
blank = []
for space in range(longity):
    blank.append("_")
print(blank)
