import sys
from stats import count_words, char_frequency, sort_char_frequency

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def generate_report(filepath):
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...\n")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------")
    frequency = char_frequency(book_text)
    sorted_frequency = sort_char_frequency(frequency)
    for entry in sorted_frequency:
        print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")

def main():
    # Check if there are enough arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    # Get the book path from command line arguments
    file_path = sys.argv[1]
    generate_report(file_path)

main()