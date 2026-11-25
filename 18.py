# Question 18: Write a program to find the longest word in a given sentence using string operations.

sentence = "Programming in Python provides exceptional capabilities"
words = sentence.split()

longest_word = max(words, key=len)

print("Sentence:", sentence)
print(f"Longest word: '{longest_word}' (length: {len(longest_word)})")
