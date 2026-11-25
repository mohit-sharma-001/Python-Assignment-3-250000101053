# Question 12: Write a program to find the first and last occurrence of a character using string methods.

text = "programming in python"
char = 'p'

first_idx = text.find(char)
last_idx = text.rfind(char)

print(f"String: '{text}'")
print(f"Target character: '{char}'")
print(f"First occurrence index: {first_idx}")
print(f"Last occurrence index : {last_idx}")
