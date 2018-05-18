from helpers import db_helpers


def newEquipment(Equipment):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    equipmentInsertQuery = "INSERT IGNORE into recipes (equipment) VALUES (%s);"
    try:
        cursor.execute(equipmentInsertQuery, (Equipment.name))
        db.commit()
    except Exception:
        return "OOPs"
    finally:
        cursor.close()
        db.close()


def checkifUserEquipmentAlreadyExists(user_id, equipment_id):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userRecipeCheckQuery = "SELECT * FROM user_equipment WHERE user_id = %s and equipment_id = %s;"
    try:
        cursor.execute(userRecipeCheckQuery, (user_id, equipment_id))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addEquipmenttoUser(user_id, equipment_id):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    userEquipmentInsertQuery = """INSERT into user_equipment (user_id, equipment_id) VALUES (%s, %s)"""
    check = checkifUserEquipmentAlreadyExists(user_id, equipment_id)
    if check == ():
        try:
            cursor.execute(userEquipmentInsertQuery, (user_id, equipment_id))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass

def checkifRecipeEquipmentAlreadyExists(recipe_id, equipment_id):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeEquipmentCheckQuery = "SELECT * FROM recipe_equipment WHERE recipe_id = %s and equipment_id = %s;"
    try:
        cursor.execute(recipeEquipmentCheckQuery, (recipe_id, equipment_id))  # to replace s% put in quotation marks
        result = cursor.fetchall()
        return result
    except Exception:
        return "Error: OOPs something went wrong!"

def addEquipmenttoRecipe(recipe_id, equipment_id):
    db = db_helpers.getDbCon()
    cursor = db.cursor()
    recipeEquipmentInsertQuery = """INSERT into recipe_equipment (recip_id, equipment_id) VALUES (%s, %s)"""
    check = checkifRecipeEquipmentAlreadyExists(recipe_id, equipment_id)
    if check == ():
        try:
            cursor.execute(recipeEquipmentInsertQuery, (recipe_id, equipment_id))  # to replace s% put in quotation markes
            db.commit()
        except Exception:
            return 'Error: unable to execute!'
        finally:
            cursor.close()
            db.close()
    else:
        pass

def getEquipmentId(equipment):
    db = helpers.getDbCon()
    cursor = db.cursor()
    equipmentIdQuery = "SELECT equipment_id FROM equipments WHERE username = %s"
    cursor.execute(userIdQuery, (equipment,))
    equipment_id = cursor.fetchone()
    return equipment_id