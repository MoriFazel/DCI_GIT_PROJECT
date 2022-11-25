"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE
print(" *Ivan and mori Warehouse Management System* ")
# Get the user name
name = input("please enter you name, dear kunde")

# Greet the user
print("Hi,", name, '\n' "Welcome to the MWMS")
# Show the menu and ask to pick a choice
print(f"from the menu below, please select and option to proceed further: \n 1. show all available items of both warehouses, \n 2. search among items for checking their availability \n 3. quit")
menu_selection= int(input("please enter 1, 2 or 3 for the desired menu number"))

# If they pick 1
while menu_selection:
    if menu_selection == 1:
        print(f"{warehouse1}{warehouse2}")
    # Else, if they pick 2
    elif menu_selection == 2:
        print('2 selected')
    # Else, if they pick 3
    elif menu_selection == 3:
        print('3 selected')
    # Else
    else:
        print

# Thank the user for the visit


