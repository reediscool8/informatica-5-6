import random

def main():

    coin = ["heads", "tails"]
    attemps = 3
    while attemps > 0:
        flip = random.choice(coin)
        guess = input("Heads or Tails? ").strip().lower()

        print("The coin landed on", flip)

        if guess == flip:
            print("You Win")
            break
        else:
            print("You Lost")
            attemps -=1
            print("Attemps left:", attemps)




if __name__ == "__main__":
    main()
