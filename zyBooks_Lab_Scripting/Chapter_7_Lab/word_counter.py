# Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method.
# The file contains a list of words separated by commas. Your program should output the words and their frequencies (the number of times each word appears in the file) without any duplicates.

import csv
from collections import Counter

# Function to read the CSV file and count word frequencies
def count_word_frequencies(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        words = []
        for row in reader:
            words.extend(row)
        
        word_counts = Counter(words)
        
        for word, count in word_counts.items():
            print(f"{word} {count}")

# Main code to read the filename and process the file
def main():
    filename = input('Enter filename:').strip()
    count_word_frequencies(filename)

if __name__ == "__main__":
    main()
