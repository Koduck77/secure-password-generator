import secrets
import string


def ask_question(message):
    while True:
        answer = input(message + " (y/n): ").lower()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter y or n.")


def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters = characters + string.ascii_uppercase
    if use_numbers:
        characters = characters + string.digits
    if use_symbols:
        characters = characters + "!@#$%^&*"

    password = ""

    for count in range(length):
        password = password + secrets.choice(characters)

    return password


def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Password length: "))

            if length < 4:
                print("Please choose a length of at least 4.")
            else:
                break
        except ValueError:
            print("Please enter a whole number.")

    use_uppercase = ask_question("Include uppercase letters?")
    use_numbers = ask_question("Include numbers?")
    use_symbols = ask_question("Include symbols?")

    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print("Your password is:", password)


if __name__ == "__main__":
    main()
