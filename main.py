from stats import get_book_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    get_book_text("books/frankenstein.txt")
    get_book_word_count("books/frankenstein.txt")


main()

