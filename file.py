hangman_stages = ['''
    +---+
    |   |
    |   0
    |  /|\
    |  / \
    |
=============''','''
    +---+
    |   |
    |   0
    |  /|\
    |  / 
    |
=============''','''
    +---+
    |   |
    |   0
    |  /|\
    |  
    |
=============''','''
    +---+
    |   |
    |   0
    |   |
    |
    |
=============''','''
    +---+
    |   |
    |   0
    |
    |
    |
=============''','''
    +---+
    |   |
    |
    |
    |
    |
=============''','''
    +---+
    |
    |
    |
    |
    |
=============''','''
    +
    |
    | 
    |
    |
    |
=============''','''


    
    
    
    
=============''']


import random
word = ["UDEMY","LOVER"]
secret = random.choice(word)
longity = len(secret)
blank = []
for space in range(longity):
    blank.append("_")
print(" ".join(blank))
guessed = []
lives = 9
end_games = False
while end_games!=True:
    guess = input("Guess a letter : ").upper()
    if guess in guessed:
        print("You have already guessed this letter!")
        continue
    else:
        guessed.append(guess)
    print(guessed)
    
    for position in range(longity):
        letter = secret[position]
        if guess==letter:
            blank[position] = letter
    if guess not in secret:
        lives -=1
    if lives == 0:
        end_games = True
        print("You lose!")
    print(" ".join(blank))
    if "_" not in blank:
        end_games = True
        print("You win!")
