numEnglish = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
              6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}


def in_english(number):
    if number == 0:
        return ""
    digit = numEnglish[number % 10]
    return in_english(number // 10) + digit + " "


def main():
    print(in_english(567))


if __name__ == "__main__":
    main()
