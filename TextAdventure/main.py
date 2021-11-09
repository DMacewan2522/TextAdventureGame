import time

playerDictionary = {"Inventory":[], "Health":3, "EXP":0}


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
            print("You lose")
    else:
        print("Something swipes at you from the darkness, delivering a fatal blow\n")
        time.sleep(2)
        print("You lose")

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