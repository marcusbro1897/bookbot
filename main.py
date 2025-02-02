def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} Wörter sind in dem Buch")
    char_list = get_alph_chars(num_chars)
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_characters(text):
    chars = {}
    words_lower = text.lower()
    for char in words_lower:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(dict):
    return dict["char"]


def get_alph_chars(chars):
    char_list = []
    for char in chars: 
        if char.isalpha():
            char_dict = {
                "char": char,
                "num": chars[char]
            }
            char_list.append(char_dict)
            char_list.sort(key=sort_on)
            for item in char_list:
                print(f"The '{item['char']}' character was found {item['num']} times")

main()  