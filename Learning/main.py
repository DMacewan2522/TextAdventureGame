import time

playerDictionary = {"Inventory":[], "Health":3, "EXP":0}

def playerNamePrint(playerName):
    time.sleep(2)
    if playerName == "Rainbow Unicorn":
        print("Prank em' John")
    elif playerName == "Declan":
        print("Bruh")
    elif playerName == "Ben":
        print("Bozo")
    time.sleep(2)

def playerDeath(wayOfDeath):
    if wayOfDeath == 1:
        print("Cthulu Ate you")
    else:
        print("You died bozo")

def threeDoors():
    doorInput = int(input("You come to a crossing with 3 doors. Which will you choose? 1, 2, or 3"))
    if doorInput == 1:
        treasureChest()
    elif doorInput == 2:
        meetCthulu()
    elif doorInput == 3:
        playerDeath(1)

def treasureChest():
    print("You find a treasure chest. Opening it reveals riches and jewels!")

def meetCthulu():
    print("You go through the door only to be met with Cthulu!!!")
    cthuluInput = int(input("Quick, What do you do? \n\n 1. Flee \n\n 2. Fight for your life"))
    if cthuluInput == 1:
        treasureChest()
    elif cthuluInput == 2:
        playerDeath()

def caveSequence():
    print("You head into the opening of the cave.\nIt's rather dark in here...")
    time.sleep(3)
    torchInput = input("You manage to spot a torch hung on the wall. Light the torch? ")
    if torchInput.lower() == "yes":
        print("You light the torch and a beast emerges from the dark into your torchlight\n\n")
        time.sleep(2)
        print("The beast swipes at you but you manage to dodge\n")
        time.sleep(2)
        fightInput = input("What do you do in retaliation? ")
        if "draw sword" in fightInput.lower() and "Sword" in playerDictionary.get("Inventory"):
            print("You attack the beast with your blade.\nIt stumbles backwards with a screech and appears injured\n\n")
            dodgeInput = input("A swipe from the angered beast comes your way. What do you do in response? ")
            if "dodge" in dodgeInput.lower():
                print("You avoid the swipe, taking no damage\n\n")
                secondAttack = input("You get another chance to attack. What will you use? ")
                if "sword" in secondAttack.lower() and "Sword" in playerDictionary.get("Inventory"):
                    print("The beast falls in combat and you make your way to the end of the cave")
            else:
                playerDictionary["Health"] -= 1
                print("You are hit by the beast, losing health")
                print("Your health = ", playerDictionary.get("Health"))
                secondAttack = input("You get another chance to attack. What will you use? ")
                if "sword" in secondAttack.lower() and "Sword" in playerDictionary.get("Inventory"):
                    print("The beast falls in combat and you make your way to the end of the cave")
        else:
            print("Something swipes at you from the darkness, delivering a fatal blow\n")
            time.sleep(2)
            playerDeath()
    else:
        print("Something swipes at you from the darkness, delivering a fatal blow\n")
        time.sleep(2)
        playerDeath()

playerNamePrint(playerName = input("Please tell me your name: "))

print("Welcome to this text based adventure test\n")
time.sleep(3)
print("You wake up in a forest, surrounded by trees.\n There is a pathway in front of you leading to an opening...\n\n")
firstChoice = input("What do you do? ")

firstChoice.lower()
if "go forward" or "go to the opening" or "go down the path" in firstChoice.lower():
    time.sleep(6)
    print("\n\nYou reach the opening and find a sword stuck in a large rock.\n Behind the rock is a dark cave.\n\n")
    secondInput = input("What would you like to do? ")
    if "get sword" in secondInput.lower():
        print("You yank the sword from the stone.\n")
        playerDictionary["Inventory"].append("Sword")
        time.sleep(2)
        print("Sword has been added to your inventory")
        print("After aquring the sword, you enter the cave\n\n")
        caveSequence()
    elif "go into cave" in secondInput.lower():
        caveSequence()