import MySQLdb
from configparser import ConfigParser
import db_helpers as helpers

def newRecipe(re_id, re_title, re_readyinmin, re_servings, re_vegi, re_url, re_aggr, re_health_sc):
    db = helpers.getDbCon()
    cursor = db.cursor()
    recipeInsertQuery = """INSERT IGNORE into recipes (recipe_id, title,
                            ready_in_minutes, servings, vegetarian, source_url, aggregate_likes, health_score)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
    try:
        cursor.execute(recipeInsertQuery, (re_id, re_title, re_readyinmin, re_servings, re_vegi, re_url, re_aggr, re_health_sc))
        db.commit()
    except Exception:
        return "OOPs"
    finally:
        cursor.close()
        db.close()

def addRecipetoUser(user_id, recipe_id):
    db = helpers.getDbCon()
    cursor = db.cursor()
    userRecipeInsertQuery = """INSERT IGNORE into recipes (user_id, recipe_id)
                                    VALUES (%s, %s) 
                                    WHERE NOT EXISTS (
                                        SELECT * FROM user_recipes WHERE recipe_id = "recipe_id AND user_id = user_id) 
                                        LIMIT 1;"""
    try:
        cursor.execute(userRecipeInsertQuery, (user_id, recipe_id))  # to replace s% put in quotation markes
        db.commit()
    except Exception:
        return 'Error: unable to execute!'
    finally:
        cursor.close()
        db.close()