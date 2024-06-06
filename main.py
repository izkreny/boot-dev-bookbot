def main():
    path = "books/frankenstein.txt"
    text = get_file_content(path)
    number_of_words = get_number_of_words(text)
    characters = count_characters(text)
    print(f"Text inside {path} file contains {number_of_words} number of words.")
    print(f"Characters found: {characters}")


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


main()
