import MySQLdb
from configparser import ConfigParser
from helpers import db_helpers

def newRecipe(recipe):
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

def addRecipetoUser(user_id, recipe_id):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeInsertQuery = """INSERT into user_recipes (user_id, recipe_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE 
                                      user_id = user_id, recipe_id = recipe_id;"""
    try:
        cursor.execute(userRecipeInsertQuery, (user_id, recipe_id))  # to replace s% put in quotation markes
        db.commit()
    except Exception:
        return 'Error: unable to execute!'
    finally:
        cursor.close()
        db.close()
