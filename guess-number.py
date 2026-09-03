import random

def main():

    number = ""

    number = random.randint(1,100)


    name = input("Hello! What is your name?")
    guess = (f"Well, {name}, I am thinking of a number between 1 and 100. Take a guess:  ")

    while guess != number:
        if number > guess:
            print("Your guess is to low Guess again")
        if number < guess:
            print("Your guess was to high Guess again")
        if number == guess:
            break


if __name__ == "__main__":
    main()



