# Question 37: Write a program to find the second-largest element in a list.

numbers = [10, 45, 23, 89, 67, 89, 54]

unique_sorted = sorted(list(set(numbers)))
if len(unique_sorted) >= 2:
    second_largest = unique_sorted[-2]
    print("List:", numbers)
    print("Second largest element:", second_largest)
else:
    print("List does not have at least 2 distinct elements.")
