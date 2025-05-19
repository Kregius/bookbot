import sys
from stats import number_of_words, character_count, sorted_dictionaries

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        book_text = get_book_text(path)
        word_count = number_of_words(book_text)
        print(f"Found {word_count} total words")
        #print(character_count(book_text))
        letter_dict = character_count(book_text)
        sorted_letters = sorted_dictionaries(letter_dict)
        for entry in sorted_letters:
            print(f"{entry['name']}: {entry['num']}")


if __name__ == "__main__":
    main()