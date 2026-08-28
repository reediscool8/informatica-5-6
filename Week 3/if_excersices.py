def main():
    one = float(input("Please input one number: "))
    two = float(input("Please input second number: "))
    sign = input("Please input operation: ")

    if sign == "+":
        plus = (one + two)
        print(plus)
    elif sign == "-":
        minus = (one - two)
        print(minus)
    elif sign == "*":
        times = (one * two)
        print(times)
    elif sign == "/":
        division = (one / two)
        print(division)
    else:
        print("Syntax Error")

if __name__ == "__main__":
    main()




