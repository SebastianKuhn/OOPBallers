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


def checkifUserRecipeAlreadyExists(user_id, recipe_id):
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

def checkifRecipeInstructionAlreadyExists(recipe, instruction):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    RecipeInstructionCheckQuery = "SELECT * FROM recipe_step WHERE recipe_id = %s and number = %s and step = %s;"
    try:
        cursor.execute(RecipeInstructionCheckQuery, (recipe.recipe_id, instruction.number, instruction.step))
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addRecipeInstructionText(recipe, instruction):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    RecipeInstrucitonInsertQuery = """INSERT into recipe_step (recipe_id, number, step)  VALUES (%s, %s, %s)"""
    check = checkifRecipeInstructionAlreadyExists(recipe.recipe_id, instruction.number, instruction.step)
    if check == ():
        try:
            cursor.execute(RecipeInstrucitonInsertQuery, (user.user_id, recipe.recipe_id))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass

#addRecipetoUser(43, 606643)

result = checkifUserRecipeAlreadyExists(44, 101141)

print(result)

db = db_helpers.getDbCon()
print(db)
cursor = db.cursor()
print(cursor)
userRecipeInsertQuery = """INSERT into user_recipes (user_id, recipe_id) VALUES (%s, %s)"""
check = result
if check == ():
    try:
        cursor.execute(userRecipeInsertQuery, (44, 101141))
        print(cursor.fetchall())
        db.commit()
    except Exception:
        print('Error: unable to execute!')
    finally:
        cursor.close()
        db.close()
else:
    pass