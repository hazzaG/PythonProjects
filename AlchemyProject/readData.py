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



def readIngredients(ingredientRarity, ingredientRole, ingredientType):
    match ingredientRarity:
        case
    
    match ingredientRole:
        case
    
    match ingredientType:
        case