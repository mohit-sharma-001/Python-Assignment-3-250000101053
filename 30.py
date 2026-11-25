# Question 30: Write a program to count the number of even and odd elements in a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = sum(1 for n in numbers if n % 2 != 0)

print("Numbers:", numbers)
print("Even numbers count:", even_count)
print("Odd numbers count :", odd_count)
