# Program 32: Check Anagram Strings

def is_anagram(str1, str2):

    # Convert strings into lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove spaces
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Compare sorted strings
    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    print(is_anagram(str1, str2))