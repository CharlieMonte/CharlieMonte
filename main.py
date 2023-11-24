import time
import random


class Player:
    def __init__(self, name='', inventory_items=[], location="jail"):
        self.name = name
        self.inventory_items = inventory_items
        self.location = location

    def __str__(self):
        return self.name, self.age, self.location


def ask_user():
    name = input("What is your name?: ")
    age = int(input("How old are you?: "))
    user = Player(name, age)
    return user


line_1 = "You are a detective who has been hired to investigate a series of mysterious disappearances in a small town. ".split()
line_2 = "You start your investigation by interviewing the locals and gathering clues. As you delve deeper into the case, ".split()
line_3 = "you discover that the disappearances are linked to a secret cult that has been operating in the town for years. ".split()
line_4 = "The cult is led by a charismatic leader. ".split()
line_5 = "You must use your detective skills to uncover the truth about the cult and stop them. ".split()
line_6 = "Along the way, you will encounter dangerous obstacles and challenging puzzles that will test your wit and courage. ".split()
lines_list = [line_1, line_2, line_3, line_4, line_5, line_6]


def print_introduction():
    for lines in lines_list:
        rand = random.randint(20, 23) / 100
        for i in range(len(lines)):
            print(lines[i], end=' ', flush=True)
            time.sleep(rand)
        print("")
    time.sleep(3)
    return ''


def print_commands():
    print("\nHere is a list of commands you may use throughout the game: ")
    time.sleep(1)
    print("'Help' – displays hints, descriptions about the game and valid commands.")
    print("'Pickup' – player attempts to pick up the item in the location assuming the item is not too heavy.")
    print("'Drop' – drop the requested item into the current location. Player must be holding the item.")
    print("'Eat' – eat the requested item. Player must be holding the edible item.")
    print("'Look' – displays a long description of the current location")
    print("'List' – displays all items currently held by the player.")
    print("'Go' [direction] – attempt to move from the current location in the requested direction.")
    print("'Hold' [item] – inserts [item] into your hand.")
    print("'Sleep' – sleeps through the night.")
    print("'Time' – display the current time of day.")
    print("'Inspect' [person, item, or place] - gives a brief description about what you are inspecting.")
    print("'Navigate' [Current Location] [Destination] - returns a route to the desired destination from the current location.")
    print("Try using a command \n")


def help():
    print("help")


def pickup():
    print("pickup")


def drop(entry=''):
    print("drop")


def eat(entry=''):
    print("eat")


def look():

    if player.self.location == "home":
        print("Your home")
    print("look")


def list_inventory():
    print("list")

def go(location, direction):
    if location == "home":
        if direction == "north":
            return "library"
        else:
            print(f'{direction} is not an available option from your current location.')
            return location
    elif location == "library":
        if direction == "north":
            return "jail"
        elif direction == "northeast":
            return "town square"
        elif direction == "south":
            return "home"
        else:
            print(f'{direction} is not an available option from your current location.')
            return location
    elif location == "jail":
        if direction == "east":
            return "town square"
        elif direction == "south":
            return "library"
        else:
            print(f'{direction} is not an available option from your current location.')
            return location
    elif location == "town square":
        if direction == "north":
            return "arcade"
        elif direction == "northeast":
            return "steakhouse"
        elif direction == "southeast":
            return "cemetery"
        elif direction == "southwest":
            return "library"
        elif direction == "west":
            return "jail"
        else:
            print(f'{direction} is not an available option from your current location.')
            return location
    elif location == "cemetery":
        if direction == "northwest":
            return "town square"
        else:
            print(f'{direction} is not an available option from your current location.')
            return location
    elif location == "steakhouse":
        if direction == "southwest":
            return "town square"
        else:
            print(f'{direction} is not an available option from your current location.')
            return location
    elif location == "arcade":
        if direction == "north":
            return "abandoned house"
        elif direction == "south":
            return "town square"
        else:
            print(f'{direction} is not an available option from your current location.')
            return location
    elif location == "abandoned house":
        if direction == "south":
            return "arcade"
        else:
            print(f'{direction} is not an available option from your current location.')
            return location
    else:
        print("Location Error")
        print(location, direction)


def hold(entry=''):
    print("hold")


def inspect(entry=''):
    if 'cookie' in entry:
        print("Looks like ... ", end='')
        time.sleep(0) #1.25
        print("a soft chocolate chip cookie")


def prompt_user():
    user_input = input().lower()
    return user_input


