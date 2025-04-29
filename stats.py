def get_book_word_count(book_text):
    word_count = len(book_text.split())
    return word_count

def char_counter(book_text):
    char_count = {}
    lower_text = book_text.lower()
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sorted_list(char_count):
    sort_list = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    return sort_list

def full_report(word_count, char_count, sort_list, filepath):
    print("============ BOOKBOT ============\n"
              f"Analyzing book found at {filepath}...\n"
              "----------- Word Count ----------\n"
              f"Found {word_count} total words\n"
              "--------- Character Count -------"
    )
    for i in range(0,len(sort_list)):
        if sort_list[i][0].isalpha():  # Only include alphabetic characters
            print(f"{sort_list[i][0]}: {sort_list[i][1]}")
    print("============= END ===============")
