# Question 19: Write a program to count the frequency of each character in a string.

text = "mississippi"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(f"String: '{text}'")
print("Character Frequencies:")
for ch, count in freq.items():
    print(f"'{ch}': {count}")
