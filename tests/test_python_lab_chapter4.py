from checkio.python_lab_chapter4 import(
   to_title_case
)

def test_hello_world():
    assert to_title_case("hello world") == "Hello World"

def test_openai_gpt_4():
    assert to_title_case("openai gpt-4") == "Openai Gpt-4"

def test_this_is_a_title():
    assert to_title_case("this is a title") == "This Is A Title"

def test_the_quick_brown_fox():
    assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"

def test_jumps_over_lazy_dog():
    assert to_title_case("JUMPs ovER a LAZy dog") == "Jumps Over A Lazy Dog"

def test_typescript_is_great():
    assert to_title_case("typescript is great") == "Typescript Is Great"

def test_the_answer_is_42():
    assert to_title_case("the answer is 42") == "The Answer Is 42"

def test_to_be_or_not_to_be():
    assert to_title_case("to be or not to be") == "To Be Or Not To Be"

def test_that_is_the_question():
    assert to_title_case("that is the question") == "That Is The Question"

def test_empty_string():
    assert to_title_case("") == ""
