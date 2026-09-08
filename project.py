import random

def main():
    print("=================================")
    print("      DID I PACK EVERYTHING?     ")
    print("=================================")

    items = ["Phone", "Backpack", "Homework", "Water", "Keys"]

    print()
    print("You are getting ready to leave!")
    print("Let's make sure you have everything.")
    print()

    while items:
        print("Items you still need:")
        print("- " + "\n- ".join(items))
        print()

        choice = input("What did you pack? ").strip().title()
        print()

        if choice in items:
            items.remove(choice)
            print("✅", choice, "is packed!")
        elif choice == "":
            print("❌ Please enter an item name.")
        else:
            print("❌ That is not on your list or already packed.")

        print()

    print("=================================")
    print("     🎉 EVERYTHING IS PACKED!    ")
    print("       You are ready to go!      ")
    print("=================================")

if __name__ == "__main__":
    main()
