from stats import word_count, character_count, dict_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:  
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    frank_count = word_count(book_text)
    print(f"{frank_count} words found in the document")
    
    counted = character_count(book_text)
    sorted = dict_sort(counted)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {frank_count} total words")
    print("--------- Character Count -------")
    for item in sorted:
        
        print(f"{item['Letter']}: {item['Count']}")

main()