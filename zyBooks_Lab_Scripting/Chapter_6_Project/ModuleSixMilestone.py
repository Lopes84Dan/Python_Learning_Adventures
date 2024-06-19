# Daniel Lopez

rooms = {
    "Wizard's Tower" : {
        'North': 'Cursed Village',
        'South': 'Forgotten Library',
        'East': 'Abandonded Castle',
        'West': 'Enchanted Forest'
    },
    "Enchanted Forest" : {
        'East': "Wizard's Tower",
        'Item': 'Enchanted Wand'
    },
    "Cursed Village" : {
        'South': "Wizard's Tower",
        'East': 'Haunted Cemetery',
        'Item': 'Protective Amulet'
    },
    "Haunted Cemetery" : {
        'West': 'Cursed Village',
        'Item': 'Ghostly Lantern'
    },
    "Forgotten Library" : {
        'North': "Wizard's Tower",
        'East': 'Crystal Cave',
        'Item': 'Spell Book'
    },
    "Crystal Cave" : {
        'West': 'Forgotten Library',
        'Item': 'Crystal Orb'
    },
    "Abandonded Castle" : {
        'North': "Demon's Layer",
        'West': "Wizard's Tower",
        'Item': 'Magical Shield'
    },
    "Demon's Layer" : {
        'South': 'Abandonded Castle',
        'Boss': 'Demon Lord'
    }
}
current_room = "Wizard's Tower"

# Gameplay loop
while current_room != 'exit':
    # Current room
    print(f'You are in the {current_room}')

    # Get user input
    command = input('Which direction would you like to head: (go North, South, East, West or quit to exit the game): ').strip().lower()

    # Check commands
    if command == 'exit':
        current_room = 'exit'
        print('You are quiting the game.')
    elif command.startswith('go '):
        direction = command.split()[1]  # Get the direction from the input command
        if direction.capitalize() in rooms[current_room]:
            current_room = rooms[current_room][direction.capitalize()]
        else:
            print("Can't go in that direction!")
    else:
        print('Invalid command!')
        
# End of game loop
print('Thanks for playing!')