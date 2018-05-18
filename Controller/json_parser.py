from Models.recipe import Recipe
from Models.ingredient import Ingredient
from Models.instruction import Instruction
from Models.equipment import Equipment


def parseIdAndTitle(json_response, value):
    value -= 1
    recipe_id = json_response[value].get("id")
    title = json_response[value].get("title")

    chosen_recipe = Recipe(recipe_id, title)

    return chosen_recipe


def parseRemainingVariables(json_response, recipe):
    ready_in_minutes = json_response.get("readyInMinutes")
    recipe.ready_in_minutes = ready_in_minutes

    servings = json_response.get("servings")
    recipe.servings = servings

    vegetarian = json_response.get("vegetarian")
    recipe.vegetarian = vegetarian

    source_url = json_response.get("sourceUrl")
    recipe.source_url = source_url

    aggregate_likes = json_response.get("aggregateLikes")
    recipe.aggregate_likes = aggregate_likes

    health_score = json_response.get("healthScore")
    recipe.health_score = health_score

    ingredients = []

    if json_response.get("extendedIngredients") is not None:
        for ingr in json_response.get("extendedIngredients"):
            name = ingr.get("name")
            ingredient_id = ingr.get("id")
            amount = ingr.get("amount")
            unit = ingr.get("unit")

            ingredient = Ingredient(name, ingredient_id, amount, unit)
            ingredients.append(ingredient)

        recipe.ingredients = ingredients

    instructions = []

    if json_response.get("analyzedInstructions") is not None:
        if json_response.get("analyzedInstructions")[0].get("steps") is not None:
            for instr in json_response.get("analyzedInstructions")[0].get("steps"):
                number = instr.get("number")
                step = instr.get("step")

                ingred = []

                for json_ingred in instr.get("ingredients"):
                    for saved_ingred in ingredients:
                        if saved_ingred.name == json_ingred.get("name"):
                            ingred.append(saved_ingred)

                equipments = []

                for equip in instr.get("equipment"):
                    name = equip.get("name")

                    equipment = Equipment(name)

                    equipments.append(equipment)

                instruction = Instruction(number, step, ingred, equipments)

                instructions.append(instruction)

            recipe.instructions = instructions

    return recipe