#exercise 1 Variable: Declaration and Value Setting
a = 2
b = 5
a, b = 2, 5
a: int = 2
b: int = 5

#ex 2 Variables with Expression Values
add=a+b
multi=a*b


def func():
    pass
def func():
    return None

#ex 3 Take and Return Argument
def func(arg):
    return arg



print("Example:")
print(func(3))

# These "asserts" are used for self-checking
assert func(3) == 3
assert func("string") == "string"
assert func(True) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

#ex 4 Multiply (Intro)
def mult_two(a: int, b: int) -> int:
    multi=a*b
    return multi


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")


#ex 5 Rectangle Perimeter
def rectangle_perimeter(length: int, width: int) -> int:
    p=2*length+2*width
    
    return p


print("Example:")
print(rectangle_perimeter(3, 2))

# These "asserts" are used for self-checking
assert rectangle_perimeter(2, 4) == 12
assert rectangle_perimeter(3, 5) == 16
assert rectangle_perimeter(10, 20) == 60
assert rectangle_perimeter(7, 2) == 18
assert rectangle_perimeter(1, 1) == 4
assert rectangle_perimeter(1, 5) == 12
assert rectangle_perimeter(4, 1) == 10
assert rectangle_perimeter(100, 100) == 400
assert rectangle_perimeter(0.5, 2) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")

#ex:6 Is Even
def is_even(num: int) -> bool:
    if num%2==0:
        return True
    else:
        return False
    return None


print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

#ex:7 Integer Sign Determination

def determine_sign(num: int) -> str:
    if num==0:
        return "zero"
    elif num>0:
        return "positive"
    else:
        return "negative"
    return ""


print("Example:")
print(determine_sign(11))

# These "asserts" are used for self-checking
assert determine_sign(5) == "positive"
assert determine_sign(0) == "zero"
assert determine_sign(-10) == "negative"
assert determine_sign(1) == "positive"
assert determine_sign(-1) == "negative"
assert determine_sign(999) == "positive"
assert determine_sign(-1000) == "negative"
assert determine_sign(123456789) == "positive"
assert determine_sign(-987654321) == "negative"
assert determine_sign(2) == "positive"

print("The mission is done! Click 'Check Solution' to earn rewards!")


#ex 8 Find Remainder

def find_remainder(dividend: int, divisor: int) -> int:
    remainder=dividend % divisor
    return remainder


print("Example:")
print(find_remainder(3, 2))

# These "asserts" are used for self-checking
assert find_remainder(10, 3) == 1
assert find_remainder(14, 4) == 2
assert find_remainder(27, 4) == 3
assert find_remainder(10, 5) == 0
assert find_remainder(10, 1) == 0
assert find_remainder(5, 7) == 5
assert find_remainder(7, 5) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")

#ex 10 Backward String
def backward_string(val: str) -> str:
    return val[::-1]  


print("Example:")
print(backward_string("val")) 

assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")

#ex 11 Just Fizz!
def checkio(num: int) -> str:
    if num % 3==0:
        return "Fizz"
    else:
        return str(num)


print("Example:")
print(checkio(3))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz"
assert checkio(6) == "Fizz"
assert checkio(10) == "10"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")

#ex 12 First Word (simplified)

def first_word(text: str) -> str:
   word=text.split(' ')
   return word[0]
     
print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")


#ex 13 Number Length

def number_length(value: int) -> int:
    value1=str(value)
    return len(value1)


print("Example:")
print(number_length(10))

# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")


#ex14 Fizz Buzz
# Taken from mission Just Fizz!

def checkio(num: int) -> str:
    if num%3==0 and num%5==0:
        return "Fizz Buzz"
    elif num % 3==0:
        return "Fizz"
    elif num %5==0:
        return "Buzz"
    
    else:
        return str(num)


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")


