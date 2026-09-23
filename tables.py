
def main():
  def main():
    while True:
        user_input = input("Enter a number (1-10): ")

        try:
            num = int(user_input)
            if 1 <= num <= 10:
                print(f"\nHere is the {num} times table:")
                for i in range(1, 11):
                    result = i * num
                    print(f"{i} times {num} is {result}")
                break  # Stops the loop after successfully printing the table
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()


