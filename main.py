from stats import get_book_word_count, char_counter, sorted_list, full_report
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    print("Usage: python3 main.py <path_to_book>")
    
    book_text = get_book_text(filepath)
    get_book_word_count(book_text)
    char_counter(book_text)
    sorted_list(char_counter(book_text))
    full_report(get_book_word_count(book_text), char_counter(book_text), sorted_list(char_counter(book_text)), filepath)
    sys.exit(1)
filepath = sys.argv[1]
main()

