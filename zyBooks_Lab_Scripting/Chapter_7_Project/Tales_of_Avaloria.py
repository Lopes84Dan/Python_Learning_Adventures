import os

# Displays the starting menu of the game
def prompt():
    print(
        "\t\t\tWelcome to the world of Avaloria\n\n"
        "A mystical land steeped in ancient magic and rich with fantastical wonders. From enchanted forests to forgotten ruins, Avaloria is a realm where legends come to life, but now shrouded in darkness as the sinister grip of the demon lord threatens its very existence. "
        "You must collect all six items before encountering the Demon Lord.\n\n"
        "Moves:\t'go {direction}' (travel north, south, east, or west)\n"
        "\t'get {item}' (add nearby item to inventory)\n\n"
    )
    
    input("Press any key to continue.....")

# Clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Map
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

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

#List of valid directions
valid_directions = ["north", "south", "east", "west"]

# Track the current room
current_room = "Wizard's Tower"

# Result after making a move
message = ""

clear()
prompt()

# Game loop
while True:
    clear()

    # Displays information of the player
    print(f'You are currently in {current_room}\nInventory: {inventory}\n' + '-' * 27)

    # Display message
    print(message)

    # Item notification
    if 'Item' in rooms[current_room].keys():
        nearby_item = rooms[current_room]['Item']
        if nearby_item not in inventory:
            # Plural
            if nearby_item[-1] == 's':
                print(f'You see {nearby_item}')
            # Singular starts with vowel
            elif nearby_item[0] in vowels:
                print(f'You see an {nearby_item}')
            # Singular starts with consonant
            else:
                print(f'You see a {nearby_item}')

    if 'Boss' in rooms[current_room].keys():
        # Losing the game
        if len(inventory) < 6:
            print(f'You lost the battle with the {rooms[current_room]["Boss"]}.'
                  'You have succumbed to the overwhelming power of the Demon Lord. Avaloria now bends to his will, ruled by him and his relentless minions. Your efforts to thwart him have faltered, and as you fade into darkness, his echoing laughter resonates with your defeat.')
        # Winning the game
        else:
            print(f'You have defeated the {rooms[current_room]["Boss"]}.'
                  'You have triumphed over the overwhelming power of the Demon Lord. Avaloria is now free from his dark grip, and his minions scatter in defeat. Your courage and strength have prevailed, restoring light and hope to the realm as the echoes of victory drown out his fading cries.')
        break # End the game after boss encounter

   # Player's move
    user_input = input('Which direction would you like to head:\n')

    # Splits move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    if len(next_move) > 1:
        item = next_move[1]
        direction = next_move[1].title()
        item = ' '.join(item).title()

    # Moving between rooms
    if action == 'Go':
        try:
            current_room = rooms[current_room][direction]
            message = f'You traveled {direction}.'
        except KeyError:
            message = 'You are unable to move that direction.'
    

    # Picking up items
    if user_input.startswith('get '):
        item = user_input[4:].strip().title()

        try:
            if 'Item' in rooms[current_room] and rooms[current_room]['Item'].title() == item:
                if item not in inventory:
                    inventory.append(item)
                    print(f'You picked up the {item}.')
                else:
                    message = (f'You already have the {item}.')
            else:
                print(f'There is no {item} here to pick up.')
        except KeyError:
            print(f'There is no {item} here to pick up.')

   # Quit game
    elif user_input == 'exit':
        print('Thank you for playing Tales of Avaloria!')
        break

# Any invalid commands
else:
    print('Invalid Command')
