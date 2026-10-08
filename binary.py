def main():
    print("The purpose of this program is to convert binary numbers into normal ones that people can understand")
    print()
    binary = float(input("Enter binary number: "))

def binary_to_decimal():
    good = True
    if digit in binary:
        if digit != 0 and digit != 1:
            valid = False

    if valid == True:
        decimal = 0
        power = len(binary) - 1

        for digit in binary:
            if digit == 1:
                decimal = decimal + (2**power)
            power = power
            print(f"Decimal number {decimal}")
    else:
        print("bad boy only binary")



if __name__ == "__main__":
    main()
