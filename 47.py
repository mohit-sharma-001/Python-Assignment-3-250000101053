# Question 47: Write a program to count the occurrences of a given element in a tuple using count().

t = (1, 3, 7, 8, 7, 5, 4, 7, 9)
elem = 7

occurrences = t.count(elem)
print("Tuple:", t)
print(f"Element {elem} occurs {occurrences} times.")
