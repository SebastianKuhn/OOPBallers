"""
This file contains class equipment which consists of the name and a unique id which is adopted from spoonacular.
"""

class Equipment(object):

    def __init__(self, equipment_name, equipment_id):
        self.equipment_name = equipment_name
        self.equipment_id = equipment_id

    def printInformation(self):
        """
        This method prints the name of the equipment.
        """
        print(str(self.equipment_name))