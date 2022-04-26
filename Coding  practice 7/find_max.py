def find_max(list_of_integers):
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        # [1:] is remaining numbers after index
        return max(list_of_integers[0], find_max(list_of_integers[1:]))


def main():
    print(find_max([4, 6, -1, 0, 200, -5, 44]))


if __name__ == "__main__":
    main()
