"""EX02 - One Shot Wordle - A step towards Wordle using loops!"""

__author__: str = "730645945"

# Named constants for emoji symbols
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# Initialize variables
index = 0
result = ""

# This is the secret word that can be changed based on user preference.
secret_word = "python"

# This gets the length of the secret word.
word_length = len(secret_word)

guess: str = input(f"What is your {word_length}-letter guess? ")

# Start a while loop to repeatedly ask for guesses until the correct length is provided
if len(guess) != word_length:
    guess = input(f"That was not {word_length} letters! Try again: ")
    while len(guess) != word_length:
        # Check if the length of the guess is equal to the length of the secret word
        guess = input(f"That was not {word_length} letters! Try again: ")

# Loop through each index of the secret word and check against the guessed word
while index < len(secret_word):
    if guess[index] == secret_word[index]:
        result += GREEN_BOX  # Guessed letter is in the correct position
    else:
        i = 0
        while i < len(secret_word):
            if guess[index] == secret_word[i]:
                result += YELLOW_BOX  # Guessed letter is in the word but in the wrong position
                break
            i += 1
        else:
            result += WHITE_BOX  # Guessed letter is not in the correct position
    index += 1

# print the emoji string
print(result)

# Check if guess matches secret word
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")