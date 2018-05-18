from Models.ingredient import Ingredient

class Recipe(object):

    def __init__(self, recipe_id, title, ready_in_minutes=None, servings=None, vegetarian=None, source_url=None,
                 aggregate_likes=None, health_score=None, ingredients=[], instructions=[]):

        self.recipe_id = recipe_id
        self.title = title
        self.ready_in_minutes = ready_in_minutes
        self.servings = servings
        self.vegetarian = vegetarian
        self.source_url = source_url
        self.aggregate_likes = aggregate_likes
        self.health_score = health_score
        self.ingredients = ingredients
        self.instructions = instructions

    def printRecipeInformations(self):
        print("Title: " + str(self.title))
        print("")
        print("Ready in Minutes: " + str(self.ready_in_minutes))
        print("Servings: " + str(self.servings))
        print("Vegetarian: " + str(self.vegetarian))
        print("Likes: " + str(self.aggregate_likes))
        print("Health Score: " + str(self.health_score) + "%")
        print("")

        if len(self.ingredients) != 0:
            print("Ingredients: ")
            for ingr in self.ingredients:
                ingr.printInformation()
        else:
            print("Unfortunately, there are no Ingredients for this recipe.")

        print("")
        if len(self.instructions) != 0:
            print("Instructions: ")
            for instr in self.instructions:
                instr.printInformation()
        else:
            print("Unfortunately, there are no Instructions for this recipe.")

