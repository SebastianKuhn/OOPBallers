class Recipe(object):

    def __init__(self, recipe_id, title, ready_in_minutes, image_url, servings, vegetarian=None, source_url=None,
                 aggregate_likes=None, health_score=None, ingredients=[], instructions=[]):

        self.recipe_id = recipe_id
        self.title = title
        self.ready_in_minutes = ready_in_minutes
        self.image_url = image_url
        self.servings = servings
        self.vegetarian = vegetarian
        self.source_url = source_url
        self.aggregate_likes = aggregate_likes
        self.health_score = health_score
        self.ingredients = ingredients
        self.instructions = instructions

    #getter methods

    def getId(self):
        return self.recipe_id

    def getTitle(self):
        return self.title

    def getReadyInMinutes(self):
        return self.ready_in_minutes

    def getImageUrl(self):
        return self.image_url

    def getServings(self):
        return self.servings

    def getVegetarian(self):
        return self.vegetarian

    def getSourceUrl(self):
        return self.source_url

    def getAggregateLikes(self):
        return self.aggregate_likes

    def gethealthScore(self):
        return self.health_score

    def getIngredients(self):
        return self.ingredients

    def getInstructions(self):
        return self.instructions

    #setter methods

    def setVegetarian(self, vegetarian):
        self.vegetarian = vegetarian

    def setSourceUrl(self, source_url):
        self.source_url = source_url

    def setAggregateLikes(self, aggregate_likes):
        self.aggregate_likes = aggregate_likes

    def sethealthScore(self, health_score):
        self.health_score = health_score

    def setIngredients(self, ingredients):
        self.ingredients = ingredients

    def setInstructions(self, instructions):
        self.instructions = instructions

