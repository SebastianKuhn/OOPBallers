import json

class GoogleVisionObject(object):

    def __init__(self, description, score):
        self.description = description
        self.score = score

    def getDescription(self):
        return self.description