def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_content(file_path)
    word_count = get_word_count(file_contents)
    letter_count = get_letter_count(file_contents)
    sorted_letters = sort_letters(letter_count)
    create_report(file_path, word_count, sorted_letters)

def get_word_count(book):
    words = book.split()
    return len(words)

def get_letter_count(book):
    letter_count = {}
    for l in book:
        lower_case_book = l.lower()
        if lower_case_book in letter_count:
            letter_count[lower_case_book] += 1
        else:
            letter_count[lower_case_book] = 1
    return letter_count

def sort_letters(letter_dict):
    filtered_list = []
    single_letter = {}
    for letter in letter_dict:
        if letter.isalpha():
            single_letter["letter"] = letter
            single_letter["num"] = letter_dict[letter]
            filtered_list.append(single_letter)
            single_letter = {}
    filtered_list.sort(reverse=True, key=sort_on)
    return filtered_list

def sort_on(dict):
    return dict["num"]

def create_report(file_path, word_count, sorted_list):
    print(f"--- Begin report of {file_path} ---\n{word_count} words found in the document\n\n")
    for char in sorted_list:
        print(f"The '{char["letter"]}' character was found {char["num"]} times")
    print("--- End report ---")

def get_book_content(file_path):
    with open(file_path) as f:
        return f.read()

main()