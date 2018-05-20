class Equipment(object):

    def __init__(self, equipment_name, equipment_id):
        self.equipment_name = equipment_name
        self.equipment_id = equipment_id

    def printInformation(self):
        print(str(self.equipment_name))