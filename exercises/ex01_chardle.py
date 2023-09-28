"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730645945"

wordle_word: str = input("Enter a 5-character word: ")


if len(wordle_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

wordle_single: str = input("Enter a single character: ")


if len(wordle_single) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + wordle_single + " in " + wordle_word)

count = 0

if wordle_word[0] == wordle_single:
    count += 1
    print(wordle_single + " found at index 0")   

if wordle_word[1] == wordle_single:
    count += 1
    print(wordle_single + " found at index 1")

if wordle_word[2] == wordle_single:
    count += 1
    print(wordle_single + " found at index 2")

if wordle_word[3] == wordle_single:
    count += 1
    print(wordle_single + " found at index 3")

if wordle_word[4] == wordle_single:
    count += 1
    print(wordle_single + " found at index 4")


if count == 0:
    print("No instances of " + wordle_single + " found in " + wordle_word)
elif count == 1:
    print("1 instance of " + wordle_single + " found in " + wordle_word)
elif count == 2:
    print("2 instances of " + wordle_single + " found in " + wordle_word)
elif count == 3:
    print("3 instances of " + wordle_single + " found in " + wordle_word)
elif count == 4:
    print("4 instances of " + wordle_single + " found in " + wordle_word)
elif count == 5:
    print("5 instances of " + wordle_single + " found in " + wordle_word)