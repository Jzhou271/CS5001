'''
You are looking to invest money in some new stocks. But you need help 
deciding if you should buy a little, buy a lot, sell, or stay. Create 
a system that takes in a number representing an analyst rating. If 
the rating is above 100 the program should output "Buy a lot", if 
the rating is above 76 and no higher than 100 the system should 
output "Buy a little", if the rating is between 50 and 76 the output
should be "Stay", if the rating is lower than 50 but above 25 the 
output should be "Sell", and if the rating is 25 or less the output 
should be "Sell! Sell! Sell!"
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
