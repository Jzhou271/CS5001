def to_squares(list_of_integers, index):
    new = []
    for x in list_of_integers:
        new.append(x)
    for index in range(len(new)):
        if type(new[index]) != list:
            new[index] = new[index] ** 2
        else:
            new[index] = to_squares(new[index])
    return new


def main():
    print(to_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


if __name__ == "__main__":
    main()
