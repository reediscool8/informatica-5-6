def main():
    def highest(a, b):
        if a > b:
            highest_num = a
        else:
               highest_num = b
               print(f"The highest number is {highest_num}")
    highest(8,2)

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    highest(num1, num2)

    def lowest(a, b, c):
        if a > b and c > b:
            lowest_number = b
        elif a > c and b > c:
             lowest_number = c
        else:
             lowest_number = a
        print(f"The lowest number is {lowest_number}")
    num3 = float(input("Enter first number: "))
    num4 = float(input("Enter second number: "))
    num5 = float(input("Enter third number: "))
    lowest(num3, num4, num5)

if __name__ == "__main__":
    main()
