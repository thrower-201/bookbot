import sys

# Check if there are enough arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path from command line arguments
path_to_book = sys.argv[1]

# Read the book
with open(path_to_book, "r") as f:
    text = f.read()

# Count words
word_count = len(text.split())

# Count letters
letter_counts = {}
for char in text.lower():
    if char.isalpha():
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

# Print report
print(f"--- Begin report of {path_to_book} ---")
print(f"{word_count} words found in the document")
print()

# Sort letters by frequency
sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
for char, count in sorted_letters:
    print(f"The '{char}' character was found {count} times")

print("--- End report ---")