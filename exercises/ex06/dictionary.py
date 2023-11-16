"""Working with dictionaries!"""

__author__ = "730645945"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary.

    Arguments:
        input_dict (dict[str, str]): A dictionary to be inverted.

    Returns:
        dict[str, str]: An inverted dictionary.
    """
    inverted_dict: dict[str, str] = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate value in input dictionary")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Finds the most frequently appearing color in a dictionary.

    Arguments:
        color_dict (dict[str, str]): A dictionary of names and favorite colors.

    Returns:
        str: The most popular color.
    """
    color_count: dict[str, int] = {}
    max_count = 0
    favorite_color: str = " "

    for color in color_dict.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

        if color_count[color] > max_count:
            max_count = color_count[color]
            favorite_color = color

    return favorite_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequency of values in a list.

    Arguments:
        input_list (list[str]): A list of values to count.

    Returns:
        dict[str, int]: A dictionary of the counts of each value in the list.
    """
    result_dict: dict[str, int] = {}
    for item in input_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Categorizes words in a list by the first letter.

    Arguments:
        word_list (list[str]): A list of words to categorize.

    Returns:
        dict[str, list[str]]: A dictionary of letters and lists of words that start with each letter.
    """
    alphabet_dict: dict[str, list[str]] = {}
    for word in word_list:
        first_letter = word[0].lower()
        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(word)
        else:
            alphabet_dict[first_letter] = [word]
    return alphabet_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendance records for a specific day.

    Arguments:
        attendance_dict (dict[str, list[str]): A dictionary of days and lists of attending students.
        day (str): The day of the week to update.
        student (str): The name of the student who attended.

    Returns:
        dict[str, list[str]]: The updated attendance dictionary.
    """
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict
