import googlevisioncontroller
import spoonacularcontroller


def searchNewRecipes():
    """asks the user for a folder file path, analyzes the pictures and prints the ingredients as well as possible
    recipes"""

    folder_path = str(input("Please insert the file path of your folder containing all the pictures"))
    list_of_image_paths = googlevisioncontroller.scanFolderforPictures(folder_path)

    # list of recognized ingredients
    recognized_ingredients = []

    for image_path in list_of_image_paths:
        recognized_ingredients.append(googlevisioncontroller.identifyNewIngredient(image_path))

    print("")
    print("Your ingredients so far are:")
    print(recognized_ingredients)
    print("")

    spoonacularcontroller.getRecipesByIngredient(recognized_ingredients)


if __name__ == "__main__":
    """starts the program"""

    is_finished = False

    while is_finished != True:
        searchNewRecipes()
        isFinished = True




