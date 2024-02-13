import readData, addData, deleteData, validation

readData.read()

print("\nWhat would you like to do?\n3. Look at Potions\n")
pathChoice = validation.validateInt()


def potionLook():
    print("\nWhat rarity of potion would you like to see?\n1. All\n2. Common\n")
    potionRarity = validation.validateInt()
    print("\nWhat type of potion would you like to see?\n1. All\n2. Potion\n3. Poison\n4. Oil\n5. Philter\n6. Elixir\n7. Miscellaneous\n")
    potionType = validation.validateInt()
    readData.readPotions(potionRarity, potionType)

def ingredientLook():
    print("\nWhat rarity of ingredients would you like to see?\n1. All\n2. Common\n")
    ingredientRarity = validation.validateInt()
    print("\nWhat role of ingredients would you like to see?\n1. All\n2. Tincture\n3. Solution\n4. Powders\n")
    ingredientRole = validation.validateInt()
    match ingredientRole:
        case 1:
            ingredientType = 1
        case 2:
            print("\nWould you like to see Mushrooms or Roots?\n1. Mushrooms\n2. Roots\n3. Both\n")
            ingredientTypeChoice = validation.validateInt
            match ingredientTypeChoice:
                case 1:
                    ingredientType = 2
                case 2:
                    ingredientType = 3
                case 3:
                    ingredientType = 4
        case 3:
            print("\nWould you like to see Plants or Herbs?\n1. Plants\n2. Herbs\n3. Both\n")
            ingredientTypeChoice = validation.validateInt
            match ingredientTypeChoice:
                case 1:
                    ingredientType = 5
                case 2:
                    ingredientType = 6
                case 3:
                    ingredientType = 7
        case 4:
            print("\nWould you like to see Mushrooms or Roots?\n1. Bark\n2. Miscellaneous\n3. Both\n")
            ingredientTypeChoice = validation.validateInt
            match ingredientTypeChoice:
                case 1:
                    ingredientType = 8
                case 2:
                    ingredientType = 9
                case 3:
                    ingredientType = 10
    readData.readIngredients(ingredientRarity, ingredientRole, ingredientType)


if pathChoice == 3:
    potionLook()