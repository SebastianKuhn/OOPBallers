"""
This file contains the Ingredient class which consists of the name, a unique id as well as the amount and the unit used

"""

class Ingredient(object):

    def __init__(self, ingredient_name, ingredient_id, amount, unit):
        self.ingredient_name = ingredient_name
        self.ingredient_id = ingredient_id
        self.amount = amount
        self.unit = unit

    def printInformation(self):
        """
        This method prints all the necessary information about the ingredient in order to present it to the user.
        """
        print(str(self.amount) + " " + str(self.unit) + " of " + str(self.ingredient_name))
