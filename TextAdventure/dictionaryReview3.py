playerInventory = {}
playerStats = {"Health":100, "Magic":0, "Courage":10}


def itemSelectOne():
    choiceOne = int(input("\n\nSelect an item to add to your inventory:\n\n 1. Magical staff \n 2. Lion's Heart \n\n What do you choose:"))
    if choiceOne == 1:
        playerInventory["Item1"] = "Magical staff"
        playerStats["Magic"] += 10
        itemSelectTwo()
    elif choiceOne == 2:
        playerInventory["Item1"] = "Lion's Heart"
        playerStats["Courage"] += 25
        itemSelectTwo()

def itemSelectTwo():
    choiceTwo = int(input("\n\nSelect an item to add to your inventory:\n\n 1. Potion of Greater Health \n 2. Courageous Emblem \n\n What do you choose:"))
    if choiceTwo == 1:
        playerInventory["Item2"] = "Potion of Greater Health"
        itemSelectThree()
    elif choiceTwo == 2:
        playerInventory["Item2"] = "Courageous Emblem"
        playerStats["Courage"] += 15
        itemSelectThree()

def itemSelectThree():
    choiceThree = int(input("\n\nSelect an item to add to your inventory:\n\n 1. Root of Health \n 2. Sigil of Greater Magic \n\n What do you choose:"))
    if choiceThree == 1:
        playerInventory["Item3"] = "Root of Health"
        playerStats["Health"] += 20
    elif choiceThree == 2:
        playerInventory["Item3"] = "Sigil of Greater Magic"
        playerStats["Magic"] += 20


itemSelectOne()

print("\n\n")
print(playerInventory)
print(playerStats)

if playerInventory["Item2"] == "Potion of Greater Health":
    usePotion = input("\n\nWould you like to use your Potion of Greater Health? : ")
    if usePotion.lower == "yes" or "y":
        playerStats["Health"] += 50

print(playerInventory)
print(playerStats)