def navigate(location, destination):
    if location == "home":
        if destination == "library":
            return print(f'North')
        elif destination == "jail":
            return print(f'North, North')
        elif destination == "town square":
            return print(f'North, Northeast')
        elif destination == "cemetery":
            return print(f'North, Northeast, SouthEast')
        elif destination == "steakhouse":
            return print(f'North, Northeast, SouthEast')
        elif destination == "arcade":
            return print(f'North, Northeast, North')
        elif destination == "abandoned house":
            return print(f'North, North, Northeast, North, North')
    elif location == "library":
        if destination == "home":
            return print(f'South')
        elif destination == "jail":
            return print(f'North')
        elif destination == "town square":
            return print(f'Northeast')
        elif destination == "cemetery":
            return print(f'Northeast, SouthEast')
        elif destination == "steakhouse":
            return print(f'Northeast, Northeast')
        elif destination == "arcade":
            return print(f'Northeast, North')
        elif destination == "abandoned house":
            return print(f'Northeast, North, North')
    elif location == "jail":
        if destination == "home":
            return print(f'South, South')
        elif destination == "library":
            return print(f'South')
        elif destination == "town square":
            return print(f'East')
        elif destination == "cemetery":
            return print(f'East, SouthEast')
        elif destination == "steakhouse":
            return print(f'East, NorthEast')
        elif destination == "arcade":
            return print(f'East, North')
        elif destination == "abandoned house":
            return print(f'East, North, North')
    elif location == "town square":
        if destination == "home":
            return print(f'Southwest, South')
        elif destination == "library":
            return print(f'SouthWest')
        elif destination == "jail":
            return print(f'West')
        elif destination == "cemetery":
            return print(f'SouthEast')
        elif destination == "steakhouse":
            return print(f'Northeast')
        elif destination == "arcade":
            return print(f'North')
        elif destination == "abandoned house":
            return print(f'North, North')
    elif location == "cemetery":
        if destination == "home":
            return print(f'NorthWest, SouthWest, South')
        elif destination == "library":
            return print(f'NorthWest, SouthEast')
        elif destination == "jail":
            return print(f'NorthWest, West')
        elif destination == "town square":
            return print(f'NorthWest')
        elif destination == "steakhouse":
            return print(f'NorthWest, NorthEast')
        elif destination == "arcade":
            return print(f'NorthWest, North')
        elif destination == "abandoned house":
            return print(f'NorthWest, North, North')
    elif location == "steakhouse":
        if destination == "home":
            return print(f'SouthWest, SouthWest, South')
        elif destination == "library":
            return print(f'SouthWest, SouthWest')
        elif destination == "jail":
            return print(f'SouthWest, West')
        elif destination == "town square":
            return print(f'SouthWest')
        elif destination == "cemetery":
            return print(f'SouthWest, SouthEast')
        elif destination == "arcade":
            return print(f'SouthWest, North')
        elif destination == "abandoned house":
            return print(f'SouthWest, North, North')
    elif location == "arcade":
        if destination == "home":
            return print(f'South, SouthWest, South')
        elif destination == "library":
            return print(f'South, SouthWest')
        elif destination == "jail":
            return print(f'South, West')
        elif destination == "town square":
            return print(f'South')
        elif destination == "cemetery":
            return print(f'South, SouthEast')
        elif destination == "steakhouse":
            return print(f'South, NorthEast')
        elif destination == "abandoned house":
            return print(f'North')
    elif location == "abandoned house":
        if destination == "home":
            return print(f'South, South, SouthWest, South')
        elif destination == "library":
            return print(f'South, South, SouthWest')
        elif destination == "jail":
            return print(f'South, South, West')
        elif destination == "town square":
            return print(f'South. South')
        elif destination == "cemetery":
            return print(f'South, South, SouthEast')
        elif destination == "steakhouse":
            return print(f'South, South, NorthEast')
        elif destination == "arcade":
            return print(f'South')
    else:
        return print(f'Your desired destination does not exist.'), location


def check_command(user_input, location):
    if "help" in user_input:
        help()
    elif "pickup" in user_input:
        pickup()
    elif "drop" in user_input:
        drop()
    elif "eat" in user_input:
        eat(hand)
    elif "look" in user_input:
        look()
    elif "list" in user_input:
        list_inventory()
    elif "go" in user_input:
        location = go(location, user_input.split()[1])
        print(f'You are now at {location}')
        return location
    elif "hold" in user_input:
        hold(user_input.split()[1])
    elif "inspect" in user_input:
        inspect(hand)
    elif "navigate" in user_input:
        location = input("Where are you coming from?: ").lower()
        destination = input("Where are you going?: ").lower()
        navigate(location, destination)
    elif "get" in user_input:
        print(location)
    else:
        pass


def main():
#    print_introduction()
#    print_commands()
    returns = check_command(prompt_user(), "jail")
    while True:
        returns = check_command(prompt_user(), returns)



if __name__ == '__main__':
    main()
