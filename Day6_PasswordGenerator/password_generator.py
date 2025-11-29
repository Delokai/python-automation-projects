import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6.")
        return None

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        result = generate_password(length)
        if result:
            print("\nYour generated password:")
            print(result)
    except ValueError:
        print("Please enter a valid number.")
