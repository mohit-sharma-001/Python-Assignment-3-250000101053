# Question 49: Write a program to demonstrate tuple immutability and create a modified tuple using concatenation.

t_original = (1, 2, 3, 4)
print("Original tuple:", t_original)

# Tuples are immutable: t_original[0] = 10 would raise TypeError
print("Tuples are immutable; modifying elements directly raises TypeError.")

# Creating a modified tuple via concatenation/slicing
t_modified = (99,) + t_original[1:]
print("Modified tuple:", t_modified)
