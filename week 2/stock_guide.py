'''CS5001
   Lab 2
   Question 4
   Jing Zhou
   1/31/3022
'''


def main():
    rating_score = int(input("Input rating: "))
    if rating_score > 100:
        print("Buy a lot")
    elif 76 < rating_score <= 100:
        print("Buy a little")
    elif 50 <= rating_score <= 76:
        print("Stay")
    elif 25 < rating_score < 50:
        print("Sell")
    else:
        print("Sell! Sell! Sell!")


if __name__ == "__main__":
    main()
