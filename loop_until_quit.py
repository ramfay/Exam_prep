"""
This program gets a user's name. The user can then enter a new name, or have the existing name printed in
upper/lowercase. A nice happy message is displayed on quit.
"""

name = str(input("Enter your name: "))
menu = "(G)et new name" \
       "\n(U)ppercase" \
       "\n(L)owercase" \
       "\n(Q)"
print(menu)
menu_choice = str(input("> ")).upper()
while menu_choice != "Q":
    if menu_choice == "G":
        name = str(input("Enter your name: "))
    elif menu_choice == "U":
        print(name.upper())
    elif menu_choice == "L":
        print(name.lower())
    else:
        print("Please pick a valid menu option")
    print(menu)
    menu_choice = str(input("> ")).upper()
print("Have a nice day!")
