# Question 7: Write a program to count the number of digits, alphabets and special characters in a string.

text = "Python_3.12 @ UTU-2024!"

alphabets = 0
digits = 0
special = 0

for ch in text:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print(f"String: '{text}'")
print(f"Alphabets: {alphabets}")
print(f"Digits: {digits}")
print(f"Special characters (including spaces/punctuation): {special}")
