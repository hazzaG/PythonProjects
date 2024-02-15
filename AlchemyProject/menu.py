import readData, addData, updateData, validation

print("\nWhat would you like to do?\n2. Add ingredients\n3. Look at Potions\n4. Look at Ingredients\n")
pathChoice = validation.inputExpectation(1, 4)
"""
"""

def addIngredientByID(ingredientId):
    notConfimed = True
    while notConfimed:
        print("\nWould you like to add to this ingredient?\n1. Yes\n2. No")
        ingredientAddConfirm = validation.inputExpectation(1, 2)
        if ingredientAddConfirm == 1:
            print("\nHow much would you like to add?")
            updateAmount = validation.inputExpectation(1, 100)
            updateData.ingredientUpdate(ingredientId,updateAmount)
            notConfimed = False
        if ingredientAddConfirm == 2:
            print("\nOperation cancelled\n")
            notConfimed = False

def ingredientReadID():
    notConfimed = True
    while notConfimed:
        print("\nPlease input ingredient ID")
        ingredientId = validation.inputExpectation(100000, 600000)
        ingredientSearched = readData.readIngredientsID(ingredientId)
        if ingredientSearched != "No record exists":
            notConfimed = False
            addIngredientByID(ingredientId)
        if ingredientSearched == "No record exists":
            print("\nInvalid ID, please try again")


def potionLook():
    print("\nWhat rarity of potion would you like to see?\n1. All\n2. Common\n3. Uncommon\n4. Rare\n5. Very rare\n")
    potionRarity = validation.inputExpectation(1, 5)
    print("\nWhat type of potion would you like to see?\n1. All\n2. Potion\n3. Poison\n4. Oil\n5. Philter\n6. Elixir\n7. Miscellaneous\n")
    potionType = validation.inputExpectation(1, 7)
    readData.readPotions(potionRarity, potionType)

def ingredientLook():
    print("\nWhat rarity of ingredients would you like to see?\n1. All\n2. Common\n3. Uncommon\n4. Rare\n5. Very rare\n")
    ingredientRarity = validation.inputExpectation(1, 5)
    print("\nWhat role of ingredients would you like to see?\n1. All\n2. Tincture\n3. Solution\n4. Powders\n")
    ingredientRole = validation.inputExpectation(1, 4)
    match ingredientRole:
        case 1:
            ingredientTypeChoice = 1
        case 2:
            print("\nWould you like to see Mushrooms or Roots?\n1. Mushrooms\n2. Roots\n3. Both\n")
        case 3:
            print("\nWould you like to see Plants or Herbs?\n1. Plants\n2. Herbs\n3. Both\n")
        case 4:
            print("\nWould you like to see Mushrooms or Roots?\n1. Bark\n2. Miscellaneous\n3. Both\n")
    if ingredientRole != 1:
        ingredientTypeChoice = validation.inputExpectation(2, 4)
    print(ingredientRarity, ingredientRole, ingredientTypeChoice)
    readData.readIngredients(ingredientRarity, ingredientRole, ingredientTypeChoice)

if pathChoice == 2:
    ingredientReadID()
if pathChoice == 3:
    potionLook()
if pathChoice == 4:
    ingredientLook()