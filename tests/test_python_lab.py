from checkio import python_lab

# Tests for the func function
def test_func_with_integer():
    assert python_lab.func(3) == 3

def test_func_with_string():
    assert python_lab.func("string") == "string"

def test_func_with_boolean():
    assert python_lab.func(True) == True


# Tests for the mult_two function
def test_mult_two_positive_numbers():
    assert python_lab.mult_two(3, 2) == 6

def test_mult_two_with_zero():
    assert python_lab.mult_two(0, 1) == 0


# Tests for the rectangle_perimeter function
def test_rectangle_perimeter_small_rectangle():
    assert python_lab.rectangle_perimeter(2, 4) == 12

def test_rectangle_perimeter_medium_rectangle():
    assert python_lab.rectangle_perimeter(3, 5) == 16

def test_rectangle_perimeter_large_rectangle():
    assert python_lab.rectangle_perimeter(10, 20) == 60

def test_rectangle_perimeter_odd_sides():
    assert python_lab.rectangle_perimeter(7, 2) == 18

def test_rectangle_perimeter_square():
    assert python_lab.rectangle_perimeter(1, 1) == 4

def test_rectangle_perimeter_thin_rectangle():
    assert python_lab.rectangle_perimeter(1, 5) == 12

def test_rectangle_perimeter_wide_rectangle():
    assert python_lab.rectangle_perimeter(4, 1) == 10

def test_rectangle_perimeter_large_square():
    assert python_lab.rectangle_perimeter(100, 100) == 400

def test_rectangle_perimeter_with_floats():
    assert python_lab.rectangle_perimeter(0.5, 2) == 5

