#ex 1  Count Vowels
def count_vowels(text: str) -> int:
    text = text.lower()  
    vowels = "aeiou" 
    count = 0
    for char in text:
        if char in vowels:  
            count += 1
    return count


print("Example:")
print(count_vowels("Hello"))

assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")

#ex 2 Sum of Integers
def sum_upto_n(N: int) -> int:
    sum=0
    for i in range(N+1):
        sum=sum+i
    return sum


print("Example:")
print(sum_upto_n(11))

# These "asserts" are used for self-checking
assert sum_upto_n(1) == 1
assert sum_upto_n(2) == 3
assert sum_upto_n(3) == 6
assert sum_upto_n(4) == 10
assert sum_upto_n(5) == 15
assert sum_upto_n(10) == 55
assert sum_upto_n(20) == 210
assert sum_upto_n(100) == 5050
assert sum_upto_n(200) == 20100
assert sum_upto_n(500) == 125250

print("The mission is done! Click 'Check Solution' to earn rewards!")
