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

def addIngredienttoRecipeInstruction(recipe):
    """
       Takes a Recipe and puts every ingredients and the corresponding into the instruction_ingredients table.
       :param recipe: object of the class recipe
       :return: nothing
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipe_instruction_id = instruction_helpers.getRecipeInstructionID(recipe)
    recipeIngredientInsertQuery = """INSERT into recipe_ingredients 
                                  (recipe_instruction_id, ingredient_id, amount, unit) VALUES (%s, %s, %s, %s);"""
    try:
        for ind, instr in enumerate(recipe.instructions):
            for ingred in instr.ingredients:
                cursor.execute(recipeIngredientInsertQuery, (recipe_instruction_id[ind][0], ingred.ingredient_id,
                                                            ingred.amount, ingred.unit))
        db.commit()
    except Exception:
        print('Error: OOPs something went wrong while adding ingredients to a recipe instruction!')
    finally:
        cursor.close()
        db.close()

def getRecipeInstructionID(recipe):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeInstructionIdQuery = "SELECT recipe_instruction_id FROM recipe_instructions WHERE recipe_id = %s"
    try:
        cursor.execute(recipeInstructionIdQuery, (recipe.recipe_id,))
        recipe_insturcion_id = cursor.fetchall()
        return recipe_insturcion_id
    except Exception:
        return "Oh Snap, this didn't work!"
    finally:
        cursor.close()
        db.close()