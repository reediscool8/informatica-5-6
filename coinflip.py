import random

def main():

    guess = input("Guess (heads/tails): ").strip().lower()

 #Before you think i cheated, I had seen the choice on a python reel and thought i would give it a shot
    coinflip = random.choice(["heads", "tails"])
#The print f i had to look up i dont fully understand it, but i couldnt get the code to work other wise
    print(f"Result: {coinflip}")


    if guess == coinflip:
        print("You win!")
    else:
        print("You Lose")

if __name__ == "__main__":
    main()
