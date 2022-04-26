def sum_values(list_of_integers, index):
    list_length = len(list_of_integers)
    if index == list_length:
        return 0
    return list_of_integers[index] + sum_values(list_of_integers, index + 1)


def main():
    print(sum_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))


if __name__ == "__main__":
    main()
