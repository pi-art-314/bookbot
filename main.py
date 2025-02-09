def main():
    content_path = "books/frankenstein.txt"
    content = get_content(content_path)
    char_count = get_alpha_char_count(content)
    sorted_char_count = sort_dictionary(char_count)
    for obj in sorted_char_count:
       print(f"The '{obj['Char']}' character was found {obj['Num']} times")

def get_content(path):
    with open(path) as content:
        return content.read()

def get_word_count(book_content):
    return len(book_content.split())

def get_raw_char_count(book_content):
    char_count = {}
    for raw_char in book_content:
        char = raw_char.lower()
        try:
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1
    return char_count

def get_alpha_char_count(book_content):
    char_count = {}
    for raw_char in book_content:
        if raw_char.isalpha():
            alpha_char = raw_char.lower()
            try:
                char_count[alpha_char] += 1
            except KeyError:
                char_count[alpha_char] = 1
    return char_count

def sort_dictionary(input_dict):
    sortlist = []
    for entry in input_dict:
        sortlist.append(dict(Char = entry, Num = input_dict[entry]))
    return sorted(sortlist, reverse=True, key=lambda x: x['Num'])

main()

