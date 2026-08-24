# Vulnerable Login Application
# This application contains intentional security weaknesses
# for the purpose of secure coding review.

USERNAME = "admin"
PASSWORD = "admin123"


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
    else:
        print("Login failed!")

    print("Debug Information:")
    print("Entered username:", username)
    print("Entered password:", password)


login()