# Write a program that replaces words in a sentence.
# The input begins with word replacement pairs (original and replacement).
# The next line of input is the sentence where any word on the original list is replaced.


# Step 1: Read word replacement pairs
replacement_pairs = input().strip().split()

# Step 2: Construct replace_dict
replace_dict = {}
for i in range(0, len(replacement_pairs), 2):
    replace_dict[replacement_pairs[i]] = replacement_pairs[i + 1]

# Step 3: Read the sentence
sentence = input()

# Step 4: Replace words in the sentence
words = sentence.split()
modified_words = []
for word in words:
    if word in replace_dict:
        modified_words.append(replace_dict[word])
    else:
        modified_words.append(word)

# Step 5: Construct modified sentence
modified_sentence = ' '.join(modified_words)

# Step 6: Print the modified sentence
print(modified_sentence)
