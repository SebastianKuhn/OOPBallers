#import classes
import base64
import json
import requests
from googlevisionobject import GoogleVisionObject

#list of commonly used terms which are too general
common_terms = ["animal source foods", "animal fat", "vegetable", "natural foods", "local foods", "produce", "food",
                "product", "product design", "ingredient", "drink", "dairy product", "yellow", "red", "blue",
                "al dente", "italian food"]

#list of recognized ingredients
recognized_ingredients = []


def appendNewIngredient(image_to_append):
    """ sends a request to the Google Vision API and chooses the correct term """

    base_url = "https://vision.googleapis.com/v1/images:annotate?key="
    api_key = "AIzaSyDfKIKpRF7OBu5Q3Q6Zh1zxFOsulyTZ2IE"
    url = base_url + api_key
    image_base64 = encodeImageAsBase64(image_to_append)

    json_request = {
                      "requests":[
                        {
                          "image":{
                            "content": image_base64.decode("utf-8")
                          },
                          "features": [
                            {
                              "type":"LABEL_DETECTION",
                              "maxResults": 5
                            }
                          ]
                        }
                      ]
                    }

    #performs request and saves response, decodes it and chooses the list in list_of_possible_ingredients
    response = requests.post(url, data=json.dumps(json_request))
    loaded_json = response.json()
    list_of_possible_ingredients = loaded_json["responses"][0]["labelAnnotations"]

    #appends the first possible ingredient's name that is not in the list of common terms
    recognized_ingredients.append(chooseCorrectIngredient(list_of_possible_ingredients))
    print("")
    print("Your ingredients so far are:")
    print(recognized_ingredients)


def chooseCorrectIngredient(list_of_ingredients):
    """loops every possible description and returns the first that is not in the list of common terms"""

    for element in list_of_ingredients:
        if compareWithCommonTerms(element):
            print("wrong description")
        else:
            return element.get("description")


def compareWithCommonTerms(ingredient):
    for term in common_terms:
        if ingredient.get("description") == term:
            return True


def encodeImageAsBase64(image_path):
    """ Loads an image from path and returns it as base64 encoded string """

    print("Encoding image: "+ image_path)
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string


def getRecipesByIngredient():

    base_url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?ranking=" \
               "1&number=5&ingredients="
    ingredients_no_spaces = []

    #delete all spaces for the url
    for ingredient in recognized_ingredients:
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

    print(response.json)


if __name__ == "__main__":
    """starts the program"""

    isFinished = False

    while isFinished != True:
        image_path = str(input("Please insert the file path of the ingredient you want to analyze"))
        appendNewIngredient(image_path)
        answer = str(input("Do you want to add another ingredient? (y/n)"))
        if answer == "n":
            getRecipesByIngredient()
            isFinished = True


