'''
Design and implement a program that is capable of converting a decimal 
number between 1 and 4999 (inclusive) as a roman numeral. 
Value	1000	500	100	50	10	5	1
Letter	M	D	C	L	X	V	I
In this assignment, we will be using a simplified version of roman 
numerals where each of the letter values are additive. This means that 
MMXXI = 1000 + 1000 + 10 + 10 + 1 = 2021 and MMMMDCCCCLXXXXVIIII = 
1000 + 1000 + 1000 + 1000 + 500 + 100 + 100 + 100 + 100 + 50 + 10 + 
10 + 10 + 10 + 5 + 1 + 1 + 1 + 1 = 4999. In this form, the letters 
are always in descending order so that 4 is represented by IIII rather 
than the more common IV.
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
