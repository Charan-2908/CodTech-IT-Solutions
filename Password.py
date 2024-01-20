import random
import string

def generate_password(length, complexity):
    if length == 0:
        return "Your length of password should be greater than zero."

    if complexity == "low":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level. Please choose 'low', 'medium', or 'high'."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator")

    # User input for password length
    length = int(
        input("Enter the desired length of the password (enter 0 to skip): "))

    # If the length is 0, this message will be displayed
    if length == 0:
        print("Your length of password should be greater than zero.")
        return

    # User input for password complexity
    complexity = input(
        "Enter the desired complexity level ('low', 'medium', or 'high'): ").lower()

    # Generate and display the password
    password = generate_password(length, complexity)
    print("Generated Password:", password)


if __name__ == "__main__":
    main()