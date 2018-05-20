from helpers import db_helpers

def newEquipment(recipe):
    """
    Takes a recipe and puts all equipments used into the equipment table of the database
    :param recipe: object of the class recipe
    :return: nothing
    """
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    equipmentInsertQuery = "INSERT IGNORE into equipment (equipment_id, name) VALUES (%s, %s);"
    try:
        for instr in recipe.instructions:
            for equip in instr.equipments:
                cursor.execute(equipmentInsertQuery, (equip.equipment_id, equip.equipment_name))
        db.commit()
    except Exception:
        return "OOPs"
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


def addEquipmenttoRecipe(recipe):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeEquipmentInsertQuery = """INSERT into recipe_equipment (recip_id, equipment_id) VALUES (%s, %s)"""
    try:
        for instr in recipe.instructions:
            for equip in instr.equipments:
                cursor.execute(recipeEquipmentInsertQuery, (recipe.recipe_id, equip.equipment_id))  # to replace s% put in quotation markes
        db.commit()
    except Exception:
        return 'Error: unable to execute!'
    finally:
        cursor.close()
        db.close()