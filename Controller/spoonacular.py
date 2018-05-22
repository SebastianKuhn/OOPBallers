"""
This file serves as the controller for the spoonacular api. Every function which communicates with the spoonacular
api is included in this file.
"""

import requests

def getRecipesByIngredient(ingredients):
    """
    fetches recipes which maximize the use of input ingredients.
    :param ingredints: list of strings
    :return decoded json
    """
    base_url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?ranking=" \
               "1&number=5&ingredients="
    ingredients_no_spaces = []

    #delete all spaces for the url
    for ingredient in ingredients:
        ingredient = ''.join(str(ingredient).split())
        ingredients_no_spaces.append(ingredient)

    ingredients = '%2C'.join(ingredients_no_spaces)
    url = base_url + ingredients

    response = requests.get(
        url,
        headers={
            "X-Mashape-Key": "PO4pY9yb8wmshcGIX33au66a9Jvdp1FpU0zjsnwB2BMrEKZ902",
            "X-Mashape-Host": "spoonacular-recipe-food-nutrition-v1.p.mashape.com"
        }
    )

    return response.json()

def getRecipeInformation(recipe_id):
    """
    fetches the informations by using the recipe_id
    :param recipe_id: integer
    :return decoded json
    """
    base_url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/" + str(recipe_id) + "/information"

    response = requests.get(
        base_url,
        headers={
            "X-Mashape-Key": "PO4pY9yb8wmshcGIX33au66a9Jvdp1FpU0zjsnwB2BMrEKZ902",
            "X-Mashape-Host": "spoonacular-recipe-food-nutrition-v1.p.mashape.com"
        }
    )

    return response.json()


def getRecipeByName(search_query):
    """
    fetches recipes using natural language detection.
    :param search_query: string
    :return decoded json
    """

    base_url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/search?query=" + search_query

    response = requests.get(
        base_url,
        headers={
            "X-Mashape-Key": "PO4pY9yb8wmshcGIX33au66a9Jvdp1FpU0zjsnwB2BMrEKZ902",
            "X-Mashape-Host": "spoonacular-recipe-food-nutrition-v1.p.mashape.com"
        }
    )

    return response.json()

