"""
In this file all the functions to add the ingredients from the API response to the database are saved.
"""
from helpers import db_helpers
from helpers import instruction_helpers

# for ingredients table
def newIngredient(recipe):
    """
    Takes a recipe and puts all ingredients used into the ingredient table of the database
    :param recipe: object of the class recipe
    :return: nothing
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    ingredientInsertQuery = """INSERT into ingredients (ingredient_id, name) VALUES (%s, %s) ON Duplicate KEY UPDATE ingredient_id = ingredient_id;"""
    try:
        for ingr in recipe.ingredients:
            cursor.execute(ingredientInsertQuery, (ingr.ingredient_id, ingr.ingredient_name))
        db.commit()
    except Exception:
        print("OOPs something went wrong while adding new Ingredients to the database!")
    finally:
        cursor.close()
        db.close()

def addIngredienttoRecipeInstruction(recipe):
    """
       Takes a Recipe and puts the ingredients matching to an instruction number into the instruction_ingredients table.
       ATTENTION: This function doesn't return the full list of ingredients. To still have all ingredients matching to
       their origin in the database the function addIngredienttoRecipe() was created (see below).
       :param recipe: object of the class recipe
       :return: adds data to the database
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipe_instruction_id = instruction_helpers.getRecipeInstructionID(recipe)
    instructionIngredientInsertQuery = """INSERT into instruction_ingredient 
                                      (recipe_instruction_id, ingredient_id, amount, unit) VALUES (%s, %s, %s, %s);"""
    try:
        for ind, instr in enumerate(recipe.instructions):
            for ingred in instr.ingredients:
                cursor.execute(instructionIngredientInsertQuery, (recipe_instruction_id[ind][0], ingred.ingredient_id,
                                                            ingred.amount, ingred.unit))
        db.commit()
    except Exception:
        print('Error: OOPs something went wrong while adding ingredients to a recipe instruction!')
    finally:
        cursor.close()
        db.close()

def addIngredienttoRecipe(recipe):
    """
    Takes a recipe and puts every ingredient and the corresponding recipe_id into the recipe_ingredients table.
    :param recipe: opject of class recipe
    :return: add Data to the database
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeIngredientInsertQuery = """INSERT into recipe_ingredients (recipe_id, ingredient_id) VALUES (%s, %s)"""

    try:
        for ingr in recipe.ingredients:
            cursor.execute(recipeIngredientInsertQuery, (recipe.recipe_id, ingr.ingredient_id))
            db.commit()
    except Exception:
        print('Error: OOPs something went wrong while adding ingredients to the recipe!')
    finally:
        cursor.close()
        db.close()


def addIngredienttoUser(user_id, recipe):
    """
    This function is used to add new Ingredients to a user's account. It puts them into the "user_ingredients" table.
    :param user_id: User_id generated by the database
    :param recipe: object of the class recipe
    :return: Adds data to database
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userIngredientInsertQuery = """INSERT into user_ingredients (user_id, ingredient_id) VALUES (%s, %s)"""

    try:
        for ingr in recipe.ingredients:
            cursor.execute(userIngredientInsertQuery, (user_id, ingr.ingredient_id))
            db.commit()
    except Exception:
        print('Error: OOPs something went wrong while adding ingredients to the user!')
    finally:
        cursor.close()
        db.close()


def getIngredientIdsForRecipe(recipe_id):
    """
    This function is used to fetch all the ingredients for a recipe
    :param recipe_id: integer
    :return: ingredient_ids: list of integers
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    ingredientIdForRecipeQuery = "SELECT ingredient_id FROM recipe_ingredients WHERE recipe_id = %s"

    try:
        cursor.execute(ingredientIdForRecipeQuery, (recipe_id,))
        results = cursor.fetchall()
        ingredient_ids = []
        for result in results:
            ingredient_ids.append(result[0])
        return ingredient_ids
    except Exception:
        print('Error: OOPs something went wrong while adding ingredients to the user!')
    finally:
        cursor.close()
        db.close()


def getAmountAndUnitForIngredient(ingredient_id, recipe_instruction_ids):
    """
    This function is used to fetch the amount and the unit for the respective Ingredient
    :param recipe_instruction_id: integer
    :param ingredient_id: integer
    :return: results: tuple with amount and unit
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    amountAndUnitQuery = "SELECT amount, unit FROM instruction_ingredient WHERE ingredient_id = %s and "\
                         "recipe_instruction_id IN "

    #adopted the query string to match the input variables
    s = "(" + ', '.join(['%s'] * len(recipe_instruction_ids)) + ")"
    amountAndUnitQuery += s

    #add both tuples in order to pass them to the execute function
    tupleQuery = (ingredient_id, )
    tupleQuery += recipe_instruction_ids

    try:
        cursor.execute(amountAndUnitQuery, tupleQuery)
        results = cursor.fetchall()
        return results
    except Exception:
        print('Error: OOPs something went wrong while getting the amount and unit!')
    finally:
        cursor.close()
        db.close()


def getIngredientNameById(ingredient_id):
    """
    This function is used to fetch the name of an ingredient
    :param ingredient_id: int
    :return: ingredient_name: string
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    amountAndUnitQuery = "SELECT name FROM ingredients WHERE ingredient_id = %s"

    try:
        cursor.execute(amountAndUnitQuery, (ingredient_id,))
        results = cursor.fetchall()
        ingredient_name = results[0]
        return ingredient_name
    except Exception:
        print('Error: OOPs something went wrong while getting the ingredient name!')
    finally:
        cursor.close()
        db.close()


def getIngredientIdByInstructionId(instruction_id):
    """
    This function is used to fetch the id of the ingredient according to its instruction
    :param instruction_id: int
    :return: ingredient_id: int
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    ingredientIdQuery = "SELECT ingredient_id FROM instruction_ingredient WHERE recipe_instruction_id = %s"

    try:
        cursor.execute(ingredientIdQuery, (instruction_id,))
        results = cursor.fetchall()
        return results
    except Exception:
        print('Error: OOPs something went wrong while getting the ingredient id!')
    finally:
        cursor.close()
        db.close()