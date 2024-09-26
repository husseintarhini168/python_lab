# ex 1 Count Vowels
def count_vowels(text: str) -> int:
    text = text.lower()  
    vowels = "aeiou" 
    count = 0
    for char in text:
        if char in vowels:  
            count += 1
    return count


# ex 2 Sum of Integers
def sum_upto_n(N: int) -> int:
    total_sum = 0
    for i in range(N + 1):
        total_sum += i
    return total_sum
