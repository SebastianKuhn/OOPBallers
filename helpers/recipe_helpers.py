import MySQLdb
from configparser import ConfigParser
import db_helpers as helpers

def newRecipe(re_id, re_title, re_readyinmin, re_servings, re_vegi, re_url, re_aggr, re_health_sc):
    db = helpers.getDbCon()
    cursor = db.cursor()
    recipeInsertQuery = "INSERT into recipes (recipe_id, title, ready_in_minutes, servings, vegetarian, source_url, aggregate_likes, health_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    # try:
    cursor.execute(recipeInsertQuery, (re_id, re_title, re_readyinmin, re_servings, re_vegi, re_url, re_aggr, re_health_sc))
    db.commit()
    print("Successfully added the recipe " + re_title)

