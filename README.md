# Hangman Game

A Python-based Hangman game where the player attempts to guess a randomly selected word one letter at a time. The program displays the hidden word using underscores and gradually reveals the letters when correct guesses are made. Incorrect guesses reduce the player's remaining lives and update the Hangman ASCII-art stages. The game also keeps track of previously guessed letters to prevent duplicate guesses and allows the player to start a new round after winning or losing.

## Features

* Randomly selects a word from a predefined word list.
* Displays the hidden word using underscores.
* Allows the player to guess one letter at a time.
* Reveals correctly guessed letters in their positions.
* Tracks previously guessed letters and prevents duplicate guesses.
* Gives the player **9 lives**.
* Displays different Hangman stages based on remaining lives.
* Detects both winning and losing conditions.
* Allows the player to start another round without restarting the program.

## How to Run

1. Make sure Python 3 is installed.
2. Run the script:

   ```bash
   python hangman.py
   ```
3. Enter one letter at a time when prompted.
4. Continue guessing until you reveal the entire word or run out of lives.
5. Choose whether to play another round after the game ends.

## Example

```text
_ _ _ _ _ _ _

Guess a letter : A
['A']
_ A _ _ _ _ _
        +---+
        |   |
        |
        |
        |
        |
    =============

Guess a letter : E
['A', 'E']
_ A _ _ _ E _

Guess a letter : Z
['A', 'E', 'Z']
You lose!

Thanks for playing, see you in the next round..
```

## Concepts Practiced

* `random.choice()`
* Lists
* `for` loops
* `while` loops
* Conditional statements
* String indexing
* String comparison
* List manipulation
* Game-state management
* ASCII art

## Language

* Python 3
