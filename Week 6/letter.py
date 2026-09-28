def main():

    invites = ("Mario", "Luigi", "Daisy", "Yoshi", "Toad", "Bowser", "Princesess Peach")
    for receiver in invites:
        if receiver != "Princess Peach":


            print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {invites [6]}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        """)


if __name__ == "__main__":
    main()
