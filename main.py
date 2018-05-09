#import classes
import base64, json, requests, glob

#list of commonly used terms which are too general
common_terms = ["animal source foods", "animal fat", "vegetable", "natural foods", "local foods", "produce", "food",
                "product", "product design", "ingredient", "drink", "dairy product", "yellow", "red", "blue",
                "al dente", "italian food"]

def scanFolderforPictures(folder_path):
    """ takes a folder directory as the input and adds all pictures in an array, which will be returned """

    jpg = folder_path + "/*.jpg"
    jpeg = folder_path + "/*.jpeg"
    png = folder_path + "/*.png"
    gif = folder_path + "/*.gif"

    list_of_formats = [jpg, jpeg, png, gif]

    list_of_image_paths = []

    for format in list_of_formats:
        list_of_image_paths.extend(glob.glob(format))

    return list_of_image_paths


def identifyNewIngredient(image_to_append):
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

    return chooseCorrectIngredient(list_of_possible_ingredients)


def chooseCorrectIngredient(list_of_ingredients):
    """loops every possible description and returns the first that is not in the list of common terms"""

    for element in list_of_ingredients:
        if compareWithCommonTerms(element):
            """no clue why that does not work otherwise"""
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

    print(response.text)

    print("")
    print("You can choose between the following recipes:")
    print("")

    for recipe in response.json():
        print(recipe.get("title"))


if __name__ == "__main__":
    """starts the program"""

    isFinished = False

    while isFinished != True:
        folder_path = str(input("Please insert the file path of your folder containing all the pictures"))
        list_of_image_paths = scanFolderforPictures(folder_path)

        # list of recognized ingredients
        recognized_ingredients = []

        for image_path in list_of_image_paths:
            recognized_ingredients.append(identifyNewIngredient(image_path))

        print("")
        print("Your ingredients so far are:")
        print(recognized_ingredients)
        print("")

        getRecipesByIngredient()
        isFinished = True




