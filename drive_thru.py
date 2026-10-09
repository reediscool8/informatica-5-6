def main():

    welcome()
    choice = int(input("Select your order: "))
    get_item(choice)

def welcome():
    menu = ["Cheeseburger","Fries", "Soda", "Ice Cream", "Cookie"]
    print("Welcome to Los Pollos Hermanos")
    print("Menu")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

def get_item(order):
    # if order == 1:
    #     print("🍔")
    # elif order == 2:
    #     print("🍟")
    # elif order == 3:
    #     print("🥤")
    # elif order == 4:
    #     print("🍦")
    # elif order == 5:
    #     print("🍪")
    kitchen = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    if 1 <= order <= 5:
        print(kitchen[order - 1])
    else:
        print("Learn to read")

if __name__ == "__main__":
    main()
