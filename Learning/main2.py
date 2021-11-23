playerStats = dict(FlyAbility = 0, Stealth = 0)
playerItems = dict(Daggers = 0, BluePotions = 0, GoldenFeathers = 0, Manuscripts = 0)

while True:
    try:
        playerChoice = int(input("\nWhich item would you like to select: \n\n 1. Daggers\n 2. Blue Potions\n 3. Golden Feathers\n 4. Manuscripts\n\n Which do you choose: "))
        if playerChoice == 1:
            playerItems["Daggers"] += 1
            print("\n", playerStats)
            print("\n", playerItems)
        elif playerChoice == 2 and playerStats["Stealth"] < 5:
            playerStats["Stealth"] += 1
            playerItems["BluePotions"] += 1
            print("\n", playerStats)
            print("\n", playerItems)
        elif playerChoice == 3 and playerStats["FlyAbility"] < 5:
            playerStats["FlyAbility"] += 1
            playerItems["GoldenFeathers"] += 1
            print("\n", playerStats)
            print("\n", playerItems)
        elif playerChoice == 4:
            playerItems["Manuscripts"] += 1
            print("\n", playerStats)
            print("\n", playerItems)
        elif playerStats["FlyAbility"] == 5 or playerStats["Stealth"] == 5 or playerChoice != (1,2,3,4):
            print("\n\nTry a different item\n")
    except ValueError:
        print("\n\nExpecting a number\n")