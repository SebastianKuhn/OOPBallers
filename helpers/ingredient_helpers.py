"""
In this file all the functions to add the ingredients from the API response to the database are saved.
"""
from helpers import db_helpers
from Models.recipe import Recipe
from Models.ingredient import Ingredient
from Models.instruction import Instruction
from Models.equipment import Equipment

# for ingredients table
def newIngredient(recipe):
    """
    Takes a recipe and puts all ingredients used into the equipment table of the database
    :param recipe: object of the class recipe
    :return: nothing
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    ingredientInsertQuery = "INSERT IGNORE into ingredients (ingredient_id, name) VALUES (%s, %s);"
    try:
        for ingr in recipe.ingredients:
            cursor.execute(ingredientInsertQuery, (ingr.ingredient_id, ingr.name))
        db.commit()
    except Exception:
        return "OOPs something went wrong"
    finally:
        cursor.close()
        db.close()

# for recipe_ingredients table

def addIngredienttoRecipe(recipe):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeIngredientInsertQuery = """INSERT into recipe_ingredients (recipe_id, number, ingredient_id, amount, unit) VALUES (%s, %s, %s, %s, %s)"""
    try:
        for instr in recipe.instructions:
            gen = (ingr for ingr in recipe.ingredients if ingr.name in instr.ingredients)
            for ingr in gen:
                cursor.execute(recipeIngredientInsertQuery, (recipe.recipe_id, instr.number, ingr.ingredient_id,
                                                     ingr.amount, ingr.unit))  # to replace s% put in quotation markes
        db.commit()
    except Exception:
        return 'Error: unable to execute!'
    finally:
        cursor.close()
        db.close()

def addIngredienttoUser(user_id, recipe):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userIngredientInsertQuery = """INSERT into user_ingredients (user_id, ingredient_id) VALUES (%s, %s)"""

    try:
        for ingr in recipe.ingredients:
            cursor.execute(userIngredientInsertQuery, (user_id, ingr.ingredient_id))  # to replace s% put in quotation markes
            db.commit()
    except Exception:
        return 'Error: unable to execute!'
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":

    equipments = []
    werkzeug1 = Equipment("Pfanne", 323)
    werkzeug2 = Equipment("Messer", 1234)
    equipments.append(werkzeug1)
    equipments.append(werkzeug2)

    ingredients =[]
    Zutat1 = Ingredient("Pfeffer", 20, 300.6, "gram")
    Zutat2 = Ingredient("Knoblauch", 324, 2, "Zehen")
    print(Zutat2.ingredient_id)
    ingredients.append(Zutat1)
    ingredients.append(Zutat2)
    print(ingredients[0].ingredient_id)
    Beschreibung = Instruction(1, "hallo", equipments, ingredients)


    rezept = Recipe(50, "test", 20, 5, True, "www.url.ch", 323, 66, ingredients,Beschreibung)
    print(rezept.ingredients[0].ingredient_id)
    print(type(rezept.ingredients[0].ingredient_id))
    print(type(rezept.ingredients))
    print(len(rezept.ingredients))