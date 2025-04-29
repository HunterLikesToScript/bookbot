from stats import get_book_word_count, char_counter, sorted_list, full_report
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    
    try:
        filepath = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(filepath)
    get_book_word_count(book_text)
    char_counter(book_text)
    sorted_list(char_counter(book_text))
    full_report(get_book_word_count(book_text), char_counter(book_text), sorted_list(char_counter(book_text)), filepath)
    
main()

