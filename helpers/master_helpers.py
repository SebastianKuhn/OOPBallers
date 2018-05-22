"""
This file serves as "master"-helpers file and contains the functions that are executed in the frontend to add a
recipe to the database, save a new recipe to the user's account or get all the recipe informations of a recipe.
"""
from helpers import equipment_helpers, instruction_helpers, ingredient_helpers, recipe_helpers
from Models.recipe import Recipe

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
        ingredient_helpers.addIngredienttoRecipeInstruction(recipe)
        equipment_helpers.addEquipmenttoRecipe(recipe)
        ingredient_helpers.addIngredienttoRecipe(recipe)

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


def master_getRecipeInformation(recipe_id):
    """
    Combines functions from the equipment, ingredient and recipe helpers files. If executed, a all the necessary
    information will be collected to create a recipe object which will be returned.
    :param recipe_id: integer
    :return: recipe: object of class Recipe
    """

    # get general information
    informations = recipe_helpers.getRecipeInformation(recipe_id)

    title = str(informations[0])
    ready_in_minutes = int(informations[1])
    servings = int(informations[2])
    if informations[3] == 0:
        vegetarian = False
    else:
        vegetarian = True
    source_url = str(informations[4])
    aggregate_likes = int(informations[5])
    health_score = int(informations[6])


    #get ingredients
    recipe = Recipe(recipe_id, " ") #created object in order to get the correct input, sorry for the bad coding

    recipe_instruction_ids = ()
    for instr_tuple in instruction_helpers.getRecipeInstructionID(recipe):
        recipe_instruction_ids += instr_tuple
    ingredient_ids = ingredient_helpers.getIngredientIdsForRecipe(recipe_id)

    print(recipe_instruction_ids)
    for ingredient_id in ingredient_ids:
        print(ingredient_helpers.getAmountAndUnitForIngredient(ingredient_id, recipe_instruction_ids))

