"""
In this file all the functions to add the recipe instructions from the API response to the database are saved.
"""

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
    recipeInstructionInsertQuery = """INSERT into recipe_instructions (recipe_id, instruction_number, step) VALUES (%s, %s, %s)"""
    try:
        for instr in recipe.instructions:
            instr.step.encode('utf-8')
            cursor.execute(recipeInstructionInsertQuery, (recipe.recipe_id, instr.instruction_number, instr.step))
        db.commit()
    except Exception:
        print("Error: OOPs something went wrong while adding instruction text to a recipe!")
    finally:
        cursor.close()
        db.close()

def getRecipeInstructionID(recipe):
    """
    uses a recipe as an input and gets the recipe_instruction_ids for the corresponding recipe
    :param recipe: object of class recipe
    :return: recipe_instruction_ids: list of integers
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeInstructionIdQuery = "SELECT recipe_instruction_id FROM recipe_instructions WHERE recipe_id = %s"
    try:
        cursor.execute(recipeInstructionIdQuery, (recipe.recipe_id,))
        recipe_instruction_id = cursor.fetchall()
        return recipe_instruction_id
    except Exception:
        return "Oh Snap, this didn't work!"
    finally:
        cursor.close()
        db.close()


def getInstructionByRecipeId(recipe_id):
    """
    gets the instruction of a certain recipe by its id
    :param recipe_id: int
    :return:
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeInstructionIdQuery = "SELECT * FROM recipe_instructions WHERE recipe_id = %s"
    try:
        cursor.execute(recipeInstructionIdQuery, (recipe_id,))
        recipe_instruction = cursor.fetchall()
        return recipe_instruction
    except Exception:
        return "Oh Snap, this didn't work!"
    finally:
        cursor.close()
        db.close()