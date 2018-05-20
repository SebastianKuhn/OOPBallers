from helpers import db_helpers


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
    recipeInstructionInsertQuery = """INSERT into recipe_step (recipe_id, number, step)  VALUES (%s, %s, %s)"""
    check = checkifRecipeInstructionAlreadyExists(recipe.recipe_id, instruction.number, instruction.step)
    if check == ():
        try:
            cursor.execute(recipeInstructionInsertQuery, (recipe.recipe_id, instruction.number, instruction.step))
            # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass