# Question 34: Write a program to delete an element from a specified index using pop().

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

removed_item = numbers.pop(2)  # Removes element at index 2 (value 30)
print(f"Popped element at index 2: {removed_item}")
print("List after pop:", numbers)
