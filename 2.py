# Question 2: Write a program to count the number of vowels in a given string.

text = "Artificial Intelligence"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"String: '{text}'")
print(f"Total vowels: {count}")
