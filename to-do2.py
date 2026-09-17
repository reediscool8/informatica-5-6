def main():
    tasks = []

while True:

    print(f"Tasks to-do: {len(tasks)} {tasks}")


    user_input = input("Enter task: ").strip()


    if user_input.lower() == "exit":
        break


    match = None
    for task in tasks:
        if task.lower() == user_input.lower():
            match = task
            break

    if match:

        choice = input(f"'{match}' found. Type 'u' to update, or press Enter to complete/remove: ").strip().lower()

        if choice == 'u':
            new_text = input("Enter the new text for this task: ").strip()
            if new_text:
                idx = tasks.index(match)
                tasks[idx] = new_text.upper()
                print("Task updated successfully.")
        else:
            tasks.remove(match)
            print(f"{match} completed. Task removed from your list.")
    else:

            tasks.append(user_input.upper())


if __name__ == "__main__":
    main()
