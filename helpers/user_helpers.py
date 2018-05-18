import helpers.db_helpers as helpers


def newUser(name, hashed_password, vegetarian):
    db = helpers.getDbCon()
    cursor = db.cursor()
    userInsertQuery = "INSERT into users (username, password, vegetarian) VALUES (%s, %s, %s)"
    try:
        cursor.execute(userInsertQuery, (name, hashed_password, vegetarian)) # to replace s% put in quotation markes
        db.commit()
    except Exception:
        return 'Error: OOPs something went wrong!'

    finally:
        cursor.close()
        db.close()

def getAllUsers():
    """
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


def deleteUser(name):
    """
    this function will delete a user from the database and say if the user has not been found in the database.
    :param name:
    :return:
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    deleteUser = "DELETE FROM users WHERE username=%s"
    try:
        info = cursor.execute(deleteUser, (name,))
        db.commit()
        if info == 0:
            print("No such user found")
        else:
            print("You deleted the user: " + name)
        return info
    except Exception:
        return "Oh Snap, this didn't work!"
    finally:
        cursor.close()
        db.close()

def getCurrentUserId(name):
    """
    This function is used to put the user with the corresponding recipes in table matching the latter two.
    :param name:
    :return:
    """
    db = helpers.getDbCon()
    cursor = db.cursor()
    userIdQuery = "SELECT user_id FROM users WHERE username = %s"
    try:
        cursor.execute(userIdQuery, (name,))
        user_id = cursor.fetchone()
        return user_id
    except Exception:
        return "Oh Snap, this didn't work!"
    finally:
        cursor.close()
        db.close()