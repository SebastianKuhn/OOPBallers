"""
This file contains the class user. A user consists of a username, a hashed password, whether he is vegetarian or not
and a unique user id.
"""


class User(object):

    def __init__(self, username, hashed_password, vegetarian_status=None, user_id=None):
        self.username = username
        self.hashed_password = hashed_password
        self.vegetarian_status = vegetarian_status
        self.user_id = user_id
