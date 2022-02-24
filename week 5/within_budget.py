'''
CS5001
Lab 5
Jing Zhou
Question 2: What can I afford?

The code designs for a function of within_budget, takes a list of prices and
set a value for the budget.
'''
import random


def within_budget(price_list, budget_value):
    '''
    The function within_budget takes a list of prices as input, and set a value
    for budget. Compared budget for each price in the list, remove out prices
    from list which  price is greater than budget. Then return the remaining
    prices that are smaller than budget.
    :param price_list: list of prices, float or integer numbers
    :param budget_value: a float or an integer number
    :return: list, which delect values that are greater than the budget_value
    '''    
    index = 0
    while index < len(price_list):
        if price_list[index] > budget_value:
            del price_list[index]
        else:
            index += 1
    return price_list


def test_within_budget_fixed(price_list, budget_value, expected=[]):
    '''
    This is the fixed test method to check if the code is correct
    '''
    print("PASS on input: ", price_list)
    actual = within_budget(price_list, budget_value)
    if expected:
        for i, j in zip(actual, expected):
            if i != j:
                print("FAIL on input:", price_list)
                print("ACTUAL output is", actual)
                print("However, EXPECTED output is", expected)
                return
        else:
            print("ACTUAL output is", actual)
            print("EXPECTED output is", expected)
    print()


def test_within_budget_random():
    '''
    This is the random method to test if the code is correct
    '''
    price_list = []
    i = 0
    while i < 10:
        price_list.append(random.random())
        i += 1
    budget_value = random.random()
    expected = test_base(price_list, budget_value)
    test_within_budget_fixed(price_list, budget_value, expected)


def test_base(price_list, budget):
    price_list.sort()
    i = 0
    while i < len(price_list):
        if price_list[i] > budget:
            return price_list[:i]
        i += 1


def main():
    test_within_budget_fixed([34, 49, 54, 74, 546], 80,
                             [34, 49, 54, 74])
    test_within_budget_fixed([12.42, 34.45, 56.2, 99.34, 1934.46], 60,
                             [12.42, 34.45, 56.2])
    test_within_budget_random()


if __name__ == "__main__":
    main()
