import hashlib
import MySQLdb # pip install mysql-client or something else
# Add new song into songs table
# used by chart crawlers
from configparser import ConfigParser
import helpers.db_helpers as helpers

def newUser(name, hashedpw, vegetarian):
    db = helpers.getDbCon()
    cursor = db.cursor()

    userInsertQuery = "INSERT into users (username, password, vegetarian) VALUES (%s, %s, %s)"
    try:
        cursor.execute(userInsertQuery, (name, hashedpw, vegetarian)) # to replace s% put in quotation markes
        db.commit()
    except Exception:
        return 'Error: unable to execute!'

    finally:
        cursor.close()
        db.close()


<<<<<<< HEAD
def newUser(name, hashed_password, vegetarian):
    db = helpers.getDbCon()
    cursor = db.cursor()
    userInsertQuery = "INSERT into users (username, password, vegetarian) VALUES (%s, %s, %s)"
    # try:
    cursor.execute(userInsertQuery, (name, hashed_password, vegetarian)) # to replace s% put in quotation markes
    db.commit()
    print("Successfully added " + name)


||||||| merged common ancestors
def newUser(name, hashed_password, vegetarian):
    db = helpers.getDbCon()
    cursor = db.cursor()
    userInsertQuery = "INSERT into users (username, password, vegetarian) VALUES (%s, %s, %s)"
    # try:
    cursor.execute(userInsertQuery, (name, hashed_password, vegetarian)) # to replace s% put in quotation markes

        cursor.execute(userInsertQuery, (name, pw, vegetarian)) # to replace s% put in quotation markes

    db.commit()
    print("Successfully added " + name)


=======
>>>>>>> 1575d92be1abad2ca2e206819484ab4cb7881f5c
def getAllUsers():
    db = helpers.getDbCon()
    cursor = db.cursor()
    getUsersQuery = "SELECT * FROM users"
    cursor.execute(getUsersQuery)
    info = cursor.fetchall() # print results
    print(info)
    return info

def getAllUsernames():
    db = helpers.getDbCon()
    cursor = db.cursor()
    getAllUsernames = "SELECT username FROM users"
    cursor.execute(getAllUsernames)
    info = cursor.fetchall()
    resp = []
    for i in info:
        resp.append(i[0])
    return resp


def getPassword(name):
    db = helpers.getDbCon()
    cursor = db.cursor()
    getpassword = "SELECT password FROM users WHERE username=%s"
    # try:
    cursor.execute(getpassword, (name,))
    info = cursor.fetchone()
    print(info[0])
    return info[0]


def deleteUser(name):
    db = helpers.getDbCon()
    cursor = db.cursor()
    deleteuser = "DELETE FROM users WHERE username=%s"
    #try
    cursor.execute(deleteuser, (name,))
    print("You deleted the user: " + name)
    db.commit()




# ------------ working functions --------------------------------------------
