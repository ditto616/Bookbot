from stats import word_count, character_count, dict_sort

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    frank_count = word_count(book_text)
    print(f"{frank_count} words found in the document")
    
    counted = character_count(book_text)
    sorted = dict_sort(counted)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {frank_count} total words")
    print("--------- Character Count -------")
    for item in sorted:
        
        print(f"{item['Letter']}: {item['Count']}")

main()