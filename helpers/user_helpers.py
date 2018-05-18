import hashlib
import MySQLdb # pip install mysql-client or something else
# Add new song into songs table
# used by chart crawlers
from configparser import ConfigParser
import helpers.db_helpers as helpers


def newuser(userid, name, password, vegetarian):
    db = helpers.getDbCon()
    cursor = db.cursor()
    hashedpw = password #not being hashed yet
    userInsertQuery = "INSERT into users (user_id, username, password, vegetarian) VALUES (%s, %s, %s, %s)"
    # try:
    cursor.execute(userInsertQuery, (userid, name, hashedpw, vegetarian)) # to replace s% put in quotation markes
    db.commit()

def getAllUsers():
    db = helpers.getDbCon()
    cursor = db.cursor()
    getUsersQuery = "SELECT * FROM users"
    cursor.execute(getUsersQuery)
    print(cursor.fetchall())
    return cursor.fetchall()

#function does not work. asked Ruben
def getPassword(user_name):
    db = helpers.getDbCon()
    cursor = db.cursor()
    getpassword = "SELECT password FROM users WHERE username = %s"
    # try:
    cursor.execute(getpassword, user_name)
    print(cursor.fetchone())
    return cursor.fetchone()


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

# ------------ working functions --------------------------------------------


#newuser(1, "Julian", "newpassword", 0)
#newuser(3, "Sebastian", "supersecurepassword", 1)
#getAllUsers()
