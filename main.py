from stats import word_count, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    frank_count = word_count(book_text)
    print(f"{frank_count} words found in the document")
    
    print(character_count(book_text))
main()