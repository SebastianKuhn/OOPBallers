from helpers import equipment_helpers, instruction_helpers, ingredient_helpers, recipe_helpers

def master_addRecipe(recipe, instruction):
    recipe_helpers.newRecipe(recipe)
    ingredient_helpers.newIngredient(recipe)
    equipment_helpers.newEquipment(instruction)


def master_addRecipetoUser(user_id, equipment, recipe, insgredient):

