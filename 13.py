# Question 13: Write a program to check whether a given string starts and ends with a particular character.

text = "apple"
start_char = 'a'
end_char = 'e'

starts = text.startswith(start_char)
ends = text.endswith(end_char)

print(f"Text: '{text}'")
print(f"Starts with '{start_char}': {starts}")
print(f"Ends with '{end_char}': {ends}")
