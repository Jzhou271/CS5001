'''
This is a project to design an ATM. the purpose for dispense money using coins
and bills a possible. the machine can dispense the following denominations:
$50, $20, $10, $5, $2, $1, $0.25, $0.10, $0.05. Assume the input will alawys
be non-negative.
2/19/2022
'''


def atm_withdrawing():
    '''
    Withdrawing money from ATM, input a single float number to print exactly
    bills and coins based on denominations.
    :param: no params
    :return: return nothing
    '''
    withdraw_amount = float(input("Input request: "))
    withdraw_amount = int(withdraw_amount * 100)
    # how many bills of $50 need to be withdrawn
    wda_50 = withdraw_amount // 5000
    withdraw_amount = withdraw_amount % 5000
    if 4998 <= withdraw_amount <= 5000:
        wda_50 += 1
        withdraw_amount = 0
    if wda_50 == 1:
        print(wda_50, "fifty")
    elif wda_50 > 1:
        print(wda_50, "fifties")
    if withdraw_amount == 0:
        return
    # how many bills of $20 need to be withdrawn
    wda_20 = withdraw_amount // 2000
    withdraw_amount = withdraw_amount % 2000
    if 1998 <= withdraw_amount <= 2000:
        wda_20 += 1
        withdraw_amount = 0
    if wda_20 == 1:
        print(wda_20, "twenty")
    elif wda_20 > 1:
        print(wda_20, "twenties")
    if withdraw_amount == 0:
        return
    # how many bills of $10 need to be withdrawn
    wda_10 = withdraw_amount // 1000
    withdraw_amount = withdraw_amount % 1000
    if 998 <= withdraw_amount <= 1000:
        wda_10 += 1
        withdraw_amount = 0
    if wda_10 != 0:
        print(wda_10, "ten")
    if withdraw_amount == 0:
        return
    # how many bills of $5 need to be withdrawn
    wda_5 = withdraw_amount // 500
    withdraw_amount = withdraw_amount % 500
    if 498 <= withdraw_amount <= 500:
        wda_5 += 1
        withdraw_amount = 0
    if wda_5 != 0:
        print(wda_5, "five")
    if withdraw_amount == 0:
        return
    # how many bills of $2 need to be withdrawn
    wda_2 = withdraw_amount // 200
    withdraw_amount = withdraw_amount % 200
    if 198 <= withdraw_amount <= 200:
        wda_2 += 1
        withdraw_amount = 0
    if wda_2 == 1:
        print(wda_2, "toony")
    elif wda_2 > 1:
        print(wda_2, "toonies")
    if withdraw_amount == 0:
        return
    # how many bills of $1 need to be withdrawn
    wda_1 = withdraw_amount // 100
    withdraw_amount = withdraw_amount % 100
    if 98 <= withdraw_amount <= 100:
        wda_1 += 1
        withdraw_amount = 0
    if wda_1 != 0:
        print(wda_1, "loony")
    if withdraw_amount == 0:
        return
    # how many coins of $0.25 need to be withdrawn
    wda_025 = withdraw_amount // 25
    withdraw_amount = withdraw_amount % 25
    if 23 <= withdraw_amount <= 25:
        wda_025 += 1
        withdraw_amount = 0
    if wda_025 == 1:
        print(wda_025, "quarter")
    elif wda_025 > 1:
        print(wda_025, "quarters")
    if withdraw_amount == 0:
        return
    # how many coins of $0.10 and $0.05 need to be withdrawn
    if 18 <= withdraw_amount <= 22:
        print("2 dimes")
    elif 13 <= withdraw_amount <= 17:
        print("1 dime\n1 nickel")     
    elif 8 <= withdraw_amount <= 12:
        print("1 dime")
    elif 3 <= withdraw_amount <= 7:
        print("1 nickel")
    elif 1 <= withdraw_amount <= 2:
        return
    if withdraw_amount == 0:
        return


def main():
    atm_withdrawing()


if __name__ == "__main__":
    main()
