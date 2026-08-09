from functions import count_vowels, is_positive


def test_positive_number():
    assert is_positive(4)


def test_negative_and_zero_are_not_positive():
    assert not is_positive(-1)
    assert not is_positive(0)


def test_vowel_count_is_case_insensitive():
    assert count_vowels("Education") == 5


def test_vowel_count_for_empty_and_consonants():
    assert count_vowels("") == 0
    assert count_vowels("rhythm") == 0
