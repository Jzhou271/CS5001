
"""
CS5001
Jing Zhou
Coding practice -- Module 2
Price per liter
Suppose you are at the grocery store to buy soda and you want to get the
best deal. Write a program that reads in the price of a six-pack of soda
and the price of a two-liter bottle. The program should print out the price
per liter for both assuming that cans are 12 oz or 0.355 liters
"""


def main():
    six_pack_price = float(input("Price per six-pack: "))
    two_liter_price = float(input("Price per two-liter: "))
    six_pack_ppl = six_pack_price / (0.355 * 6)
    two_liter_ppl = two_liter_price / 2
    print("Six-pack price per liter: ", six_pack_ppl)
    print("Two-liter price per liter:", two_liter_ppl)


if __name__ == "__main__":
    main()
