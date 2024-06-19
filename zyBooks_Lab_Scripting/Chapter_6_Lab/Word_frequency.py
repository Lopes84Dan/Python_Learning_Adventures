# Write a program that reads a list of words.
# Then, the program outputs those words and their frequencies.

# Read input from user
user_input = input()

# Split the input into a list of words
words = user_input.split()

# Create an empty dictionary to store word frequencies
word_counts = {}

# Count the frequency of each word
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Output each word and its frequency
for word in words:
    print(f'{word} {word_counts[word]}')
