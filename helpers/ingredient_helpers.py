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

def addIngredienttoRecipe(recipe):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeIngredientInsertQuery = """INSERT into recipe_ingredients (recipe_id, number, ingredient_id, amount, unit) VALUES (%s, %s, %s, %s, %s)"""
    try:
        for instr in recipe.instructions:
            gen = (ingr for ingr in recipe.ingredients if ingr.name in instr.ingredients)
            for ingr in gen:
                cursor.execute(recipeIngredientInsertQuery, (recipe.recipe_id, instr.number, ingr.ingredient_id,
                                                     ingr.amount, ingr.unit))  # to replace s% put in quotation markes
        db.commit()
    except Exception:
        return 'Error: unable to execute!'
    finally:
        cursor.close()
        db.close()

def addIngredienttoUser(user_id, recipe):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userIngredientInsertQuery = """INSERT into user_recipes (user_id, ingredient_id) VALUES (%s, %s)"""
    
    try:
        for ingr in recipe.ingredients:
            cursor.execute(userIngredientInsertQuery, (user_id, ingr.ingredient_id))  # to replace s% put in quotation markes
            db.commit()
    except Exception:
        return 'Error: unable to execute!'
    finally:
        cursor.close()
        db.close()

