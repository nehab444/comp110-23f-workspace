"""EX03 - Six Try Wordle - Enables six try function!"""

__author__: str = "730645945"


def contains_char(prime_string: str, char_search: str) -> bool:
    """Check if a single character of a second string is found at any index of a first string.

    Args:
    prime_string (str): A string that is being searched through for the second parameter.
    char_search (str): A string that is expected to be a single character in length and is the character being searched for.

    Returns:
    bool: True if the character is found, False otherwise.
    """
    assert len(char_search) == 1

    index = 0
    while index < len(prime_string):
        if prime_string[index] == char_search:
            return True
        index += 1

    return False


def emojified(user_guess: str, user_secret: str) -> str:
    """Given two strings of equal length, the first a guess, and the second a secret, it will return a string of emoji.

    Args:
    - user_guess- this is what the user guesses
    - user_secret- this is the secret word trying to be figured out

    Returns:
    str: Returns user guess as string
    """
    assert len(user_guess) == len(user_secret)

    result = ""
    index = 0
    while index < len(user_guess):
        if user_guess[index] == user_secret[index]:
            # Append green emoji box
            result += "\U0001F7E9"
        else:
            char = user_guess[index]
            if contains_char(user_secret, char):
                # Append yellow emoji box
                result += "\U0001F7E8"
            else:
                # Append white emoji box
                result += "\U00002B1C"
        index += 1

    return result


def input_guess(expected_length: int) -> str:
    """Its purpose is given an integer “expected length” of a guess as a parameter, it will prompt the user for a guess and continue prompting them until they provide a guess of the expected length.

    Parameter
    - expected_length
    """
    user_guess = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word = "codes"  # Replace with the actual secret word

    # Initialize game variables
    turns = 0
    max_turns = 6
    while turns < max_turns:
        turns += 1
        print(f"\n=== Turn {turns}/{max_turns} ===")
        
        # Prompt the user for a guess
        user_guess = input_guess(len(secret_word))
        
        # Codify the emoji results of the user's guess versus the secret
        emoji_result = emojified(user_guess, secret_word)
        print(emoji_result)
        
        # Check if the user's guess is correct
        if user_guess == secret_word:
            print(f"\nYou won in {turns}/{max_turns} turns!")
            return
    
    print(f"\n X/{max_turns} - Sorry, try again tomorrow!")
    return
 

if __name__ == "__main__":
    main()
