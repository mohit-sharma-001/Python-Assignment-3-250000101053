# Question 14: Write a program to remove leading and trailing spaces from a string.

text = "   Hello, Python Learners!   "

stripped = text.strip()
l_stripped = text.lstrip()
r_stripped = text.rstrip()

print(f"Original       : '{text}'")
print(f"strip()        : '{stripped}'")
print(f"lstrip()       : '{l_stripped}'")
print(f"rstrip()       : '{r_stripped}'")
