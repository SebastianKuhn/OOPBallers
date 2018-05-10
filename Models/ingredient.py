class Ingredient(object):

    def __init__(self, name, ingredient_id=None, amount=None, unit=None):
        self.name = name
        self.ingredient_id = ingredient_id
        self.amount = amount
        self.unit = unit

    #getter methods

    def getName(self):
        return self.name

    def getId(self):
        return self.ingredient_id

    def getAmount(self):
        return self.amount

    def getUnit(self):
        return self.unit

    #setter methods

    def setId(self, ingredient_id):
        self.ingredient_id = ingredient_id

    def setAmount(self, amount):
        self.amount = amount

    def setUnit(self, unit):
        self.unit = unit
