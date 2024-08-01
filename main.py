def main():
    path = "books/frankenstein.txt"
    text = read_file(path)

    word_count = count_words(text)
    chars = count_chars(text)
    dict_list = convert_to_list(chars)
    dict_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    print_dict_list(dict_list)

    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)


def read_file(path):
    with open(path) as file:
        return file.read()
    return ""


def count_chars(text):
    text = text.lower()
    result = {}

    for char in text:
        if not char.isalpha():
            continue
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


def convert_to_list(d):
    result = []
    for obj in d:
        result.append({
            "letter": obj,
            "count": d[obj],
            })

    return result


def sort_on(d):
    return d["count"]


def print_dict_list(lst):
    for d in lst:
        char = d["letter"]
        count = d["count"]
        print(f"The '{char}' character was found {count} times")


main()
