def get_book_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        print(f"{word_count} words found in the document")
