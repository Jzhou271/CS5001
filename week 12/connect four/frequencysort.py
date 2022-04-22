"""
Jing Zhou
Lab 12 Efficiency, Searching, and Sorting
If two elements have different frequencies, then the one which has a greater
frequency should come first.
If two elements have the same frequency, than the one that appeared first in
the original list should come first.
"""
from collections import defaultdict


def value_pair():
    """
    The function initially takes list by frequence of numbers and index that
    comes to the list
    """
    # [freq, first_idx]
    return [0, -1]


def sort(list_of_numbers):
    """
    The function initially takes list of numbers, and convert into dictionary
    by key of numbers and value of [frequency, first index]. Then sort numbers
    by frequence first, and sort numbers by index next
    :param: list | list of numbers, can be integer and float
    :return: list | final list that return the frequency first, and remaining
    idex comes by original order
    """
    # get freq and idx for each number
    freq_with_idx = defaultdict(value_pair)
    for idx, num in enumerate(list_of_numbers):
        freq_with_idx[num][0] += 1
        if freq_with_idx[num][1] == -1:
            freq_with_idx[num][1] = idx

    # sort numbers by freq
    freq_ordered_list = [[] for _ in range(len(list_of_numbers) + 1)]
    for key in freq_with_idx:
        freq = freq_with_idx[key][0]
        freq_ordered_list[freq].append(key)

    # sort numbers by idx
    freq_idx_ordered_list = []
    for i in range(len(freq_ordered_list) - 1, -1, -1):
        if freq_ordered_list[i]:
            while freq_ordered_list[i]:
                min_idx = float('inf')
                element = None
                for num in freq_ordered_list[i]:
                    idx = freq_with_idx[num][1]
                    if idx < min_idx:
                        min_idx = idx
                        element = num
                freq_idx_ordered_list.append(element)
                freq_ordered_list[i].remove(element)

    # store numbers sorted by freq and idx
    res_list = []
    for num in freq_idx_ordered_list:
        times_to_repeat = freq_with_idx[num][0]
        for i in range(times_to_repeat):
            res_list.append(num)
    return res_list


def main():
    print(sort([3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]))
    print(sort([4, 5, 4, 5, 6, 9, 1, 1, 0]))


if __name__ == "__main__":
    main()
