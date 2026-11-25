# Question 20: Write a program to demonstrate string formatting using the format() method and f-strings.

item = "Laptop"
price = 54999.5
quantity = 2

# format() method
msg1 = "Purchased {} x {} at INR {:.2f}".format(quantity, item, price)
print("Using .format():", msg1)

# f-string
msg2 = f"Purchased {quantity} x {item} at INR {price:.2f} (Total: INR {quantity * price:.2f})"
print("Using f-string :", msg2)
