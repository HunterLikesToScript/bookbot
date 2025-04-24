from stats import get_book_word_count, char_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    book_text = get_book_text("books/frankenstein.txt")
    get_book_word_count(book_text)
    char_counter(book_text)


main()

