def main():
    path = "books/frankenstein.txt"
    text = get_file_content(path)
    number_of_words = get_number_of_words(text)
    print(f"Text inside {path} file contains {number_of_words} number of words.")


def get_file_content(path):
    with open(path) as file:
        return file.read()

def get_number_of_words(string):
    words = string.split()
    return len(words)


main()
