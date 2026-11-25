# Question 32: Write a program to append five elements to an existing list.

my_list = [1, 2, 3]
print("Initial list:", my_list)

new_elements = [4, 5, 6, 7, 8]
for elem in new_elements:
    my_list.append(elem)

print("List after appending 5 elements:", my_list)
