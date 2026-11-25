# Question 22: Write a program to demonstrate the difference between raw strings and normal strings.

# Normal string: escape sequences like \n, \t are processed
normal_str = "Hello\\nWorld\\tPython"

# Raw string: escape sequences are treated as literal characters (prefixed with r)
raw_str = r"Hello\nWorld\tPython"

print("Normal string (with escape interpretation):")
print(normal_str)

print("\nRaw string (treated as literal text):")
print(raw_str)
