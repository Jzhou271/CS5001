def choose(n, k): 
    if k == 0:
        return 1
    if n == k:
        return 1
    else:
        return choose(n-1, k-1) + choose(n-1, k)


def main():
    print(choose(50, 3))


if __name__ == "__main__":
    main()
