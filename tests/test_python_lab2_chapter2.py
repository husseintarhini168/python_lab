from checkio.python_lab2_chapter2 import(
    is_even, 
    determine_sign, 
    find_remainder, 
    backward_string, 
    checkio, 
    first_word, 
    number_length
)

# Test for ex: 6 Is Even
def test_is_even_2():
    assert is_even(2) == True

def test_is_even_5():
    assert is_even(5) == False

def test_is_even_0():
    assert is_even(0) == True


# Test for ex: 7 Integer Sign Determination
def test_determine_sign_positive():
    assert determine_sign(5) == "positive"

def test_determine_sign_zero():
    assert determine_sign(0) == "zero"

def test_determine_sign_negative():
    assert determine_sign(-10) == "negative"

def test_determine_sign_positive_1():
    assert determine_sign(1) == "positive"

def test_determine_sign_negative_1():
    assert determine_sign(-1) == "negative"

def test_determine_sign_positive_large():
    assert determine_sign(999) == "positive"

def test_determine_sign_negative_large():
    assert determine_sign(-1000) == "negative"

def test_determine_sign_positive_very_large():
    assert determine_sign(123456789) == "positive"

def test_determine_sign_negative_very_large():
    assert determine_sign(-987654321) == "negative"

def test_determine_sign_positive_2():
    assert determine_sign(2) == "positive"


# Test for ex: 8 Find Remainder
def test_find_remainder_10_3():
    assert find_remainder(10, 3) == 1

def test_find_remainder_14_4():
    assert find_remainder(14, 4) == 2

def test_find_remainder_27_4():
    assert find_remainder(27, 4) == 3

def test_find_remainder_10_5():
    assert find_remainder(10, 5) == 0

def test_find_remainder_10_1():
    assert find_remainder(10, 1) == 0

def test_find_remainder_5_7():
    assert find_remainder(5, 7) == 5

def test_find_remainder_7_5():
    assert find_remainder(7, 5) == 2


# Test for ex: 10 Backward String
def test_backward_string_val():
    assert backward_string("val") == "lav"

def test_backward_string_empty():
    assert backward_string("") == ""

def test_backward_string_ohho():
    assert backward_string("ohho") == "ohho"

def test_backward_string_numbers():
    assert backward_string("123456789") == "987654321"


# Test for ex: 11 Just Fizz!
def test_checkio_fizz_15():
    assert checkio(15) == "Fizz Buzz"

def test_checkio_fizz_6():
    assert checkio(6) == "Fizz"

def test_checkio_fizz_10():
    assert checkio(10) == "Buzz"

def test_checkio_fizz_7():
    assert checkio(7) == "7"


# Test for ex: 12 First Word
def test_first_word_hello_world():
    assert first_word("Hello world") == "Hello"

def test_first_word_a_word():
    assert first_word("a word") == "a"

def test_first_word_greeting():
    assert first_word("greeting from CheckiO Planet") == "greeting"

def test_first_word_hi():
    assert first_word("hi") == "hi"


# Test for ex: 13 Number Length
def test_number_length_10():
    assert number_length(10) == 2

def test_number_length_0():
    assert number_length(0) == 1

def test_number_length_4():
    assert number_length(4) == 1

def test_number_length_44():
    assert number_length(44) == 2


# Test for ex: 14 Fizz Buzz
def test_checkio_fizz_buzz_15():
    assert checkio(15) == "Fizz Buzz"

def test_checkio_fizz_buzz_6():
    assert checkio(6) == "Fizz"

def test_checkio_fizz_buzz_10():
    assert checkio(10) == "Buzz"

def test_checkio_fizz_buzz_7():
    assert checkio(7) == "7"
