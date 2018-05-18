"""
In this file all the functions to add the ingredients from the API response to the database are saved.
"""
from helpers import db_helpers
from Models.ingredient import Ingredient

# for ingredients table
def newIngredient(ingredient):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    ingredientInsertQuery = "INSERT IGNORE into ingredients (ingredient_id, name) VALUES (%s, %s);"
    try:
        cursor.execute(ingredientInsertQuery, (ingredient.ingredient_id, ingredient.name))
        db.commit()
    except Exception:
        return "OOPs something went wrong"
    finally:
        cursor.close()
        db.close()

# for recipe_ingredients table
# the number is the step in in which the ingredient is used
def addIngredientToRecipe(ingredient, recipe, instruction):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    ingredientInsertQuery = "INSERT into ingredients (recipe_id, number, ingredient_id, amount, unit) VALUES (%s, %s, %s, %s, %s);"
    try:
        cursor.execute(ingredientInsertQuery, (recipe.recipe_id, instruction.number, ingredient.ingredient_id, ingredient.amount, ingredient.unit))
        db.commit()
    except Exception:
        return "OOPs something went wrong"
    finally:
        cursor.close()
        db.close()

# for user_ingredients table
def checkifUserIngredientAlreadyExists(user_id, ingredient_id):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userIngredientCheckQuery = "SELECT * FROM user_ingredients WHERE user_id = %s and ingredient_id = %s;"
    try:
        cursor.execute(userIngredientCheckQuery, (user_id, ingredient_id))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addIngredienttoUser(user_id, ingredient_id):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userIngredientInsertQuery = """INSERT into user_recipes (user_id, ingredient_id) VALUES (%s, %s)"""
    check = checkifIngredientAlreadyExists(user_id, ingredient_id)
    if check == ():
        try:
            cursor.execute(userIngredientInsertQuery, (user_id, ingredient_id))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass


coffee = Ingredient("coffee", 2, 4.5, "cups")
