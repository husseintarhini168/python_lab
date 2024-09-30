"""
This module contains test cases for the function `to_title_case` 
from the 'checkio.python_lab_chapter4' module. The purpose of this test
is to verify that the function correctly capitalizes the first letter of each 
word in a string.

The test included checks the basic functionality by passing the string 
"hello world" and expecting the result "Hello World". 
More tests can be added to validate different edge cases and inputs.
"""

from checkio.python_lab_chapter4 import to_title_case

def test_hello_world():
    """
    Test the to_title_case function with the input "hello world".
    It should return the string "Hello World" with each word capitalized.
    
    This test ensures that the function can handle basic cases where 
    the input is a lowercase string with space-separated words.
    """
    assert to_title_case("hello world") == "Hello World"
