import random

def main():
    print("Mathlingo")
    streak = 0
    while streak < 3:
        number1 = random.randint(10, 99)
        number2 = random.randint(10, 99)

        print(f"What is {number1} + {number2}?")

        answer = int(input("Your answer: "))

        if answer == number1 + number2:
            streak = streak + 1
            print(f"Correct! Streak: {'⭐' * streak}")
        else:
            streak = 0
            print("Incorrect. Streak set to 0.")

    print("You got 3 correct in a row! Game over.")

if __name__ == "__main__":
    main()
