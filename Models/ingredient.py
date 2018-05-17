class Ingredient(object):

    def __init__(self, name, ingredient_id, amount, unit):
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