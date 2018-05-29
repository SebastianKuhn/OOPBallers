"""
This file serves as the controller for the google vision api. Every function which communicates with the google vision
api is included in this file.
"""

#import classes
import base64, json, requests, glob

#list of commonly used terms which are too general
common_terms = ["animal source foods", "animal fat", "vegetable", "natural foods", "local foods", "produce", "food",
                "product", "product design", "ingredient", "drink", "dairy product", "yellow", "red", "blue",
                "al dente", "italian food", "superfood", "fruit", "still life photography", "banana family"]

def scanFolderforPictures(folder_path):
    """
    takes a folder directory as the input and adds all pictures in an array, which will be returned
    input: folder path as string
    :return list of strings
    """

    jpg = folder_path + "/*.jpg"
    JPG = folder_path + "/*.JPG"
    jpeg = folder_path + "/*.jpeg"
    png = folder_path + "/*.png"
    gif = folder_path + "/*.gif"

    list_of_formats = [jpg, JPG, jpeg, png, gif]

    list_of_image_paths = []

    for image_format in list_of_formats:
        list_of_image_paths.extend(glob.glob(image_format))

    return list_of_image_paths


def identifyNewIngredient(image_to_append):
    """
    sends a request to the Google Vision API and chooses the correct term
    input: image_path
    :return list of strings
    """

    base_url = "https://vision.googleapis.com/v1/images:annotate?key="
    api_key = "AIzaSyDfKIKpRF7OBu5Q3Q6Zh1zxFOsulyTZ2IE"
    url = base_url + api_key
    image_base64 = encodeImageAsBase64(image_to_append)

    json_request = {
                      "requests":[
                        {
                          "image":{
                            "content": image_base64.decode("utf-8") #decoding from bytes into a string
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

    return chooseCorrectIngredient(list_of_possible_ingredients)


def encodeImageAsBase64(image_path):
    """
    Loads an image from path and returns it as base64 encoded string
    input: image path as string
    :return String
    """

    print("Encoding image: "+ image_path)
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string


def chooseCorrectIngredient(list_of_ingredients):
    """
    loops every possible description and returns the first that is not in the list of common terms
    input: list of strings
    :return String
    """

    for element in list_of_ingredients:
        if not compareWithCommonTerms(element):
            return element.get("description")


def compareWithCommonTerms(ingredient):
    """
    loops the input ingredient's description through all common terms and returns true if one of the is equal
    input: String
    return: Boolean
    """

    for term in common_terms:
        if ingredient.get("description").lower() == term:
            return True