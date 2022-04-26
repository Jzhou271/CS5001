def formula(x):   
    if x <= 1:
        return 3
    else:
        return 2 * formula(x - 1) + 5


def main():
    print(formula(5))


if __name__ == "__main__":
    main()
