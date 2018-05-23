"""
In this file all functions to add users to the database are saved.
"""

import helpers.db_helpers as helpers

def newUser(user):
    """
    Inserts new user into database
    :param name: type string
    :param hashed_password: string will be hashed in main.py before being saved into db.
    :param vegetarian: boolean
    :return:
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    userInsertQuery = "INSERT into users (username, password, vegetarian) VALUES (%s, %s, %s)"
    try:
        cursor.execute(userInsertQuery, (user.username, user.hashed_password, user.vegetarian_status)) # to replace s% put in quotation markes
        db.commit()
    except Exception:
        return 'Error: OOPs something went wrong!'

    finally:
        cursor.close()
        db.close()

def getAllUsers():
    """
    Display the whole users table
    :return: all usernames that are currently in the database
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    getUsersQuery = "SELECT * FROM users"
    try:
        cursor.execute(getUsersQuery)
        info = cursor.fetchall() # print results
        return info
    except Exception:
        return "Error: OOPs something went wrong!"
    finally:
        cursor.close()
        db.close()


def getAllUsernames():
    """
    Display all usernames from the users table.
    :return:
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    getAllUsernames = "SELECT username FROM users"
    try:
        cursor.execute(getAllUsernames)
        info = cursor.fetchall()
        resp = []
        for i in info:
            resp.append(i[0])
        return resp
    except Exception:
        return "Oh Snap, this didn't work!"
    finally:
        cursor.close()
        db.close()

def getUser(name):
    """
    Search user by his username and return the username.
    Function is used to check if a username already exists in the database.
    :param username:
    :return: username
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    getuser = "SELECT username FROM users WHERE username=%s"
    try:
        cursor.execute(getuser, (name,))
        info = cursor.fetchone()
        return info[0]
    except Exception:
        return None
    finally:
        cursor.close()
        db.close()

def getPassword(name):
    db = helpers.getDbCon()
    cursor = db.cursor()
    getpassword = "SELECT password FROM users WHERE username=%s"
    try:
        cursor.execute(getpassword, (name,))
        info = cursor.fetchone()
        return info[0]
    except Exception:
        return "Oh Snap, this didn't work!"
    finally:
        cursor.close()
        db.close()

def getVegetarianStatus(name):
    """
    This function will return if a user searched with his username is vegetarian.
    :param username:
    :return:
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    getVegetarian = "SELECT vegetarian FROM users WHERE username=%s"
    try:
        cursor.execute(getVegetarian, (name,))
        info = cursor.fetchone()
        return info[0]
    except Exception:
        return "Oh Snap, this didn't work!"
    finally:
        cursor.close()
        db.close()

def deleteUser(user):
    """
    This function will delete a user from the database and say if the user has not been found in the database.
    :param username:
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    #dirtydirtycoding
    deleteUserQuery = "SET FOREIGN_KEY_CHECKS=0; DELETE FROM users WHERE user_id=%s; SET FOREIGN_KEY_CHECKS=1;"
    #try:
    cursor.execute(deleteUserQuery, (user.user_id,))
    info = cursor.fetchall()
    db.commit()

    if info == 0:
        print("No such user found")
    else:
        print("You deleted the user: " + user.usernname)
    return info
    #except Exception:
    #return "Oh Snap, this didn't work!"
    #finally:
    cursor.close()
    db.close()

def getCurrentUserId(name):
    """
    This function is used to put the user with the corresponding recipes in table matching the latter two.
    :param username:
    :return: 1 or 0
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    userIdQuery = "SELECT user_id FROM users WHERE username = %s;"
    try:
        cursor.execute(userIdQuery, (name,))
        user_id = cursor.fetchone()
        return user_id
    except Exception:
        return "Oh Snap, this didn't work!"
    finally:
        cursor.close()
        db.close()


def unsafeGetUsername(name):
    """
    This unsafe function is created for learning purposes.
    We tried to inject our database.
    :param username:
    :return: username
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    if "drop" in str(name).lower() or "delete" in str(name).lower():
        print("Please don't do it Ruben!")
        return
        print("SHOULDNT SHOW")
    fail = "SELECT username FROM users WHERE username=%s" % (name)
    cursor.execute(fail)
    for row in cursor.fetchall():
        print(row)
    return cursor.fetchall()
    cursor.close()
    db.close()
