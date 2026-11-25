# Question 38: Write a program to remove duplicate elements from a list.

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]

# Preserving order while removing duplicates
unique_list = []
for n in numbers:
    if n not in unique_list:
        unique_list.append(n)

print("Original list:", numbers)
print("Unique list  :", unique_list)
