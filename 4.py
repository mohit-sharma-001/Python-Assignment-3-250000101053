# Question 4: Write a program to reverse a string without using built-in reverse functions.

text = "Uttarakhand"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(f"Original String: '{text}'")
print(f"Reversed String: '{reversed_text}'")
