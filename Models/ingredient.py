class Ingredient(object):

    def __init__(self, ingredient_name, ingredient_id, amount, unit):
        self.ingredient_name = ingredient_name
        self.ingredient_id = ingredient_id
        self.amount = amount
        self.unit = unit

    def printInformation(self):
        print(str(self.amount) + " " + str(self.unit) + " of " + str(self.ingredient_name))
