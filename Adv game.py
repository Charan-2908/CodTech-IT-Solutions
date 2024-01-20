import time

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself standing in front of a mysterious cave.")
    print("Do you want to enter the cave?")


def make_choice(options):
    while True:
        print("\nChoose an option:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choice = input("Enter the number of your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Invalid choice. Please enter a valid number.")


def explore_cave():
    print("\nYou enter the cave and see two tunnels.")
    time.sleep(1)
    print("To the left, there is a dark and narrow tunnel.")
    time.sleep(1)
    print("To the right, there is a well-lit tunnel with strange markings on the walls.")

    options = ["Enter the left tunnel", "Enter the right tunnel"]
    choice = make_choice(options)

    if choice == 1:
        return explore_dark_tunnel()
    else:
        return explore_lit_tunnel()


def explore_dark_tunnel():
    print("\nYou chose to enter the dark tunnel.")
    time.sleep(1)
    print("As you walk deeper, it becomes difficult to see.")
    time.sleep(1)
    print("Suddenly, you hear a growl. A pack of wolves is approaching!")

    options = ["Try to sneak past them", "Fight the wolves"]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou manage to sneak past the wolves and continue your journey.")
        return "Survived"
    else:
        print("\nThe wolves are too strong. Unfortunately, you didn't make it.")
        return "Game Over"


def explore_lit_tunnel():
    print("\nYou chose to enter the well-lit tunnel.")
    time.sleep(1)
    print("The tunnel leads to a room filled with treasure!")
    time.sleep(1)
    print("But wait, there is also a sleeping dragon guarding the treasure.")

    options = ["Attempt to take some treasure quietly", "Wake up the dragon"]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou successfully take some treasure and sneak away without waking the dragon.")
        return "Treasure Acquired"
    else:
        print("\nThe dragon wakes up in anger! It breathes fire, and you're toast.")
        return "Game Over"


def main():
    introduction()
    options = ["Enter the cave", "Leave"]
    choice = make_choice(options)

    if choice == 1:
        result = explore_cave()
        print("\nGame Result:", result)
    else:
        print("\nYou decide not to enter the cave. The adventure ends.")


if __name__ == "__main__":
    main()