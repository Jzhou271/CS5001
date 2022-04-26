def lower_triangle(n):
    if n < 1:
        return
    else:
        lower_triangle(n - 1)
    # now that we reached 1, we can start printing out the stars 
    # as we climb out the stack ...
    # print('* ' * n)
    print('* ' * n)


def main():
    lower_triangle(1)


if __name__ == "__main__":
    main()

