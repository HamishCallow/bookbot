def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents 
def count_words(book_text):
    wordcount = book_text.split()
    return len(wordcount)
def count_characters(book_text):
    char_count = {}
    low_text = book_text.lower()
    for char in low_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def char_sort(char_count):
    char_list = []
    for key, num in char_count.items():
        char_list.append({"char": key, "num": num})
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list
def alpha_char(char_list):
    final_list = []
    for char in char_list:
        if char["char"].isalpha():
            final_list.append(char)
    return final_list