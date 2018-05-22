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
                print("")
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

    #gets the user's id and creates a user object
    try:
        user_id = int(helpers.getCurrentUserId(username)[0])
        user = User(name, hashed_pw, vegetarian, user_id)
    except Exception:
        user = User(name, hashed_pw, vegetarian)
        print("oops something went wrong with fetching the user id")


    return user
