import hashlib
import MySQLdb # pip install mysql-client or something else
# Add new song into songs table
# used by chart crawlers
from configparser import ConfigParser
<<<<<<< HEAD
import db_helpers as helpers
from contextlib import closing

def newUser(name, password, vegetarian):
    db = helpers.getDbCon()
    with closing(db.cursor()) as cursor:
        hashedpw = password #not being hashed yet
        userInsertQuery = "INSERT into users (username, password, vegetarian) VALUES (%s, %s, %s)"
        # try:
        cursor.execute(userInsertQuery, (name, hashedpw, vegetarian)) # to replace s% put in quotation markes
=======
import helpers.db_helpers as helpers


def newUser(name, hashed_password, vegetarian):
    db = helpers.getDbCon()
    cursor = db.cursor()
    userInsertQuery = "INSERT into users (username, password, vegetarian) VALUES (%s, %s, %s)"
    # try:
    cursor.execute(userInsertQuery, (name, hashed_password, vegetarian)) # to replace s% put in quotation markes
>>>>>>> 022cd3426a6a23477b20cfeb9fc03910aafcab35
    db.commit()
    print("Successfully added " + name)


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
<<<<<<< HEAD
    db.commit()





# ------------ working functions --------------------------------------------

newUser("Max", "124", 0)
#newuser(3, "Sebastian", "supersecurepassword", 1)
#getAllUsers()
#deleteUser("Sinan")
=======
    db.commit()
>>>>>>> 022cd3426a6a23477b20cfeb9fc03910aafcab35
