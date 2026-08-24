# Secure Login Application
# Improved version after security review

import getpass
import hashlib
import os

USERNAME = "admin"

# Salt and password hash for demonstration purposes
SALT = os.urandom(16)
PASSWORD_HASH = hashlib.pbkdf2_hmac(
    "sha256",
    b"StrongPassword@123",
    SALT,
    100000
)


def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    entered_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        SALT,
        100000
    )

    if username == USERNAME and entered_hash == PASSWORD_HASH:
        print("Login successful!")
    else:
        print("Login failed!")


login()
