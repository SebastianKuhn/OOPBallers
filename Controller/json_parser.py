"""
This file serves as the json parser. Ever funciton which parses a json response is included in this file.
"""

from Models.recipe import Recipe
from Models.ingredient import Ingredient
from Models.instruction import Instruction
from Models.equipment import Equipment


def parseIdAndTitle(json_response, value):
    """
    takes a json response and an int value as an input and gets the id and title of the recipe which are used
    to create a recipe object.
    input: decoded json, int
    :return Recipe
    """
    value -= 1
    recipe_id = json_response[value].get("id")
    title = json_response[value].get("title")

    chosen_recipe = Recipe(recipe_id, title)

    return chosen_recipe


def parseRemainingVariables(json_response, recipe):
    """
    takes a json response and a recipe object as an input and gets the the remaining variables to complete the recipe
    input: decoded json, recipe
    :return recipe
    """
    ready_in_minutes = json_response.get("readyInMinutes")
    recipe.ready_in_minutes = int(ready_in_minutes)

    servings = json_response.get("servings")
    recipe.servings = int(servings)

    vegetarian = json_response.get("vegetarian")
    recipe.vegetarian = bool(vegetarian)

    source_url = json_response.get("sourceUrl")
    recipe.source_url = str(source_url)

    aggregate_likes = json_response.get("aggregateLikes")
    recipe.aggregate_likes = int(aggregate_likes)

    health_score = json_response.get("healthScore")
    recipe.health_score = int(health_score)

    ingredients = []

    #parse all the ingredients and add them to the list of ingredients as a ingredient object
    if json_response.get("extendedIngredients") is not None:
        for ingr in json_response.get("extendedIngredients"):
            ingredient_name = ingr.get("name")
            ingredient_id = ingr.get("id")
            amount = ingr.get("amount")
            unit = ingr.get("unit")

            ingredient = Ingredient(ingredient_name, ingredient_id, amount, unit)
            ingredients.append(ingredient)

        recipe.ingredients = ingredients

    instructions = []

    #parse all the instructions and add them as instruction objects to the instructions list
    if json_response.get("analyzedInstructions") is not None:

        if len(json_response.get("analyzedInstructions")) != 0:

            if json_response.get("analyzedInstructions")[0].get("steps") is not None:

                for instr in json_response.get("analyzedInstructions")[0].get("steps"):
                    instruction_number = instr.get("number")
                    step = instr.get("step")

                    ingred = []

                    for json_ingred in instr.get("ingredients"):
                        for saved_ingred in ingredients:
                            if saved_ingred.ingredient_id == json_ingred.get("id"):
                                ingred.append(saved_ingred)

                    equipments = []

                    for equip in instr.get("equipment"):
                        equipment_name = equip.get("name")
                        equipment_id = equip.get("id")

                        equipment = Equipment(equipment_name, equipment_id)

                        equipments.append(equipment)

                    instruction = Instruction(instruction_number, step, ingred, equipments)

                    instructions.append(instruction)

                recipe.instructions = instructions

    return recipe