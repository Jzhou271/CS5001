"""
Coding practice -- Module 6
10. Count words
Write a program that reads in a sentence from the keyboard and prints each
word on it's own line.

Enter a sentence: The cat in the hat
0. The
1. cat
2. in
3. the
4. hat

"""


def count_words(sentence):
    sentence = input("Enter a sentence: ")
    str1 = sentence.split()
    output = ""
    i = 0
    for i in range(len(str1)):
        var = str(i) + ". "
        output += var + str(str1[i]) + "\n"
    return output.strip()


def main():
    print(count_words(""))


if __name__ == "__main__":
    main()
