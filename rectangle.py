def main():
    width = int(input("Enter the width of the rectangle: "))
    print("O" * width)
    print("O" * width)
    print("O" * width)
    print("O" * width)
    print("O" * width)

    p = (width * 2)+(5 * 2)
    print("Perimeter:", p)

    a = (5 * width)
    print("Area:", a)

    d = ((width*width + 5*5)**.5)
    print("Diagonal:", d)

if __name__ == "__main__":
        main()
