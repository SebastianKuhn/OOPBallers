import MySQLdb
from configparser import ConfigParser

def getDbCon():
    # Configure settings
    parser = ConfigParser()
    parser.read('../config/config.ini')

    db_host = parser.get('db','host')
    db_user = parser.get('db','user')
    db_password = parser.get('db','password')
    db_name = parser.get('db','db')
    print(db_name)
    return (MySQLdb.connect(db_host, db_user, db_password, db_name))
