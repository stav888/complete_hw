def is_positive(number):
    return number > 0


def count_vowels(text):
    return sum(character.lower() in "aeiou" for character in text)
