# ex 6: Is Even
def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False
    return None


# ex 7: Integer Sign Determination
def determine_sign(num: int) -> str:
    if num == 0:
        return "zero"
    elif num > 0:
        return "positive"
    else:
        return "negative"


# ex 8: Find Remainder
def find_remainder(dividend: int, divisor: int) -> int:
    remainder = dividend % divisor
    return remainder


# ex 10: Backward String
def backward_string(val: str) -> str:
    return val[::-1]


# ex 11: Just Fizz!
def checkio(num: int) -> str:
    if num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


# ex 12: First Word (simplified)
def first_word(text: str) -> str:
    word = text.split(' ')
    return word[0]


# ex 13: Number Length
def number_length(value: int) -> int:
    value1 = str(value)
    return len(value1)


# ex 14: Fizz Buzz
def checkio(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
