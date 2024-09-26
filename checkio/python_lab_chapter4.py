
# ex Convert To Title Case
def to_title_case(sentence: str) -> str:
    words = sentence.split(" ")  
    title_cased = map(str.capitalize, words) 
    return " ".join(title_cased)

