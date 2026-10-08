def main():

    welcome()
    choice = int(input("Select your order: "))
    get_item(choice)

def welcome():
    menu = ["Cheeseburger","Fries", "Soda", "Ice Cream", "Cookie"]
    print("Welcome to Los Pollos Hermanos")
    print("Menu")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

def get_item(order):
    # if order == 1:
    #     print("🍔")
    # elif order == 2:
    #     print("🍟")
    # elif order == 3:
    #     print("🥤")
    # elif order == 4:
    #     print("🍦")
    # elif order == 5:
    #     print("🍪")
    kitchen = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    if 1 <= order <= 5:
        print(kitchen[order - 1])
    else:
        print("Learn to read")

if __name__ == "__main__":
    main()





def main():
    binary = input("Enter a binary number: ")
    binary_to_decimal(binary)


def binary_to_decimal(binary):
    valid = True

    # Check if input contains non-binary characters
    for digit in binary:
        if digit != "0" and digit != "1":
            valid = False

    if valid == True:
        # Convert binary to decimal
        decimal = 0
        power = len(binary) - 1

        for digit in binary:
            if digit == "1":
                decimal = decimal + (2**power)
            power = power - 1

        print(f"Decimal equivalent: {decimal}")
    else:
        print("Invalid input! Only 0s and 1s allowed.")


if __name__ == "__main__":
    main()




def main():
    binary = input("Enter a binary number: ")
    binary_to_decimal(binary)


def binary_to_decimal(binary):
    decimal = 0
    is_binary = 1

    for digit in binary:
        if digit == "0":
            decimal = decimal * 2 + 0
        elif digit == "1":
            decimal = decimal * 2 + 1
        else:
            is_binary = 0

    if is_binary == 1:
        print(f"Decimal equivalent: {decimal}")
    else:
        print("Invalid input! Only 0s and 1s allowed.")


if __name__ == "__main__":
    main()
