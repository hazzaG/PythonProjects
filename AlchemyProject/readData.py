from alchemyConnect import *

# create subroutine
def read():
    try:
        dbCursor.execute("SELECT * FROM potions")
        # # dbCursor.execute("CREATE DATABASE TEST")

        rows = dbCursor.fetchall()
        # OR 
        # rows = dbCursor.execute("SELECT * FROM potions").fetchall()

        if not rows:
            print("No record exists")
        else:
            for aRecord in rows:
                print(aRecord)
    except sql.errors.Error as e:
        print(f"{e}")
if __name__ == "__main__":
    read()

def readPotions(potionRarity, potionType):
    match potionRarity:
        case 1:
            potionRarity = "%"
        case 2:
            potionRarity = "Common"
        case 3:
            potionRarity = "Uncommon"
        case 4:
            potionRarity = "Rare"
        case 5:
            potionRarity = "Very rare"

    match potionType:
        case 1:
            potionType = "%"
        case 2:
            potionType = "Potion"
        case 3:
            potionType = "Poison"
        case 4:
            potionType = "Oil"
        case 5:
            potionType = "Philter"
        case 6:
            potionType = "Elixir"
        case 7:
            potionType = "Miscellaneous"

    try:
        dbCursor.execute(f"SELECT * FROM potions WHERE Rarity LIKE '{potionRarity}' AND Type LIKE '{potionType}'")

        rows = dbCursor.fetchall()
        # OR 
        # rows = dbCursor.execute("SELECT * FROM potions").fetchall()

        if not rows:
            print("No record exists")
        else:
            for aRecord in rows:
                print(aRecord)
    except sql.errors.Error as e:
        print(f"{e}")
if __name__ == "__main__":
    readPotions()



def readIngredients(ingredientRarity, ingredientRole, ingredientTypeChoice):
    ingredientType = ingredientRole * (ingredientTypeChoice * ingredientRole)
    print(ingredientType)

    match ingredientRarity:
        case 1:
            ingredientRarity = "%"
        case 2:
            ingredientRarity = "Common"
        case 3:
            ingredientRarity = "Uncommon"
        case 4:
            ingredientRarity = "Rare"
        case 5:
            ingredientRarity = "Very rare"
    
    match ingredientRole:
        case 1:
            ingredientRole = "%"
        case 2:
            ingredientRole = "Tincture"
        case 3:
            ingredientRole = "Solution"
        case 4:
            ingredientRole = "Powders"
    
    match ingredientType:
        case 1:
            ingredientType = "%"
        case 4:
            ingredientType = "Mushrooms"
        case 8:
            ingredientType = "Roots"
        case 12:
            ingredientType = "%"
        case 9:
            ingredientType = "Plants"
        case 18:
            ingredientType = "Herbs"
        case 27:
            ingredientType = "%"
        case 16:
            ingredientType = "Barks"
        case 32:
            ingredientType = "Miscellaneous"
        case 48:
            ingredientType = "%"
    try:
        dbCursor.execute(f"SELECT * FROM ingredients WHERE Rarity LIKE '{ingredientRarity}' AND IngRole LIKE '{ingredientRole}' AND IngType LIKE '{ingredientType}'")

        rows = dbCursor.fetchall()
        # OR 
        # rows = dbCursor.execute("SELECT * FROM potions").fetchall()

        if not rows:
            print("No record exists")
        else:
            for aRecord in rows:
                print(aRecord)
    except sql.errors.Error as e:
        print(f"{e}")
if __name__ == "__main__":
    readIngredients()


def readIngredientsID(ingredientId):
    try:
        dbCursor.execute(f"SELECT Name,Rarity,IngType,Amount FROM ingredients WHERE ID = {ingredientId}")
        # # dbCursor.execute("CREATE DATABASE TEST")

        rows = dbCursor.fetchall()
        # OR 
        # rows = dbCursor.execute("SELECT * FROM potions").fetchall()

        if not rows:
            return "No record exists"
        else:
            for aRecord in rows:
                print(aRecord)
    except sql.errors.Error as e:
        print(f"{e}")
if __name__ == "__main__":
    readIngredientsID()