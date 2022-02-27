"""
CS5001
Jing Zhou
Coding practice -- Module 5
Extract letter
Write a function called extract_letter that returns the correct letter in
a word. It should take two parameters, the word and the index of the letter
to return. For example, the call extract_letter("Strings", 5) would be g
"""


def extract_letter(strings, index_num):
    return strings[index_num]


def main():
    print(extract_letter("evenlyn", 4))


if __name__ == "__main__":
    main()
