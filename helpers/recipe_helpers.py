from helpers import db_helpers

def newRecipe(recipe):
    """
    This function adds a new recipe to the database' recipes table.
    :param recipe: takes and object of the class recipe
    :return: nothing
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeInsertQuery = "INSERT IGNORE into recipes (recipe_id, title, ready_in_minutes, servings, vegetarian, " \
                        "source_url, aggregate_likes, health_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    try:
        cursor.execute(recipeInsertQuery, (recipe.recipe_id, recipe.title, recipe.ready_in_minutes, recipe.servings,
                                           recipe.vegetarian, recipe.source_url, recipe.aggregate_likes,
                                           recipe.health_score))
        db.commit()

    except Exception:
        return "OOPs something went wrong"
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
        return "Error: OOPs something went wrong!"

def addRecipetoUser(user_id, recipe):
    """
    This function is used to add recipes to the personal user accounts. It uses the function
    checkifUserRecipeAlreadyExists() to check if the recipe is already saved.

    :param user_id: Takes the user_id of a specific user
    :param recipe_id: Takes the recipe_id of a specific recipe
    :return: nothing
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeInsertQuery = """INSERT into user_recipes (user_id, recipe_id) VALUES (%s, %s)"""
    check = checkifUserRecipeAlreadyExists(user_id, recipe.recipe_id)
    if check == ():
        try:
            cursor.execute(userRecipeInsertQuery, (user_id, recipe.recipe_id))
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass
