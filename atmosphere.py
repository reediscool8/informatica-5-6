def main():

    layer = input("Descent atmosphere layer:  ")
    if layer == "Exosphere":
        print("Your altitude level will be between 700-10000 km")
    elif layer == "Thermosphere":
        print("Your altitude level will be between 85-700 km")
    elif layer == "Mesosphere":
        print("Your altitude level will be between 50-85 km")
    elif layer == "Stratosphere":
        print("Your altitude level will be between 12-50 km")
    elif layer == "Troposphere":
        print("Your altitude level will be between 0-12 km")
    else:
        print("Check your spelling")


    altitude = float(input("Enter exact altitude"))

    if altitude > 10000:
        time = 4650 + 1230 + 175 + 506.7 + 600
    elif altitude > 700:
        time = (((altitude - 700) / 2) + 1230 + 175 + 506.7 + 600)








if __name__ == "__main__":
    main()


