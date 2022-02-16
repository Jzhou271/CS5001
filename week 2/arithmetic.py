'''CS5001
   Lab 2
   Question 2
   Jing Zhou
'''


def main():
    f_string = input("Input first number: ")
    s_string = input("Input second number: ")
    f_number = float(f_string)
    s_number = float(s_string)
    operator = input("Input operator (+,-,*,/): ")
    if operator == "+":
        answer = f_number + s_number
    elif operator == "-":
        answer = f_number - s_number
    elif operator == "*":
        answer = f_number * s_number
    elif operator == "/":
        if s_number == 0:
            answer = "NaN"
        else:
            answer = f_number / s_number
    else:
        print("Invalid operator. ""Please use +,-,*,/.")
        return
    print(f_string, operator, s_string, "=", answer)


if __name__ == "__main__":
    main()
