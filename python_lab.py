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




