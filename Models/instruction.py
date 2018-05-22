"""
This file contains the class instructions which consists of the number, steps and equipment used in every
step to create a recipe.
"""

class Instruction(object):

    def __init__(self, instruction_number, step, ingredients, equipment):
        self.instruction_number = instruction_number
        self.step = step
        self.ingredients = ingredients
        self.equipment = equipment

    def printInformation(self):
        """
        This method prints all the necessary information about the instruction in order to present it to the user.
        """
        print("")
        print("Step " + str(self.instruction_number) + ": ")

        if len(self.ingredients) != 0 or len(self.equipment) != 0:
            print("You need: ")

        if len(self.ingredients) != 0:
            print("Ingredients:")
            for ingredient in self.ingredients:
                ingredient.printInformation()

        if len(self.equipment) != 0:
            print("Equipment:")
            for equipment in self.equipment:
                equipment.printInformation()

        print("")
        print(self.step)
        print("")
