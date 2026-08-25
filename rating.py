def main():
    print("Krusty Crab")
    rating  = int(input("Please rate 0-5:  "))

    if rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excelent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    else:
        print("Poor")

    print("Thank you for your feedback on the Krusty Crab")



if __name__ == "__main__":
    main()

