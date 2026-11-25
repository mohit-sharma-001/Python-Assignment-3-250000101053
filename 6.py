# Question 6: Write a program to count uppercase and lowercase characters in a string.

text = "Veer Madho Singh BHANDARI"

upper_count = sum(1 for c in text if c.isupper())
lower_count = sum(1 for c in text if c.islower())

print(f"Text: '{text}'")
print(f"Uppercase characters: {upper_count}")
print(f"Lowercase characters: {lower_count}")
