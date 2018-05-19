import requests

def getRecipesByIngredient(ingredients):

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

    base_url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/" + str(recipe_id) + "/information"

    response = requests.get(
        base_url,
        headers={
            "X-Mashape-Key": "PO4pY9yb8wmshcGIX33au66a9Jvdp1FpU0zjsnwB2BMrEKZ902",
            "X-Mashape-Host": "spoonacular-recipe-food-nutrition-v1.p.mashape.com"
        }
    )

    return response.json()


def getRecipeByName(name):

    base_url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/search?query=" + name

    response = requests.get(
        base_url,
        headers={
            "X-Mashape-Key": "PO4pY9yb8wmshcGIX33au66a9Jvdp1FpU0zjsnwB2BMrEKZ902",
            "X-Mashape-Host": "spoonacular-recipe-food-nutrition-v1.p.mashape.com"
        }
    )

    print(response.json())

    return response.json()

