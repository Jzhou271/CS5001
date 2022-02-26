'''
This is the lab1 assignment.
1/20/2022
'''


def main():
    flo_number = input("Enter a floating point number:")
    f = float(flo_number) * 100
    int_number = int(f)
    final = "{} is {}/100".format(flo_number, int_number)
    print(final)


#if __name__ == "__main__":
main()
