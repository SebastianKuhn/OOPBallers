"""
This file contains the function needed to connect to establish a connection to the db.
"""
import MySQLdb
from configparser import ConfigParser

def getDbCon():
    """
    Establishes a connection to the database
    :return: Mysqldb.connect object that can be used to access the database.
    """
    # Configure settings. Try and except are used because of sketchy behaviour of parser.read function.
    parser = ConfigParser()
    try:
        parser.read('config/config.ini')
        db_host = parser.get('db', 'host')
        db_user = parser.get('db', 'user')
        db_password = parser.get('db', 'password')
        db_name = parser.get('db', 'db')
    except Exception:
        parser.read('../config/config.ini')
        db_host = parser.get('db', 'host')
        db_user = parser.get('db', 'user')
        db_password = parser.get('db', 'password')
        db_name = parser.get('db', 'db')

    return MySQLdb.connect(db_host, db_user, db_password, db_name, use_unicode=True, charset="utf8")
