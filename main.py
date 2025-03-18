import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    
    #content = get_book_text(path_to_book)
    result = char_count(path_to_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    num_words(path_to_book)
    print("--------- Character Count -------")
    char_list = [{'char' : key, 'count' : value} for key, value in result.items()]
    char_list.sort(reverse=True, key=sort_on)
    for i in char_list:
        print(f"{i['char']}: {i['count']}")
    return 

main()