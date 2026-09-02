import random

def main():

    guess = input("Guess (heads/tails): ").strip().lower()

    coinflip = random.choice(["heads", "tails"])

    print(f"Result: {coinflip}")


    if guess == coinflip:
        print("You win!")
    else:
        print("You Lose")

if __name__ == "__main__":
    main()
