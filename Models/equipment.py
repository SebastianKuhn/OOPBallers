class Equipment(object):

    def __init__(self, name, equipment_id):
        self.name = name
        self.equipment_id = equipment_id

    def printInformation(self):
        print(str(self.name))