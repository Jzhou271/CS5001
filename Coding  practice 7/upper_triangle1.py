def printPatternRowRecur(n):
    # base condition
    if (n < 1):
        return        

    # print the remaining
    # stars of the n-th row
    # recursively
    print("*", end = " ")
    printPatternRowRecur(n - 1)


def upper_triangle(n):
    # base condition
    if (n < 1):
        return
     
    # print the stars of
    # the n-th row
    printPatternRowRecur(n)
     
    # move to next line
    print("")
     
    # print stars of the
    # remaining rows recursively
    upper_triangle(n - 1)


def main():
    upper_triangle(5)


if __name__ == "__main__":
    main()
