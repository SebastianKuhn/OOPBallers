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
    image_base64 = encode_image_as_base64(image_to_append)

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
    recognized_ingredients.append(chooseCorrectIngredient(list_of_possible_ingredients).getDescription())


def chooseCorrectIngredient(list_of_ingredients):
    """loops every possible description and returns the first that is not in the list of common terms"""

    for element in list_of_ingredients:
        for term in common_terms:
            if element.get("description") != term:
                description = element.get("description")
                score = element.get("score")
                ingredient = GoogleVisionObject(description, score)
                return ingredient


def encode_image_as_base64(image_path):
    """ Loads an image from path and returns it as base64 encoded string """

    print("Encoding image: "+ image_path)
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string


if __name__ == "__main__":
    """starts the program"""

    isFinished = False

    while isFinished != True:
        image_path = str(input("Please insert the file path of the ingredient you want to analyze"))
        appendNewIngredient(image_path)
        answer = str(input("Do you want to add another ingredient? (y/n)"))
        if answer == "n":
            print(recognized_ingredients)
            isFinished = True


