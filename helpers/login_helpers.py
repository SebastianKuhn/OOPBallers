"""
This file contains all functions to log in users.
"""

import helpers.user_helpers as helpers
from Models.user import User
import hashlib

def hash_password(password):
    """
    This function hashes a password.

    input: password as a string
    :return hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()


def login():
    """
    This function asks the user for a username and a password which both will be checked in the database in order
    to login.
    input: -
    :return -
    """

    while True:

        while True:
            name = str(input("Enter your username  "))

            username = helpers.getUser(name)

            if username is not None:
                break
            else:
                print("Something went wrong. Please try again.")
                print("")

        while True:
            password = str(input("Enter your password  "))
            hashed_pw = helpers.getPassword(name)
            if hashed_pw == hash_password(password):
                print("You have successfully logged in.")
                print("")
                break
            else:
                print("Wrong Password, please try again.")
                print("")
                continue

        break

    #gets the vegetarian status of the user
    if helpers.getVegetarianStatus(name) == 0:
        vegetarian = False
    else:
        vegetarian = True

    #creates a user which will be returned
    user = User(name, hashed_pw, vegetarian)

    return user
