# Question 25: Write a program to check whether two strings are equal, ignoring their case.

str1 = "Hello World"
str2 = "hello world"

if str1.lower() == str2.lower():
    print(f"'{str1}' and '{str2}' are equal (case-insensitive).")
else:
    print(f"'{str1}' and '{str2}' are NOT equal.")
