from helpers import db_helpers


def checkifRecipeAlreadyExists(recipe):
    """
    Takes the recipe_id and checks if the recipe of which we want to add the instructions to the instruction table
    was already inserted in the table before.
    :param recipe: object of class recipe
    :return: Returns result from SELECT statement
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeCheckQuery = "SELECT * FROM recipes_instructions WHERE  recipe_id = %s;"
    try:
        cursor.execute(userRecipeCheckQuery, recipe.recipe_id)  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"
    finally:
        cursor.close()
        db.close()


def addRecipeInstructionText(recipe):
    """
    Uses checkifRecipeAlreadyExists() function to verify that the recipe text wasn't added to the "recipe_instructions"
    table before. If this is not the case, the instructions of the input recipe are added to the "recipe_instructions"
    table.
    :param recipe: object of class recipe
    :return: adds data to database
    """

    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeInstructionInsertQuery = """INSERT into recipe_insructions (recipe_id, number, step)  VALUES (%s, %s, %s)"""
    check = checkifRecipeAlreadyExists(recipe.recipe_id)
    if check == ():
        try:
            for instr in recipe.instructions:
                cursor.execute(recipeInstructionInsertQuery, (recipe.recipe_id, instr.number, instr.step))
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass