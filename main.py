from Controller import googlevision, spoonacular, json_parser
from helpers import user_helpers
from helpers import recipe_helpers
import hashlib, uuid
from Models.user import User
from Models.recipe import Recipe


def welcome():
    """
    starts the program and welcomes the user
    """

    print("""


                 \ \  / /                                                  ___         ___
                  \ \/ /           _   __      _   __     //             //   ) )    //   ) )
                   \/ / //   / / // ) )  ) ) // ) )  ) ) // //   / /      __ / /    //   / /
                   / / //   / / // / /  / / // / /  / / // ((___/ /          ) )   //   / /
                  / / ((___( ( // / /  / / // / /  / / //      / /     ((___/ / . ((___/ /
                                                              / /
                                                             / /
            
            """)
    print("Welcome to Yummly, you're tool to search recipes by snapping pictures of the ingredients in the fridge!")
    print("")
    print("")
    print("Please choose to either log in if you already have an account or sign up if you do not.")
    print("")


def login():
    """
    prompts the user to login and checks the credentials in the database
    """
    print("")

    while True:
        username = str(input("username: "))
        password = str(input("password: "))

        # check username and password in the database using the database controller -> if clause following
        # check password => hash function in the database controller



        break


    print("")
    print("You successfully logged in")
    print("")

    #return user


def signUp():
    """
    prompts the user to define a username and a password. The username will be checked in the
    database whether it is still available
    """
    print("")

    while True:
        username = str(input("Please enter a username: "))

        # check username against database using the database controller
        usernames = user_helpers.getAllUsernames()

        username_exists = False

        for name in usernames:

            if username.lower() == name.lower():
                print("")
                print("This username already exist, please login or choose another username.")
                print("")
                username_exists = True

        if username_exists is False:
            break

    print("")
    password = str(input("Please enter a password: "))
    print("")

    #determine whether the new user is vegetarian
    while True:
        vegetarian_input = str(input("Are you a vegetarian? (Y/N) "))

        if vegetarian_input.lower() == "y":
            vegetarian = True
            break
        elif vegetarian_input.lower() == "n":
            vegetarian = False
            break
        else:
            vegetarian_input = print("Please enter Y or N.")

    #hash password
    hashed_password = hash_password(password)

    #create User
    user_helpers.newUser(username, hashed_password,vegetarian)
    user = User(username, hashed_password, vegetarian)

    print("")
    print("You successfully created an account!")
    print("")

    #return user to use within the running program
    return user


def hash_password(password):
    """
    input: password as a string
    :return hashed password
    """

    return hashlib.sha256(password.encode()).hexdigest()


def presentOptions():
    """
    presents all the available options
    """

    print("Please enter the number of one of the following options:")
    print("1. Search a new recipe using pictures")
    print("2. Search recipes by name")
    print("3. Get all your recipes")
    print("'info' to get information on all options")
    print("'exit' to end the program")
    print("")


def checkUserInput(cur_user):
    """
    checks the user input and matches it with the available options
    input: current user as User-object
    """

    user_input = str(input("What would you like to do? "))

    #search new recipe by ingredients.
    if user_input == "1":
        #saves all recognized ingredients, which are used to search for a recipe in the spoonacular controller
        recognized_ingredients = identifyIngredients()
        recipes = spoonacular.getRecipesByIngredient(recognized_ingredients)
        chosen_recipe = chooseRecipe(recipes)
        chosen_recipe.printRecipeInformations()
        print("")

        while True:
            save_recipe_input = str(input("Would you like to save the recipe? Y/N "))

            if save_recipe_input.lower() == "y":
                recipe_helpers.newRecipe(chosen_recipe)
                user_id = user_helpers.getCurrentUserId(cur_user.username)
                recipe_helpers.addRecipetoUser(user_id, chosen_recipe.recipe_id)
                break
            elif save_recipe_input.lower() == "n":
                break
            else:
                print("Oops, please type Y or N.")

        print("")

    elif user_input == "2":
        print("")
        search_query = str(input("What recipe would you like to search for? "))
        recipes = spoonacular.getRecipeByName(search_query)
        chosen_recipe = chooseRecipe(recipes)
        chosen_recipe.printRecipeInformations()
        # saveRecipeInDatabase?
        print("")

    elif user_input == "3":
        print("")
        print("get your recipes")
        print("")

    elif user_input.lower() == "info":
        presentOptions()

    elif user_input.lower() == "exit":
        return True

    else:
        print("")
        print("Please enter a valid number. If you need further information type: info")
        print("")

    presentOptions()


def identifyIngredients():
    """
    asks the user for a folder file path, analyzes the pictures and returns the ingredients
    :return recognized ingredients as Ingredient-objects in a list
    """

    list_of_image_paths = []

    #checks if there are any results
    while len(list_of_image_paths) == 0:
        print("")
        folder_path = str(input("Please insert the file path of your folder containing all the pictures:  "))
        list_of_image_paths = googlevision.scanFolderforPictures(folder_path)

        if len(list_of_image_paths) == 0:
            print("")
            print("Please enter a valid folder file path which includes pictures!")
            print("")

    # list of recognized ingredients
    recognized_ingredients = []

    #starts the googlevision api call for every picture and appends the recognized ingredient to the list
    for image_path in list_of_image_paths:
        recognized_ingredients.append(googlevision.identifyNewIngredient(image_path))

    print("")
    print("Your ingredients so far are:")
    print(recognized_ingredients)
    print("")

    return recognized_ingredients


def chooseRecipe(response):
    """
    takes the spoonacular response as input and asks the user which recipe he wants to choose.
    input: spoonacular json-response
    :return complete_recipe as Recipe object

    """

    recipes = None

    try:
        if response.get("results") is not None:
            recipes = response.get("results")

    except:
        recipes = response

    print("")
    print("You can choose between the following recipes:")
    print("")

    number = 1

    #prints the fetched recipe names
    for recipe in recipes:
        print(str(number) + ". " + recipe.get("title"))
        number += 1

    #checks whether the user input is an int and if it is not out of bounds
    while True:
        try:
            print("")
            chosen_recipe_nr = input("About which one would you like to know more? Just type in the number: ")
            print("")

            value = int(chosen_recipe_nr)

            if value <= 0 or value > number-1: #subtracted 1 because the for-loop increases the number 1 too much
                print("Oops, your number is not even listed!")
            else:
                break

        except ValueError:
            print("Please enter a valid number!")
            print("")

    chosen_recipe = json_parser.parseIdAndTitle(recipes, value)

    recipe_information = spoonacular.getRecipeInformation(chosen_recipe.recipe_id)

    print(recipe_information)

    complete_recipe = json_parser.parseRemainingVariables(recipe_information, chosen_recipe)

    return complete_recipe


if __name__ == "__main__":
    """starts the program"""

    current_user = None

    welcome()

    login_or_signup = str(input("Login/Sign up (1/2): "))
    login_status = False

    while login_status is False:
        if login_or_signup == "1":
            current_user = login()
            login_status = True
        elif login_or_signup == "2":
            current_user = signUp()
            login_status = True
        else:
            print("")
            print("Please enter either 1 or 2")
            login_or_signup = str(input("Login/Sign up (1/2): "))

    presentOptions()

    is_finished = False

    while is_finished != True:
        is_finished = checkUserInput(current_user)