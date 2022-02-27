"""
CS5001
Jing Zhou
Coding practice -- Module 5
Read values
"""


def read_values(integer):
    output = []
    i = 0
    while i < len(integer):
        if integer[i] > 0:
            output.append(integer[i])
            i += 1
        else:
            del integer[i]
    return output


def main():
    print(read_values([-56, -5, -99, 66, 0, 35, 46, 4986]))


if __name__ == "__main__":
    main()
