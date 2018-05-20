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


def checkifUserEquipmentAlreadyExists(user, equipment):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeCheckQuery = "SELECT * FROM user_equipment WHERE user_id = %s and equipment_id = %s;"
    try:
        cursor.execute(userRecipeCheckQuery, (user.user_id, equipment.equipment_id))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addEquipmenttoUser(user, equipment):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userEquipmentInsertQuery = """INSERT into user_equipment (user_id, equipment_id) VALUES (%s, %s)"""
    check = checkifUserEquipmentAlreadyExists(user.user_id, equipment.equipment_id)
    if check == ():
        try:
            cursor.execute(userEquipmentInsertQuery, (user.user_id, equipment.equipment_id))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass

def checkifRecipeEquipmentAlreadyExists(recipe, equipment):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeEquipmentCheckQuery = "SELECT * FROM recipe_equipment WHERE recipe_id = %s and equipment_id = %s;"
    try:
        cursor.execute(recipeEquipmentCheckQuery, (recipe.recipe_id, equipment.equipment_id))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addEquipmenttoRecipe(recipe, equipment):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeEquipmentInsertQuery = """INSERT into recipe_equipment (recip_id, equipment_id) VALUES (%s, %s)"""
    check = checkifRecipeEquipmentAlreadyExists(recipe.recipe_id, equipment.equipment_id)
    if check == ():
        try:
            cursor.execute(recipeEquipmentInsertQuery, (recipe.recipe_id, equipment.equipment_id))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass

def getEquipmentId(equipment):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    equipmentIdQuery = "SELECT equipment_id FROM equipments WHERE username = %s"
    cursor.execute(equipmentIdQuery, (equipment.name,))
    equipment_id = cursor.fetchone()
    return equipment_id