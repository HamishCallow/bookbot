import sys
from stats import count_words
from stats import count_characters
from stats import get_book_text
from stats import char_sort
from stats import alpha_char
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        num_words = count_words(book_text)
        num_char = count_characters(book_text)
        char_num_list = char_sort(num_char)
        alpha_char_list = alpha_char(char_num_list)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in alpha_char_list:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
main()

