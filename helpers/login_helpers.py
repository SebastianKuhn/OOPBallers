import helpers.user_helpers as helpers
import hashlib

def hash_password(password):
    """
    input: password as a string
    :return hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    for i in range(0,3):
        name = str(input("Enter your username  "))
        if helpers.getUser(name) != None:
            break
        else:
            print("Something went wrong. Please try again.")

    for i in range(0,3):
        password = str(input("Enter your password  "))
        if helpers.getPassword(name) == hash_password(password):
            print("You have successfully logged in.")
            break

        else:
            print("Wrong Password, please try again.")
            continue

login()



