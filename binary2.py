def main():
    print("Welcome")

    valid_bits = ["0","1"]
    while True:
        correct = 0
        binary_number = input("Endter your binary number: ")
        for char in binary_number:
            if char in valid_bits:
                correct += 1
        if correct == len(binary_number):
            break
        else:
            print("invalid input")

    binary_to_decimal(binary_number)

def binary_to_decimal(binary):
    decimal = 0
    for bit in binary:
        decimal = (decimal * 2) + int(bit)
    print(decimal)

if __name__ == "__main__":
    main()
