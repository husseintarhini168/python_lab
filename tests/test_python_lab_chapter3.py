from checkio.python_lab_chapter3 import count_vowels, sum_upto_n


# Tests for count_vowels function
def test_count_vowels_hello():
    assert count_vowels("hello") == 2


def test_count_vowels_openai():
    assert count_vowels("openai") == 4


def test_count_vowels_typescript():
    assert count_vowels("typescript") == 2


def test_count_vowels_single_a():
    assert count_vowels("a") == 1


def test_count_vowels_single_b():
    assert count_vowels("b") == 0


def test_count_vowels_all_vowels_lowercase():
    assert count_vowels("aeiou") == 5


def test_count_vowels_all_vowels_uppercase():
    assert count_vowels("AEIOU") == 5


def test_count_vowels_sentence_fox():
    assert count_vowels("The quick brown fox") == 5


def test_count_vowels_sentence_dog():
    assert count_vowels("Jumps over the lazy dog") == 6


def test_count_vowels_empty_string():
    assert count_vowels("") == 0


# Tests for sum_upto_n function
def test_sum_upto_1():
    assert sum_upto_n(1) == 1


def test_sum_upto_2():
    assert sum_upto_n(2) == 3


def test_sum_upto_3():
    assert sum_upto_n(3) == 6


def test_sum_upto_4():
    assert sum_upto_n(4) == 10


def test_sum_upto_5():
    assert sum_upto_n(5) == 15


def test_sum_upto_10():
    assert sum_upto_n(10) == 55


def test_sum_upto_20():
    assert sum_upto_n(20) == 210


def test_sum_upto_100():
    assert sum_upto_n(100) == 5050


def test_sum_upto_200():
    assert sum_upto_n(200) == 20100


def test_sum_upto_500():
    assert sum_upto_n(500) == 125250
