def get_book_word_count(book_text):
    word_count = len(book_text.split())
    print(f"{word_count} words found in the document")

def char_counter(book_text):
    char_count = {}
    lower_text = book_text.lower()
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    print(char_count)