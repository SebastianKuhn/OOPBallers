class User(object):

    def __init__(self, username, hashed_password, vegetarian_status=None, user_id=None):
        self.username = username
        self.hashed_password = hashed_password
        self.vegetarian_status = vegetarian_status
        self.user_id = user_id

    #getter methods

    def getUsername(self):
        return self.username

    def getHashedPassword(self):
        return self.hashed_password

    def getVegetarianStatus(self):
        return self.vegetarian

    def getId(self):
        return self.user_id

    #setter methods

    def setVegetarianStatus(self, vegetarian_status):
        self.vegetarian_status = vegetarian_status

    def setId(self, user_id):
        self.user_id = user_id
