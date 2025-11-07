food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.

food = sorted([item for item in food.split(',')])
equipment = sorted([item for item in equipment.split(',')])
pets = sorted([item for item in pets.split(',')])
sleep_aids = sorted([item for item in sleep_aids.split(',')])

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = [food, equipment, pets, sleep_aids]

print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

# d) Use bracket notation and format to display the contents of the selected cabinet.
# If the user entered an invalid number, print an error message.

# while True:
#     user_input = int(input('Select a number from 0-3, each one represents a cabinet: (9700 ends loop)'))
#     if user_input == 0:
#         print(f'food: {cargo_hold[0]}')
#     elif user_input == 1:
#         print(f'equipment: {cargo_hold[1]}')
#     elif user_input == 2:
#         print(f'pets: {cargo_hold[2]}')
#     elif user_input == 3:
#         print(f'sleep aids: {cargo_hold[3]}')
#     elif user_input == 9700:
#         break
#     else:
#         print('enter a valid number')


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item.
# Use the in method to check if the cabinet contains the selected item,
# then print “Cabinet ____ DOES/DOES NOT contain ____.”

while True:
    user_input = int(input(f'Select a number from 0-3, 0: food, 1: equipment, 2: pets, 3: sleep aids, 9700: ends program)'))
    item_check = str(input(f'Pick an item why not: '))
    if user_input == 0:
        if item_check in cargo_hold[0]:
            print(f'Cabinet food DOES contain {item_check}.')
        else:
            print(f'Cabinet food DOES NOT contain {item_check}.')
    elif user_input == 1:
        if item_check in cargo_hold[1]:
            print(f'Cabinet equipment DOES contain {item_check}.')
        else:
            print(f'Cabinet equipment DOES NOT contain {item_check}.')
    elif user_input == 2:
        if item_check in cargo_hold[2]:
            print(f'Cabinet pets DOES contain {item_check}.')
        else:
            print(f'Cabinet pets DOES NOT contain {item_check}.')
    elif user_input == 3:
        if item_check in cargo_hold[3]:
            print(f'Cabinet sleep aids DOES contain {item_check}.')
        else:
            print(f'Cabinet sleep aids DOES NOT contain {item_check}.')
    elif user_input == 9700:
        break
    else:
        print('enter a valid number or double check the second thing')