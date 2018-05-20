"""
In this file all the functions to add the ingredients from the API response to the database are saved.
"""
from helpers import db_helpers

# for ingredients table
def newIngredient(recipe):
       """
    Takes a recipe and puts all ingredients used into the equipment table of the database
    :param recipe: object of the class recipe
    :return: nothing
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    ingredientInsertQuery = "INSERT IGNORE into ingredients (ingredient_id, name) VALUES (%s, %s);"
    try:
        for ingr in recipe.ingredients:
            cursor.execute(ingredientInsertQuery, (ingr.ingredient_id, ingr.name))
        db.commit()
    except Exception:
        return "OOPs something went wrong"
    finally:
        cursor.close()
        db.close()

# for recipe_ingredients table
# the number is the step in in which the ingredient is used
def checkifRecipeIngredientAlreadyExists(recipe, ingredient, instruction):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeIngredientCheckQuery = """SELECT * FROM recipe_ingredients 
                          WHERE recipe_id = %s and number = %s and ingredient_id = %s and amount = %s and unit = %s;"""
    try:
        cursor.execute(recipeIngredientCheckQuery, (recipe.recipe_id, instruction.number, ingredient.ingredient_id, ingredient.amount, ingredient.unit))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addIngredienttoRecipe(recipe, ingredient, instruction):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeIngredientInsertQuery = """INSERT into recipe_ingredients (recipe_id, number, ingredient_id, amount, unit) VALUES (%s, %s, %s, %s, %s)"""
    check = checkifRecipeIngredientAlreadyExists(recipe, ingredient, instruction)
    if check == ():
        try:
            cursor.execute(recipeIngredientInsertQuery, (recipe.recipe_id, instruction.number, ingredient.ingredient_id, ingredient.amount, ingredient.unit))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass

# for user_ingredients table
def checkifUserIngredientAlreadyExists(user, ingredient):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userIngredientCheckQuery = "SELECT * FROM user_ingredients WHERE user_id = %s and ingredient_id = %s;"
    try:
        cursor.execute(userIngredientCheckQuery, (user.user_id, ingredient.ingredient_id))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addIngredienttoUser(user, ingredient):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userIngredientInsertQuery = """INSERT into user_recipes (user_id, ingredient_id) VALUES (%s, %s)"""
    check = checkifUserIngredientAlreadyExists(user.user_id, ingredient.ingredient_id)
    if check == ():
        try:
            cursor.execute(userIngredientInsertQuery, (user.user_id, ingredient.ingredient_id))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass

