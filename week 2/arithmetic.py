'''
In this program you will write a simple arithmetic program. It will 
take one number as input (either an integer or a floating point number)
and then a second, and then ask for an operator (+, -, *, /). If a 
different string is input for an operator display a message saying it
is an invalid operator (see example below). If the second number is 0 
and the operator is / the answer should be NaN.
1/22/2022
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
