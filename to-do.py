def main():
    list = []
    while True:
        print(f"You have {len(list)} tasks to do.")
        print(list)
        command = input("What do you want to do? (add, complete or end): ").upper()
        if command == "ADD":
            tasks = input("Enter new task: ").upper()
            list.append(tasks)
            print(list)

        elif command == "COMPLETE":
            remove = input("What would you like to remove? ").upper()
            list.remove(remove)
            print(list)

        else:
            break







if __name__ == "__main__":
    main()
