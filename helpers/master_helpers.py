"""
This file serves as "master"-helpers file and contains the functions that are executed in the frontend to either add a
Recipe to the database or save a new recipe to the user's account.
"""
from helpers import equipment_helpers, instruction_helpers, ingredient_helpers, recipe_helpers

def master_addRecipe(recipe):
    """
    Combines functions from the equipment, ingredient and recipe helpers files. If executed, all details of a recipe
    are saved to the corresponding tables in the database. The tables are "recipes", "equipments", "ingredients" and
    "recipe_instructions".
    :param recipe: object of the class recipe
    :return: adds data to database
    """
    recipe_helpers.newRecipe(recipe)
    ingredient_helpers.newIngredient(recipe)
    equipment_helpers.newEquipment(recipe)
    instruction_helpers.addRecipeInstructionText(recipe)

def master_addRecipetoUser(user_id, equipment, recipe, insgredient):

