# Question 3: Write a program to count vowels and consonants separately in a string.

text = "Hello World"
vowels_set = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels_set:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Text: '{text}'")
print(f"Vowels count: {vowel_count}")
print(f"Consonants count: {consonant_count}")
