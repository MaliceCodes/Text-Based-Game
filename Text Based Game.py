def print_instructions():
    print('**Alternate Reality Escape Game**')
    print('You are trapped inside an alternate reality\nand are being hunted by an evil entity.')
    print('Find a Key and escape, or die by the entity.')
    print('Optional: Find a knife and kill the entity.')
    print('Move Commands: "Go North", "Go South", "Go East", "Go West"\nTake item command: "Take (item)"')
    input('Press "Enter" to continue. Type "Exit" at anytime to quit.')


rooms = {'Bathroom': {'name': 'Bathroom', 'South': 'Laundry Room', 'East': 'Bedroom', 'North': 'Living Room'},
         'Bedroom': {'name': 'Bedroom', 'West': 'Bathroom', 'item': 'Hoodie'},
         'Dining Room': {'name': 'Dining Room', 'North': 'Kitchen', 'item': 'Food'},
         'Kitchen': {'name': 'Kitchen', 'East': 'Living Room', 'South': 'Dining Room', 'item': 'Knife'},
         'Living Room': {'name': 'Living Room', 'North': 'Office', 'South': 'Bathroom', 'East': 'Family Room',
                         'West': 'Kitchen', 'item': 'Flashlight'},
         'Office': {'name': 'Office', 'South': 'Living Room', 'East': 'Guest Room', 'Villain': 'Entity'},
         'Guest Room': {'name': 'Guest Room', 'West': 'Office', 'South': 'Family Room', 'item': 'Key'},
         'Family Room': {'name': 'Family Room', 'North': 'Guest Room', 'West': 'Living Room'},
         'Laundry Room': {'name': 'Laundry Room', 'North': 'Bathroom', 'item': 'Note'},
         }



inventory = []
current_room = 'Bathroom'
message = ''
note = ("You may be wondering where you are right now.\nYou're in an alternate universe."
        " The 'friend' that you know is not the same one.\nYou must find a way to escape or kill the entity.")

print_instructions()

while True:

    print(f"\nYou are in the {current_room}\nInventory : {inventory}\n{'-' * 27}")
    print(message)

    if "item" in rooms[current_room].keys():
        room_items = rooms[current_room]['item']

        if room_items not in inventory:
            print(f'You see a {room_items}.\nDo you take it\nor continue on? ')

        else:
            print('There are no items in this room.')

    if 'Villain' in rooms[current_room].keys():

        if 'Knife' in inventory:
            print(f"You killed the {rooms[current_room]['Villain']} and must now escape!")

        else:
            print(f'The {rooms[current_room]["Villain"]} is too strong\nand you were killed. Try Again.')
            break

    if 'item' in rooms[current_room].keys():

        if 'Key' in inventory:
            print("You found the Key and can now\nescape through the Family Room!")

    if 'Key' in inventory:
        if current_room == 'Family Room':
            print('You have escaped! Congratulations!')
            break

    if 'Note' in inventory:
        if user_input == 'Read Note':
            print(note)

    user_input = input('Where do you go? ')

    next_move = user_input.split(' ')

    action = next_move[0].title()

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = ' '.join(item).title()

    if action == 'Go':
        try:
            current_room = rooms[current_room][direction]
            message = f'You went {direction}'

        except:
            message = 'You cannot go that way.'

    elif action == 'Take':

        try:
            if item == rooms[current_room]['item']:

                if item not in inventory:
                    inventory.append(rooms[current_room]['item'])
                    message = 'Item Acquired'

                else:
                    message = f'You already have the {item}'
            else:
                message = f'Cannot find item'
        except:
            message = f'Cannot find {item}'
    elif action == 'Exit':
        print('Thanks For Playing.')
        break
    else:
        message = 'Invalid Command'
