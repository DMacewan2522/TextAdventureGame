#They face some goblins and a goblin boss in the cave as well as find some items.
#Goblin chief fight
#When they leave the cave they find a forest with a shrine at the end of it.
#The player inspecting the shrine causes them to find a magical amulet within the holy water in the shrine
#There is then a conversation/speech from the deity the shrine pertains to. The game ends with future adventures layed out for the player
#(Cliffhanger) "You prepare for future adventure!"

###################################################

#Module Imports
import time
import random
import TextAdventureDescriptionText as discText

#Player stats dictionary
playerDictionary = {"Inventory": [], "Health": 100}

#Global Variables
restraintsEscaped = False

#Function that allows text to be printed onto the screen character by character (Essentially replaces print)
def typeText(text):
    for ch in text:
        print(ch, end="")
        time.sleep(0.005)

#Called upon when a players health is reduced to 0
def PlayerDeath():
    typeText(discText.playerDeathText)
    restartGame = input("\nDo you wish to start the game again? (Y/N) ")
    if restartGame.lower() == "y":
        StartSequence()
    elif restartGame.lower == "n":
        exit()
    else:
        PlayerDeath()

#Intro sequence
def StartSequence():
    time.sleep(1)
    #Game Title
    typeText("""
  ______   ______    __   __       __  .__   __.   _______      ______     ___   ____    ____  _______     _______.
 /      | /  __  \  |  | |  |     |  | |  \ |  |  /  _____|    /      |   /   \  \   \  /   / |   ____|   /       |
|  ,----'|  |  |  | |  | |  |     |  | |   \|  | |  |  __     |  ,----'  /  ^  \  \   \/   /  |  |__     |   (----`
|  |     |  |  |  | |  | |  |     |  | |  . `  | |  | |_ |    |  |      /  /_\  \  \      /   |   __|     \   \    
|  `----.|  `--'  | |  | |  `----.|  | |  |\   | |  |__| |    |  `----./  _____  \  \    /    |  |____.----)   |   
 \______| \______/  |__| |_______||__| |__| \__|  \______|     \______/__/     \__\  \__/     |_______|_______/    
                                                                                                                   """)
    time.sleep(3)
    #Dialogue to introduce the character to their enemies
    typeText("\n\nLocation: ???")
    time.sleep(2)
    typeText("\n\nYou wake up, dazed and confused with hands and feet tied.\n"
             "As you start to wake up you hear the grunts of goblins around you and stiffen into alertness.")
    time.sleep(3)
    typeText("\n\nGoblin 1:")
    typeText("\nWell look who finally woke up... Dinner!")
    time.sleep(3)
    typeText("\n\nGoblin 2:")
    typeText("\nKnock em' out good you did, what are we thinking... Human Soup? Barbeque?")
    time.sleep(3)
    typeText("\n\nGoblin Boss:")
    typeText("\nShut it you two, that's for the chief to decide")
    time.sleep(3)
    typeText("\n\nGoblin Boss:")
    typeText("\nCome on, lets go tell the chief that our new friend here is awake")
    time.sleep(3)
    typeText("\n\nThe three goblins leave the damp dingy cave you are captive in and slam the door shut.")
    UserInputStartingActions()

#Called upon when the player inputs to escape their restraints
def RestraintEscape():
    time.sleep(2)
    # Calls upon another .py file that stores large descriptive text. This is used throughout the code
    typeText(discText.restraintEscapeText)
    restraintsEscaped = True
    UserInputRoomActions()

#Called upon when the player inputs to look around the room they wake up in
def StartRoomInspect():
    time.sleep(2)
    typeText(discText.startRoomLookText)
    #If statement to ensure the player doesn't become restrained again if they have already performed that action
    if restraintsEscaped == True:
        UserInputRoomActions()
    else:
        UserInputStartingActions()

#The input options that the player has when they are restrained in the first room
def UserInputStartingActions():
    userInputStarting = input("\n\nWhat would you like to do? ")
    if "restraints" in userInputStarting.lower():
        RestraintEscape()
    elif "room" in userInputStarting.lower():
        StartRoomInspect()
    else:
        print("Invalid input")
        UserInputStartingActions()

#The input options that the player has when they have escaped their restraints
def UserInputRoomActions():
    userInputRoom = input("\n\nWhat would you like to do? ")
    if "take" and "sword" in userInputRoom.lower():
        typeText("You acquire a Short Sword!")
        playerDictionary["Inventory"].append("Sword")
        print("Current inventory: ", playerDictionary["Inventory"])
        UserInputRoomActions()
    elif "leave" or "door" in userInputRoom.lower():
        CaveCorridor()
    else:
        print("Invalid input")
        UserInputRoomActions()

#First goblin combat sequence.
def RandGoblinOneCombatSequence():
    #Player can only block and attack if the sword is in their inventory
    if "Sword" in playerDictionary.get("Inventory"):
        blockGoblinOne = input("\nThe goblin swings it's blade at you! Do you try to block? (Y/N) ")
        if blockGoblinOne.lower() == "y":
            typeText("\nYou pull your sword up just in time and the goblins attack is thwarted!")
            #Blocking gives the player an opportunity to attack the goblin back
            attackGoblinOne = input("Do you swing back at the goblin? (Y/N) ")
            if attackGoblinOne.lower() == "y":
                typeText("\nYou take a fatal swing at the goblin and it falls to the ground!")
                userInputPostGoblinOne = input("\nWhat would you like to do? ")
                exit()
            else:
                RandGoblinOneCombatSequence()
        #If the player does not block, they take damage
        else:
            typeText("\nYou are hit by the goblin's blade and take 15 damage!")
            playerDictionary["Health"] -= 15
            print("Your current health is: ", playerDictionary.get("Health"))
            if playerDictionary["Health"] <= 0:
                PlayerDeath()
            else:
                RandGoblinOneCombatSequence()
    #If the sword is not in their inventory, they cannot block and are repeatedly attacked with bonus damage
    else:
        # The player is told that they do not have defences, implying that they needed to pick up the sword which they will likely pick up when they play again
        typeText("\nYou are hit by the goblin's blade and, with no defences, take 50 damage!")
        playerDictionary["Health"] -= 50
        print("Your current health is: ", playerDictionary.get("Health"))
        if playerDictionary["Health"] <= 0:
            PlayerDeath()
        else:
            RandGoblinOneCombatSequence()


#Called upon when the player chooses to leave the starting room
def CaveCorridor():
    #Random enemy generator. Essentially flips a coin to see if an enemy is present or not
    enemyCaveCorridorPresent = 1
    time.sleep(2)
    typeText(discText.caveCorridorDescription)
    time.sleep(2)
    #Begins combat sequence with the enemy if they are present
    if enemyCaveCorridorPresent == 1:
        typeText("\nWithout having time to think, a goblin comes walking towards you "
                 "from the direction you need to go... He draws his sword and charges!")
        RandGoblinOneCombatSequence()
    #Asks the player what they wish to do if there is no enemy present
    else:
        userInputCaveCorridor = input("\nWhat would you like to do? ")
        exit()

#Begins the game
StartSequence()
