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
        return "OOPs"
    finally:
        cursor.close()
        db.close()


def checkifUserRecipeAlreadyExists(user, recipe):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeCheckQuery = "SELECT * FROM user_recipes WHERE user_id = %s and recipe_id = %s;"
    try:
        cursor.execute(userRecipeCheckQuery, (user.user_id, recipe.recipe_id))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addRecipetoUser(user, recipe):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeInsertQuery = """INSERT into user_recipes (user_id, recipe_id) VALUES (%s, %s)"""
    check = checkifUserRecipeAlreadyExists(user.user_id, recipe.recipe_id)
    if check == ():
        try:
            cursor.execute(userRecipeInsertQuery, (user.user_id, recipe.recipe_id))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass

def checkifRecipeStepAlreadyExists(recipe, instruction)):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeStepCheckQuery = "SELECT * FROM recipe_step WHERE recipe_id = %s and number = %s and step = %s;"
    try:
        cursor.execute(userRecipeStepCheckQuery, (recipe.recipe_id, instruction.number, instruction.step))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addRecipeInstructionText(recipe, instruction):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeInsertQuery = """INSERT into recipe_step (recipe_id, number, step)  VALUES (%s, %s, %s)"""
    check = checkifUserRecipeAlreadyExists(recipe.recipe_id, instruction.number, instruction.step)
    if check == ():
        try:
            cursor.execute(userRecipeInsertQuery, (user.user_id, recipe.recipe_id))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass