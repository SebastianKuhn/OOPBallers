class Instruction(object):

    def __init__(self, number, step, ingredients, equipment):
        self.number = number
        self.step = step
        self.ingredients = ingredients
        self.equipment = equipment

    def printInformation(self):
        print("")
        print("Step " + str(self.number) + ": ")
        print("You need: ")
        print("Ingredients:")
        for ingredient in self.ingredients:
            ingredient.printInformation()
        print("Equipment:")
        for equipment in self.equipment:
            equipment.printInformation()
        print("")
        print(self.step)
        print("")
