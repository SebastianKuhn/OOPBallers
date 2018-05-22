"""
This file serves as "master"-helpers file and contains the functions that are executed in the frontend to add a
recipe to the database, save a new recipe to the user's account or get all the recipe informations of a recipe.
"""
from helpers import equipment_helpers, instruction_helpers, ingredient_helpers, recipe_helpers
from Models.recipe import Recipe
from Models.ingredient import Ingredient
from Models.equipment import Equipment
from Models.instruction import Instruction

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
    ingred = []
    recipe = Recipe(recipe_id, " ") #created object in order to get the correct input, sorry for the bad coding

    recipe_instruction_ids = []
    for instr_tuple in instruction_helpers.getRecipeInstructionID(recipe):
        recipe_instruction_ids.append(instr_tuple[0])
    ingredient_ids = ingredient_helpers.getIngredientIdsForRecipe(recipe_id)

    #inefficient code to create all ingredients of the recipe.
    for ingredient_id in ingredient_ids:
        for recipe_instruction_id in recipe_instruction_ids:
            if len(ingredient_helpers.getAmountAndUnitForIngredient(ingredient_id, recipe_instruction_id)) != 0:
                ingredient_name = ingredient_helpers.getIngredientNameById(ingredient_id)
                amount = ingredient_helpers.getAmountAndUnitForIngredient(ingredient_id, recipe_instruction_id)[0][0]
                unit = ingredient_helpers.getAmountAndUnitForIngredient(ingredient_id, recipe_instruction_id)[0][1]
                ingredient_object = Ingredient(ingredient_name, ingredient_id, amount, unit)
                ingred.append(ingredient_object)
                break


    #get instructions
    instructions = []
    recipe_instructions = instruction_helpers.getInstructionByRecipeId(recipe_id)

    for instruction in recipe_instructions:
        instruction_id = instruction[0]
        instruction_nr = instruction[2]
        step = instruction[3]

        ingredients = []

        ingredient_ids = ingredient_helpers.getIngredientIdByInstructionId(instruction_id)

        for ingredient in ingred:
            if isempty(ingredient_ids) is not True:
                for id in ingredient_ids:
                    if ingredient.ingredient_id == id:
                        ingredients.append(ingredient)

        equipments = []

        equipment_ids = equipment_helpers.getEquipmentByInstructionId(instruction_id)

        if isempty(equipment_ids) is not True:
            for id in equipment_ids:
                equipment_tuple = equipment_helpers.getEquipmentByEquipmentId(id)
                if isempty(equipment_tuple) is not True:
                    for equipment in equipment_tuple:
                        id = equipment[0]
                        name = equipment[1]

                        equi = Equipment(name, id)
                        equipments.append(equi)

        instruct = Instruction(instruction_nr, step, ingredients, equipments)
        instructions.append(instruct)

    return Recipe(recipe_id, title, ready_in_minutes, servings, vegetarian, source_url, aggregate_likes, health_score,
                  ingred, instructions)

def isempty(tuple):
    if tuple:
        return False
    else:
        return True