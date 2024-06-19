# Daniel Lopez

rooms = {
    "Wizard's Tower": {
        'North': 'Cursed Village',
        'South': 'Forgotten Library',
        'East': 'Abandonded Castle',
        'West': 'Enchanted Forest'
    },
    "Enchanted Forest": {
        'East': "Wizard's Tower"
    },
    "Cursed Village": {
        'South': "Wizard's Tower",
        'East': 'Haunted Cemetery'
    },
    "Haunted Cemetery": {
        'West': 'Cursed Village'
    },
    "Forgotten Library": {
        'North': "Wizard's Tower",
        'East': 'Crystal Cave'
    },
    "Crystal Cave": {
        'West': 'Forgotten Library'
    },
    "Abandonded Castle": {
        'North': "Demon's Layer",
        'West': "Wizard's Tower"
    },
    "Demon's Layer": {
        'South': 'Abandonded Castle',
        'Boss': 'Demon Lord'
    }
}

valid_directions = ["north", "south", "east", "west"]

current_room = "Wizard's Tower"

# Gameplay loop
while current_room != 'exit':
    # Current room
    print(f'You are in the {current_room}')

    # Get user input
    user_input = input('Which direction would you like to head:\n').lower()

    # Splits move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    if len(next_move) > 1:
        direction = next_move[1].title()

    # Check for invalid command here
    words = user_input.split()
    if len(words) != 2 or words[0] != "go" or words[1] not in valid_directions:
        print("Invalid command. Please enter 'go' followed by a valid direction.")

    # Moving between rooms
    if action == 'Go':
        try:
            current_room = rooms[current_room][direction]
            message = f'You traveled {direction}.'
        except KeyError:
            message = 'You are unable to move that direction.'

    # Check for exit
    if user_input == 'exit':
        print('End of game!')
        break
