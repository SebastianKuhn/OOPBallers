class Instruction(object):

    def __init__(self, number, step, ingredients, equipment):
        self.number = number
        self.step = step
        self.ingredients = ingredients
        self.equipment = equipment

    #getter methods

    def getNumber(self):
        return self.number

    def getStep(self):
        return self.step

    def getIngredients(self):
        return self.ingredients

    def getEquipment(self):
        return self.equipment
