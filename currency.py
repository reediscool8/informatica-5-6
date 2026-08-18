def main():

    p = int(input("What do you have left in pesos? "))
    s = int(input("What do you have left in soles? "))
    r = int(input("What do you have left in reais? "))

    U = (p * .00032) + (s * .30) + (r * .19)
    M = (p * .0054) + (s / 5.07) + (r / 3.28)

    print("USD:", U)
    print("MXN:", M)

if __name__ == "__main__":
    main()
