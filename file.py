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
guessed = []
lives = 6
end_games = False
while end_games!=True:
    guess = input("Guess a letter : ").upper()
    if guess in guessed:
        print("You have already guessed this letter!")
    else:
        guessed.append(guess)
    for position in range(longity):
        letter = secret[position]
        if guess==letter:
            blank[position] = letter
    if guess not in secret_word:
        lives -=1
    if lives == 0:
        end_game = True
        print("You lose!")
    print(blank)
    if "_" not in blank:
        end_game = True
        print("You win!")
