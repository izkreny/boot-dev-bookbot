def main():
    path = "books/frankenstein.txt"
    text = get_file_content(path)
    number_of_words = get_number_of_words(text)
    characters_dict = count_characters(text)
    list_of_letters = convert_dict_to_list_of_dicts(characters_dict)
    print_report(path, number_of_words, list_of_letters)


def get_file_content(path):
    with open(path) as file:
        return file.read()


def get_number_of_words(string):
    words = string.split()
    return len(words)


def count_characters(string):
    characters = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0}
    string = string.lower()

    for char in string:
        if char in characters:
            characters[char] += 1

    return characters


def convert_dict_to_list_of_dicts(dict):
    list = []

    for item in dict:
        letter = item
        letter_count = dict[item]
        list_item = {"name": letter, "count": letter_count}
        list.append(list_item)

    return list


def print_report(file, num_of_words, letters_list):
    letters_list.sort(reverse=True, key=lambda item: item["count"])

    print(f"--- Begin report for {file} file ---")
    print(f"{num_of_words} words found inside the file")
    print("")

    for letter in letters_list:
        char = letter["name"]
        count = letter["count"]
        print(f"The '{char}' charachter was found {count} times")
    print("--- End report ---")

main()
