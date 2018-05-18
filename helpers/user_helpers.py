import hashlib
import MySQLdb # pip install mysql-client or something else
# Add new song into songs table
# used by chart crawlers
from configparser import ConfigParser
import db_helpers as helpers

def newUser(userid, name, password, vegetarian):
    db = helpers.getDbCon()
    cursor = db.cursor()
    hashedpw = password #not being hashed yet
    userInsertQuery = "INSERT into users (user_id, username, password, vegetarian) VALUES (%s, %s, %s, %s)"
    # try:
    cursor.execute(userInsertQuery, (userid, name, hashedpw, vegetarian)) # to replace s% put in quotation markes
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

def getAllUsersnames():
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

#newUser(6, "Taylor", "123", 0)
#newuser(3, "Sebastian", "supersecurepassword", 1)
#getAllUsers()
#deleteUser("Sinan")
