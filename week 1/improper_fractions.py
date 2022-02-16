'''
Jing Zhou
2022 Jan 20
CS5001

This is the lab1 assignment.
'''


def main():
    flo_number = input("Enter a floating point number:")
    f = float(flo_number) * 100
    int_number = int(f)
    final = "{} is {}/100".format(flo_number, int_number)
    print(final)


#if __name__ == "__main__":
main()
