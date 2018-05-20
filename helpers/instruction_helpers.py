from helpers import db_helpers


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
    recipeInstructionInsertQuery = """INSERT into recipe_insructions (recipe_id, instruction_number, step)  VALUES (%s, %s, %s)"""
    try:
        for instr in recipe.instructions:
            cursor.execute(recipeInstructionInsertQuery, (recipe.recipe_id, instr.instruction_number, instr.step))
        db.commit()
    except Exception:
        return 'Error: unable to execute!'
    finally:
        cursor.close()
        db.close()