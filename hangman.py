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
word = ["Absolute", "Building", "Creative", "Dynamite", "Elephant", "Balance", 
        "Curious", "Journey", "Pioneer", "Vibrant", "Canvas", "Design", "Energy", "Moment", 
        "Wisdom", "Brave", "Focus", "Light", "Peace", "Voice","Adventure", "Brilliant", "Discovery", 
        "Freedom", "Harmony", "Invention", "Jubilant", "Knowledge", "Labyrinth", "Mountain", "Navigator", 
        "Optimism", "Pinnacle", "Resilient", "Starlight", "Triumph", "Universe", "Valiant", "Whisper", 
        "Zenith", "Breeze", "Canyon", "Dolphin", "Emerald", "Falcon", "Glacier", "Horizon", "Island", "Jungle", 
        "Kettle", "Lagoon", "Meadow", "Nebula", "Oasis", "Planet", "Quartz", "River", "Summit", "Thunder", "Valley"]
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
    print(hangman_stages[lives])
    if "_" not in blank:
        end_games = True
        print("You win!")
    if end_games:
        ask = input("Do you want to play again? (Y/N)")
        if ask == "Y":
            secret = random.choice(word)
            blank.clear()
            longity = len(secret)
            for space in range(longity):
                blank.append("_")
            end_games = False
            guessed.clear()
            lives = 9
        else:
            print("Thanks for playing, see you in the next round..")

