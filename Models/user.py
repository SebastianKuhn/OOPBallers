class User(object):

    def __init__(self, user_id, username, hashed_password, vegetarian):
        self.user_id = user_id
        self.username = username
        self.hashed_password = hashed_password
        self.vegetarian = vegetarian

    #getter methods

    def getId(self):
        return self.user_id

    def getUsername(self):
        return self.username

    def getHashedPassword(self):
        return self.hashed_password

    def getVegetarianStatus(self):
        return self.vegetarian
