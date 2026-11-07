# Program 33: First Non-Repeating Character

def first_non_repeating_char(text):
    for char in text:
        if text.lower().count(char.lower()) == 1:
            return char

    return None