import hashlib
import MySQLdb # pip install mysql-client or something else
# Add new song into songs table
# used by chart crawlers
from configparser import ConfigParser
import db_helpers as helpers

def newuser(userid, name, password, vegetarian):
    db = helpers.getDbCon()
    cursor = db.cursor()
    hashedpw = password
    userInsertQuery = "INSERT into users (user_id, username, password, vegetarian) VALUES (%s, %s, %s, %s)"
    # try:
    cursor.execute(userInsertQuery, (userid, name, hashedpw, vegetarian)) # to replace s% put in quotation markes
    db.commit()

def getAllUsers():
    db = helpers.getDbCon()
    cursor = db.cursor()

    getUsersQuery = "SELECT * FROM users"
    cursor.execute(getUsersQuery)
    # print(cursor.fetchall())
    return cursor.fetchall()


def login(record):
    db = getDbCon()
    cursor = db.cursor()

    kpiInsertQuery = "INSERT into kpis (song_id, name, value, crawl_time) VALUES (%s, %s, %s, %s)"
    # try:
    cursor.execute(kpiInsertQuery, (record["song_id"], record["name"], record["value"], record["crawl_time"]))
    db.commit()


#newuser(1, "Julian", "newpassword", 0)
getAllUsers()
