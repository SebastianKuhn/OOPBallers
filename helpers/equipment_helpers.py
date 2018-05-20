from helpers import db_helpers

def newEquipment(recipe):
    """
    Takes a recipe and puts all equipments used into the equipment table of the database
    :param recipe: object of the class recipe
    :return: adds data to the database
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    equipmentInsertQuery = """INSERT IGNORE into equipment (equipment_id, equipment_name) VALUES (%s, %s);"""
    try:
        for instr in recipe.instructions:
            for equip in instr.equipment:
                cursor.execute(equipmentInsertQuery, (equip.equipment_id, equip.equipment_name))
        db.commit()
    except Exception:
        print("Error: OOPs something went wrong while adding new equipment to the database")
    finally:
        cursor.close()
        db.close()


def addEquipmenttoRecipe(recipe):
    """
    Takes a recipe and puts all equipments used into the recipe_equipment table of the database
    :param recipe: object of the class recipe
    :return: adds data to the database
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeEquipmentInsertQuery = """INSERT into recipe_equipment (recipe_id, instruction_number, equipment_id) VALUES (%s, %s, %s)"""
    try:
        for instr in recipe.instructions:
            for equip in instr.equipment:
                cursor.execute(recipeEquipmentInsertQuery, (recipe.recipe_id, instr.instruction_number, equip.equipment_id))
        db.commit()
    except Exception:
        print('Error: OOPs something went wrong while adding Equipment to a user!'
    finally:
        cursor.close()
        db.close()


def addEquipmenttoUser(user_id, recipe):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userEquipmentInsertQuery = """INSERT into user_equipment (user_id, equipment_id) VALUES (%s, %s)"""
    try:
        for instr in recipe.instructions:
            for equip in instr.equipments:
                cursor.execute(userEquipmentInsertQuery, (user_id, equip.equipment_id))  # to replace s% put in quotation markes
        db.commit()
    except Exception:
        return 'Error: unable to execute!'
    finally:
        cursor.close()
        db.close()