"""
In this file all the functions to add the recipes from the API response to the database are saved.
"""
from helpers import db_helpers

def newRecipe(recipe):
    """
    This function adds a new recipe to the database' recipes table.
    :param recipe: takes and object of the class recipe
    :return: nothing
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeInsertQuery = "INSERT into recipes (recipe_id, title, ready_in_minutes, servings, vegetarian, " \
                        "source_url, aggregate_likes, health_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON Duplicate KEY UPDATE recipe_id = recipe_id;"
    try:
        cursor.execute(recipeInsertQuery, (recipe.recipe_id, recipe.title, recipe.ready_in_minutes, recipe.servings,
                                           recipe.vegetarian, recipe.source_url, recipe.aggregate_likes,
                                           recipe.health_score))
        db.commit()

    except Exception:
        print("ERROR: OOPs something went wrong while adding the new recipe to recipe table")
    finally:
        cursor.close()
        db.close()


def checkifUserRecipeAlreadyExists(user_id, recipe_id):
    """
    This function is used to check if a user already saved a distinct recipe in his personal account. (i.e. the
    user_recipes table. It is used in the function addRecipetoUser().
    :param user_id: Takes the user_id of a specific user
    :param recipe_id: Takes the recipe_id of a specific recipe
    :return: returns a variable that holds the Output from the SELECT statement
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeCheckQuery = "SELECT * FROM user_recipes WHERE user_id = %s and recipe_id = %s;"
    try:
        cursor.execute(userRecipeCheckQuery, (user_id, recipe_id))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        print("Error: OOPs something went wrong while checking if the user has already saved the recipe!")
    finally:
        cursor.close()
        db.close()

def addRecipetoUser(user_id, recipe):
    """
    This function is used to add recipes to the personal user accounts.

    :param user_id: Takes the user_id of a specific user
    :param recipe_id: Takes the recipe_id of a specific recipe
    :return: nothing
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeInsertQuery = """INSERT into user_recipes (user_id, recipe_id) VALUES (%s, %s)"""

    try:
        cursor.execute(userRecipeInsertQuery, (user_id, recipe.recipe_id))
        db.commit()
    except Exception:
        print('Error: OOPs something went wrong while adding the recipe to the user!')
    finally:
        cursor.close()
        db.close()


def checkifRecipeAlreadyExists(recipe):
    """
    Takes the recipe_id and checks if the recipe of which we want to add the instructions to the instruction table
    was already inserted in the recipe table before.
    :param recipe: object of class recipe
    :return: Returns result from SELECT statement
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeCheckQuery = "SELECT * FROM recipes WHERE recipe_id = %s;"
    try:
        cursor.execute(userRecipeCheckQuery, (recipe.recipe_id,))
        result = cursor.fetchall()
        return result

    except Exception:
        print("Error: OOPs something went wrong in checking if the record already exists!")
    finally:
        cursor.close()
        db.close()

def getRecipeIds(user):
    """
    Takes a user as the input and returns a list with all of the user's recipe ids.
    :param user: object of class User
    :return: list of integers
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeTitlesQuery = "SELECT recipe_id FROM user_recipes WHERE user_id = %s;"
    try:
        cursor.execute(userRecipeTitlesQuery, (user.user_id,))
        results = cursor.fetchall()
        list_of_recipe_ids = []
        for result in results:
            list_of_recipe_ids.append(result[0])
        return list_of_recipe_ids

    except Exception:
        print("Error: OOPs something went wrong in getting the user's recipe id's!")
    finally:
        cursor.close()
        db.close()


def getRecipeName(recipe_id):
    """
    Takes a recipe id as the input and returns the respective recipe name.
    :param integer
    :return: string
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeNameQuery = "SELECT title FROM recipes WHERE recipe_id = %s;"
    try:
        cursor.execute(recipeNameQuery, (recipe_id,))
        results = cursor.fetchall()
        for result in results:
            return result[0]
    except Exception:
        print("Error: OOPs something went wrong in getting the recipe name.")
    finally:
        cursor.close()
        db.close()


def getRecipeNames(list_of_recipe_ids):
    """
    Takes a list of recipes as the input and gets all his recipe id's which are used to fetch all the recipe names which will
    be returned
    :param list_of_recipe_ids: list of integers
    :return: list of strings
    """
    list_of_recipe_names = []

    for recipe_id in list_of_recipe_ids:
        list_of_recipe_names.append(getRecipeName(recipe_id))

    return list_of_recipe_names


def getRecipeInformation(recipe_id):
    """
    Takes a recipe id and the term that is needed as the input and returns the value of the term.
    :param recipe_id: integer, term: string
    :return: tuple response
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeNameQuery = "SELECT title, ready_in_minutes, servings, vegetarian, source_url, aggregate_likes, health_score " \
                      "FROM recipes WHERE recipe_id = %s;"
    try:
        cursor.execute(recipeNameQuery, (recipe_id,))
        results = cursor.fetchall()
        return results[0]
    except Exception:
        print("Error: OOPs something went wrong in getting information of " + term + ".")
    finally:
        cursor.close()
        db.close()

