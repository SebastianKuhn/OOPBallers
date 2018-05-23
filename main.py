"""
This is the main file which starts the program and interacts with the user.
"""

from Controller import googlevision, spoonacular, json_parser
from helpers import user_helpers
from helpers import login_helpers
from helpers import master_helpers
from helpers import recipe_helpers
import hashlib
from Models.user import User
from helpers import ingredient_helpers


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
    #starts the login function in login_helpers and returns a user object
    user = login_helpers.login()

    return user


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

        #loops through all usernames and checks whether the username already exists.
        username_exists = False
        for name in usernames:

            if username.lower() == name.lower():
                #username exists - lets the user decide whether he rather wants to login.
                print("")
                login_input = input("This username already exist, do you want to login? (Y/N) ")
                print("")

                if login_input.lower() == "y":
                    login_user = login_helpers.login()
                    return login_user

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
    user = User(username, hashed_password, vegetarian)
    user_helpers.newUser(user)

    #fetch User ID
    user_id = user_helpers.getCurrentUserId(username)

    user.user_id = user_id

    print("")
    print("You successfully created an account!")
    print("")

    #return user to use within the running program
    return user


def hash_password(password):
    """
    hash password using sha256
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
    print("4. Delete your Account")
    print("'info' to get information on all options")
    print("'exit' to end the program")
    print("")


def checkUserInput(cur_user):
    """
    checks the user input and matches it with the available options
    input: current user as User-object
    """

    presentOptions()
    user_input = str(input("What would you like to do? Type in a number or 'info' for information: "))

    #search new recipe by ingredients.
    if user_input == "1":
        #saves all recognized ingredients, which are used to search for a recipe in the spoonacular controller
        recognized_ingredients = identifyIngredients()
        #fetches 5 possible recipes
        recipes = spoonacular.getRecipesByIngredient(recognized_ingredients)
        #lets the user decide which recipe he wants
        chosen_recipe = chooseRecipeFromJson(recipes)
        #prints the recipe's information
        chosen_recipe.printRecipeInformations()

        #lets the user decide wheter he wants to save the recipe in his account
        saveRecipe(chosen_recipe, cur_user)

    elif user_input == "2":
        print("")
        #asks for the search query
        search_query = str(input("What recipe would you like to search for? "))
        #saves the api response
        recipes = spoonacular.getRecipeByName(search_query)

        if len(recipes.get("results")) != 0:
            # lets the user decide which recipe he wants
            chosen_recipe = chooseRecipeFromJson(recipes)
            # prints the recipe's information
            chosen_recipe.printRecipeInformations()
            # lets the user decide wheter he wants to save the recipe in his account
            saveRecipe(chosen_recipe, cur_user)
            print("")
        else:
            print("")
            print("")
            print("Unfortunately your search did not have any results. Please start again.")
            print("")
            print("")

    elif user_input == "3":
        #get all recipe ids and titles for the current user
        list_of_recipe_ids = recipe_helpers.getRecipeIds(cur_user)
        list_of_recipe_titles = recipe_helpers.getRecipeNames(list_of_recipe_ids)
        check = isempty(list_of_recipe_ids)
        if check is True:
            #print the recipes
            number = 1
            for title in list_of_recipe_titles:
                print(str(number) + ". " + str(title))
                number += 1
            print("")

            chosen_value = chooseCorrectNumber(number)

            chosen_recipe_id = list_of_recipe_ids[chosen_value-1]

            chosen_recipe = master_helpers.master_getRecipeInformation(chosen_recipe_id)

            chosen_recipe.printRecipeInformations()
        else:
            print("")
            print("Unfortunately you have no recipes saved. You can search recipes with option 1 or 2")
            print("")

    elif user_input == "4":
        print("")
        delete_response = str(input("Do you really want to delete your account? Type 'DELETE' to delete your Account or "
                                "'cancel' to cancel: "))

        if delete_response == "DELETE":
            print("")
            print(cur_user.username)
            print(user_helpers.deleteUser(cur_user.user_id))
            print("The programm will now end.")
            return True
        elif delete_response.lower() == "cancel":
            print("")
            presentOptions()

        else:
            print("")
            delete_response = str(input("Please type in DELETE in caps or cancel to cancel. "))
            print("")


    elif user_input.lower() == "info":
        #presents all the options that the user has
        presentOptions()

    elif user_input.lower() == "exit":
        #ends the program
        return True

    else:
        print("")
        print("Please enter a valid number. If you need further information type: info")
        print("")


def saveRecipe(chosen_recipe, cur_user):
    """
    saves the Recipe to the current user.
    input: recipe, user
    """
    while True:
        save_recipe_input = str(input("Would you like to save the recipe? Y/N "))

        if save_recipe_input.lower() == "y":
            #adds the recipe to the database
            master_helpers.master_addRecipe(chosen_recipe)
            #gets the user_id of the current user
            user_id = user_helpers.getCurrentUserId(cur_user.username)[0]
            #adds the recipe to the user
            master_helpers.master_addRecipetoUser(user_id, chosen_recipe)
            break
        elif save_recipe_input.lower() == "n":
            break
        else:
            print("Oops, please type Y or N.")

    print("")

def identifyIngredients():
    """
    asks the user for a folder file path, analyzes the pictures and returns the ingredients in a list
    :return list of strings
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

    #prints all the ingredients
    print("")
    print("Your ingredients so far are:")

    number = 1

    for ingredient in recognized_ingredients:
        print(str(number) + ". " + ingredient)
        number += 1

    print("")

    return recognized_ingredients


