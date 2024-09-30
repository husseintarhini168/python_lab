from checkio.python_lab_chapter4 import to_title_case

def test_hello_world():
    """
    Test the to_title_case function with the input "hello world".
    It should return the string "Hello World" with each word capitalized.
    """
    assert to_title_case("hello world") == "Hello World"
