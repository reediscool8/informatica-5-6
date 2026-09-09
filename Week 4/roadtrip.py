def main():
    answer = ""
    followup = ""

    while answer != "Yes!":
        answer = input("Are we there yet? ").strip().title()
        if answer == "Yes":
            followup = input("Really? ").strip().title()
        if followup == "Yes!":
            break


    print("We are here!")



if __name__ == "__main__":
    main()