def chooseRecipeFromJson(response):
    """
    takes the spoonacular response as input and asks the user which recipe he wants to choose.
    input: decoded json response
    :return recipe

    """

    recipes = None

    #try to get "results" from the response in case the getRecipeByName function was triggered. Otherwise it is
    #the getRecipeByIngredients resposne which has no "results" key
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

    #lets the user choose a number and checks whether it is valid.
    value = chooseCorrectNumber(number)

    #parses the first response to return a recipe object with id and title
    chosen_recipe = json_parser.parseIdAndTitle(recipes, value)

    #api call to get the full recipe information
    recipe_information = spoonacular.getRecipeInformation(chosen_recipe.recipe_id)

    #parses the full recipe information to add the remaining variables like likes, ingredients, instructions etc.
    complete_recipe = json_parser.parseRemainingVariables(recipe_information, chosen_recipe)
    return complete_recipe


def chooseCorrectNumber(number):
    """
    takes the number which has been incremented in the for loop as input and returns the value chosen from the user.
    input: number: int
    :return value: Integer

    """
    #checks whether the user chooses a correct number
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

    return value

def isempty(list):
    """
    this function checks wheter a tuple is empty or not
    :param list: list which is either filled or empty
    :return: boolean: False if it is not empty and true if the tuple is empty
    """
    if not list:
        return False
    else:
        return True

if __name__ == "__main__":
    """starts the programm"""
    #global user who is logged in
    current_user = None

    #prints the welcome message
    welcome()

    #lets the user decide whether he wants to login or signup
    login_or_signup = str(input("Login/Sign up (1/2): "))
    login_status = False

    while login_status is False:
        if login_or_signup == "1":
            #current user will be set to logged in user
            current_user = login()
            login_status = True
        elif login_or_signup == "2":
            #current user will be set to the new user
            current_user = signUp()
            login_status = True
        else:
            print("")
            print("Please enter either 1 or 2")
            print("")
            login_or_signup = str(input("Login/Sign up (1/2): "))

    #presents all the available options
    #presentOptions()

    #runs the program as long as is_finished is false
    is_finished = False

    while is_finished != True:
        is_finished = checkUserInput(current_user)
