"""
This file serves as "master"-helpers file and contains the functions that are executed in the frontend to either add a
Recipe to the database or save a new recipe to the user's account.
"""
from helpers import equipment_helpers, instruction_helpers, ingredient_helpers, recipe_helpers

def master_addRecipe(recipe):
    """
    Combines functions from the equipment, ingredient and recipe helpers files. If executed, all details of a recipe
    are saved to the corresponding tables in the database. The tables are "recipes", "equipments", "ingredients",
    "recipe_instructions", "recipe_ingredients" and "recipe_equipment".
    :param recipe: object of the class recipe
    :return: adds data to database
    """
    # all functions inside this function already have try and except statements built-in. That's why no
    # try and except statement is used here.
    check = recipe_helpers.checkifRecipeAlreadyExists(recipe)

    # these functions work with INSERT IGNORE and thus don't need to be in the conditional.
    recipe_helpers.newRecipe(recipe)
    ingredient_helpers.newIngredient(recipe)
    equipment_helpers.newEquipment(recipe)

    if check == ():
        instruction_helpers.addRecipeInstructionText(recipe)
        print("I'm starting the function now!")
        ingredient_helpers.addIngredienttoRecipe(recipe)
        print("The function has been ran!")
        equipment_helpers.addEquipmenttoRecipe(recipe)

    else:
        pass

def master_addRecipetoUser(user_id, recipe):
    """
    Combines functions from the equipment, ingredient and recipe helpers files. If executed, a recipe is saved to a
    user's account. Additionally, to gain further insights out of user data collection, equipment and ingredients
    used by a user are added to it's account as well.
    :param user_id: the unique user_id, auto-incremented by the database
    :param recipe: object of the class recipe
    :return: adds data to database
    """

    # all functions inside this function already have try and except statements built-in. That's why no
    # try and except statement is used here.
    check = recipe_helpers.checkifUserRecipeAlreadyExists(user_id, recipe.recipe_id)

    if check == ():
        recipe_helpers.addRecipetoUser(user_id, recipe)
        equipment_helpers.addEquipmenttoUser(user_id, recipe)
        ingredient_helpers.addIngredienttoUser(user_id, recipe)

    else:
        pass

