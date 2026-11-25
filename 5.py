# Question 5: Write a program to check whether a given string is a palindrome.

text = "radar"
clean_text = text.lower()

if clean_text == clean_text[::-1]:
    print(f"'{text}' is a Palindrome.")
else:
    print(f"'{text}' is not a Palindrome.")
