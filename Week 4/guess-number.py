import random

def main():
    number = random.randint(1, 100)
    name = input("Hello! What is your name? ")

    guess = int(input(f"Well, {name}, I am thinking of a number between 1 and 100. Take a guess: "))

    while guess != number:
        if number > guess:
            print("Your guess is too low. Guess again.")

        elif number < guess:
            print("Your guess was too high. Guess again.")


        guess = int(input("Take another guess: "))

    print(f"You guessed it!  Gooooood boy {name}")

if __name__ == "__main__":
    main()
