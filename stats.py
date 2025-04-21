def word_count(book):
    book_list = book.split()
    return len(book_list)
def character_count(book):
    char_dict = {}
    for char in book:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict