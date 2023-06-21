import re
from collections import Counter

def count_words(filename, num_words):
    # Read the file
    with open(filename, 'r') as file:
        text = file.read()

    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Count the occurrences of each word
    word_counts = Counter(text.split())

    # Display the most frequent words
    print(f"Top {num_words} most frequently used words:")
    for word, count in word_counts.most_common(num_words):
        print(f"{word}: {count}")

# Example usage
filename = 'example.txt'  # Replace with your file name
num_words = 10  # Replace with the desired number of words to display

count_words(filename, num_words)
