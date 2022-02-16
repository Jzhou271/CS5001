'''CS5001
   Homework 2
   Jing Zhou
   2/1/2022
'''


def main():
    num_abc = int(input("Enter number:"))
    if 1 <= num_abc <= 4999:
        tmp = num_abc
        roman_num = (num_abc // 1000) * 'M'
        num_abc = num_abc - (num_abc // 1000) * 1000
        roman_num = roman_num + (num_abc // 500) * 'D'
        num_abc = num_abc - (num_abc // 500) * 500
        roman_num = roman_num + (num_abc // 100) * 'C'
        num_abc = num_abc - (num_abc // 100) * 100
        roman_num = roman_num + (num_abc // 50) * 'L'
        num_abc = num_abc - (num_abc // 50) * 50
        roman_num = roman_num + (num_abc // 10) * 'X'
        num_abc = num_abc - (num_abc // 10) * 10
        roman_num = roman_num + (num_abc // 5) * 'V'
        num_abc = num_abc - (num_abc // 5) * 5
        roman_num = roman_num + (num_abc // 1) * 'I'
    else:
        return
    print(tmp, "is", roman_num)


if __name__ == "__main__":
    main()
