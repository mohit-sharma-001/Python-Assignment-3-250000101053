# Question 44: Write a program to copy one list into another and demonstrate the difference between copy() and direct assignment.

original = [1, 2, [3, 4]]

# Direct assignment (creates alias / reference)
direct_ref = original

# Shallow copy using copy()
copied = original.copy()

original.append(5)

print("Original after append(5):", original)
print("Direct assignment (affected):", direct_ref)
print("copy() list (not affected by outer append):", copied)
