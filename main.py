from Controller import googlevision, spoonacular
import hashlib, uuid
from Models.user import User


def welcome():
    """starts the program and welcomes the user"""

    print("""

                 \ \  / /                                                  ___         ___
                  \ \/ /           _   __      _   __     //             //   ) )    //   ) )
                   \/ / //   / / // ) )  ) ) // ) )  ) ) // //   / /      __ / /    //   / /
                   / / //   / / // / /  / / // / /  / / // ((___/ /          ) )   //   / /
                  / / ((___( ( // / /  / / // / /  / / //      / /     ((___/ / . ((___/ /
                                                              / /
                                                             / /
            
            """)
    print("Welcome to Yummly, you're tool to search recipes by snapping pictures of the ingredients the fridge!")
    print("")
    print("")
    print("Please choose to either log in if you already have an account or sign up if you do not.")
    print("")


def login():
    """prompts the user to login and checks the credentials in the database"""
    print("")

    correct_login = False

    while correct_login != True:
        username = input("username: ")
        password = input("password: ")

        # check username and password in the database using the database controller -> if clause following
        # check password => hash function in the database controller

        correct_login = True


    print("")
    print("You successfully logged in")
    print("")

    #return user


def signUp():
    """prompts the user to define a username and a password. The username will be checked in the
    database whether it is still available"""
    print("")

    username_available = False

    while username_available != True:
        username = input("Please enter a username: ")

        # check username against database using the database controller



    password = input("Please enter a passwort: ")

    #hash password
    hashed_password = hash_password(password)

    #create User
    user = User(username, hashed_password)


    print("")
    print("You successfully created an account!")
    print("")

    return user


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def presentOptions():
    """presents all the available options"""

    print("Please enter the number of one of the following options:")
    print("1. Search a new recipe using pictures")
    print("2. Search recipes by name")
    print("3. Get all your recipes")
    print("'info' to get information on all options")
    print("'end' to end the program")
    print("")


def checkUserInput():
    """checks the user input and matches it with the available options"""

    user_input = str(input("What would you like to do? "))

    if user_input == "1":
        searchNewRecipes()

    elif user_input == "2":
        print("")
        print("search Recipe by name")
        print("")

    elif user_input == "3":
        print("")
        print("get your recipes")
        print("")

    elif user_input == "info":
        presentOptions()

    elif user_input == "end":
        return True

    else:
        print("")
        print("Please enter a valid number. If you need further information type: info")
        print("")

def searchNewRecipes():
    """asks the user for a folder file path, analyzes the pictures and prints the ingredients as well as possible
    recipes"""

    print("")
    folder_path = str(input("Please insert the file path of your folder containing all the pictures:  "))
    list_of_image_paths = googlevision.scanFolderforPictures(folder_path)

    # list of recognized ingredients
    recognized_ingredients = []

    for image_path in list_of_image_paths:
        recognized_ingredients.append(googlevision.identifyNewIngredient(image_path))

    print("")
    print("Your ingredients so far are:")
    print(recognized_ingredients)
    print("")

    spoonacular.getRecipesByIngredient(recognized_ingredients)


if __name__ == "__main__":
    """starts the program"""

    current_user = None

    welcome()

    login_or_signup = str(input("Login/Sign up (1/2): "))
    login_status = False

    while login_status is False:
        if login_or_signup == "1":
            #current_user =
            login()
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
        is_finished = checkUserInput()