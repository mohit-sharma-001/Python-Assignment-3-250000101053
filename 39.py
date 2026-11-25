# Question 39: Write a program to merge two lists into a single list.

list_a = [1, 2, 3]
list_b = [4, 5, 6]

# Method 1: Using + operator
merged = list_a + list_b

# Method 2: Using extend
extended = list_a.copy()
extended.extend(list_b)

print("List A:", list_a)
print("List B:", list_b)
print("Merged list:", merged)
