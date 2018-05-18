class User(object):

    def __init__(self, username, hashed_password, vegetarian_status=None, user_id=None):
        self.username = username
        self.hashed_password = hashed_password
        self.vegetarian_status = vegetarian_status
        self.user_id = user_id
