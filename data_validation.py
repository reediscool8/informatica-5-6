def main():
    not_validated = True
    while not_validated:

        try:

            number = int(input("Enter a number between 1 and 10: "))
            if number >= 1:
                if number <= 10:
                    print("Number stored successfully. ")
                    not_validated = False
            else:
                print("A number 1 through 10!")


        except ValueError:
            print("Enter a number!")

if __name__ == "__main__":
    main()
