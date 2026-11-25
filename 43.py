# Question 43: Write a program to find the index of a specified element in a list.

cars = ["Audi", "BMW", "Tesla", "Toyota", "Ford"]
search_car = "Tesla"

if search_car in cars:
    idx = cars.index(search_car)
    print(f"'{search_car}' found at index: {idx}")
else:
    print(f"'{search_car}' not found in the list.")
