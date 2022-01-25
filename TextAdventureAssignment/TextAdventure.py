#They face some goblins and a goblin boss in the cave as well as find some items.
#Goblin chief fight
#(Cliffhanger) "You prepare for future adventure!"

#Name: Declan Macewan       Student Number: 2005884

#Module Imports
import time
import random
import TextAdventureDescriptionText as descText

#Player stats dictionary
playerDictionary = {"Inventory": [], "Health": 100}

#Global Variables
restraintsEscaped = False
goblinChiefHealth = 150

#Function that allows text to be printed onto the screen character by character (Essentially replaces print)
def typeText(text):
    for ch in text:
        print(ch, end="")
        time.sleep(0.01)

#Called upon when a players health is reduced to 0
def PlayerDeath():
    typeText(descText.playerDeathText)
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
    typeText("\n\nYou wake up, dazed and confused with hands and feet loosely tied.\n"
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
    typeText(descText.restraintEscapeText)
    restraintsEscaped = True
    UserInputRoomActions()

#Called upon when the player inputs to look around the room they wake up in
def StartRoomInspect():
    time.sleep(2)
    typeText(descText.startRoomLookText)
    #If statement to ensure the player doesn't become restrained again if they have already performed that action
    if restraintsEscaped == True:
        UserInputRoomActions()
    else:
        UserInputStartingActions()

#The input options that the player has when they are restrained in the first room
def UserInputStartingActions():
    userInputStarting = input("\n\nWhat would you like to do? (Try to escape restraints? / Look around the room for more information?) ")
    if "restraints" in userInputStarting.lower():
        RestraintEscape()
    elif "room" in userInputStarting.lower():
        StartRoomInspect()
    else:
        print("\nInvalid input")
        UserInputStartingActions()

#The input options that the player has when they have escaped their restraints
def UserInputRoomActions():
    userInputRoom = input("\n\nWhat would you like to do? (Take the sword? / Leave the room?) ")
    if "take" and "sword" in userInputRoom.lower():
        typeText("\nYou acquire a Short Sword!")
        playerDictionary["Inventory"].append("Sword")
        print("\nCurrent inventory: ", playerDictionary["Inventory"])
        UserInputRoomActions()
    elif "leave" or "room" in userInputRoom.lower():
        CaveCorridor()
    else:
        typeText("\nInvalid input")
        UserInputRoomActions()

#First goblin combat sequence.
def RandGoblinOneCombatSequence():
    #Player can only block and attack if the sword is in their inventory
    if "Sword" in playerDictionary.get("Inventory"):
        blockGoblinOne = input("\nThe goblin swings it's blade at you! Do you try to block? (Y/N) ")
        if "y" or "yes" in blockGoblinOne.lower():
            typeText("\nYou pull your sword up just in time and the goblins attack is thwarted!")
            #Blocking gives the player an opportunity to attack the goblin back
            attackGoblinOne = input("\nDo you swing back at the goblin? (Y/N) ")
            if "y" or "yes" in attackGoblinOne.lower():
                typeText("\nYou take a fatal swing at the goblin and it falls to the ground!")
                userInputPostGoblinOne = input("\n\nWhat would you like to do? ")
                if "walk" or "forward" or "go" in userInputPostGoblinOne.lower():
                    CaveHallway()
                else:
                    typeText("Invalid Input")
                    CaveCorridorChoice()
            else:
                RandGoblinOneCombatSequence()
        #If the player does not block, they take damage
        else:
            typeText("\nYou are hit by the goblin's blade and take 15 damage!")
            playerDictionary["Health"] -= 15
            print("\nYour current health is: ", playerDictionary.get("Health"))
            if playerDictionary["Health"] <= 0:
                PlayerDeath()
            else:
                RandGoblinOneCombatSequence()
    #If the sword is not in their inventory, they cannot block and are repeatedly attacked with bonus damage
    else:
        # The player is told that they do not have defences, implying that they needed to pick up the sword which they will likely pick up when they play again
        typeText("\nYou are hit by the goblin's blade and, with no defences, take 50 damage!")
        playerDictionary["Health"] -= 50
        print("\nYour current health is: ", playerDictionary.get("Health"))
        if playerDictionary["Health"] <= 0:
            PlayerDeath()
        else:
            RandGoblinOneCombatSequence()

#Called upon when the player chooses to leave the starting room
def CaveCorridor():
    #Random enemy generator. Essentially flips a coin to see if an enemy is present or not
    enemyCaveCorridorPresent = random.randint(1,2)
    time.sleep(2)
    typeText(descText.caveCorridorDescription)
    time.sleep(2)
    #Begins combat sequence with the enemy if they are present
    if enemyCaveCorridorPresent == 1:
        typeText("\nWithout having time to think, a goblin comes walking towards you "
                 "from the direction you need to go... He draws his sword and charges!")
        RandGoblinOneCombatSequence()
    #Asks the player what they wish to do if there is no enemy present
    else:
        CaveCorridorChoice()

#Called upon to give the player input options in the cave corridor sequences
def CaveCorridorChoice():
    userInputCaveCorridor = input("\n\nWhat would you like to do? ")
    if "walk" or "forward" or "go" in userInputCaveCorridor.lower():
        CaveHallway()
    else:
        typeText("\nInvalid Input")
        CaveCorridorChoice()

#Called upon after cave corridor section is complete and the player chooses to
def CaveHallway():
    time.sleep(2)
    typeText(descText.caveHallwayDescription)
    time.sleep(2)
    CaveSplitChoice()

#Player input on which path they wish to choose - Changes which item they acquire second
def CaveSplitChoice():
    caveSplitChoice = input("\n\nWhich path do you choose? Left or Right? ")
    if "l" or "left" in caveSplitChoice.lower():
        CaveSplitLeft()
    elif "r" or "right" in caveSplitChoice.lower():
        CaveSplitRight()
    else:
        typeText("\nInvalid Input")
        CaveSplitChoice()

#Called upon if the player chooses the left path, also gives the player a new item
def CaveSplitLeft():
    time.sleep(2)
    typeText(descText.caveSplitLeftDescriptionOne)
    breakWall = input("\nDo you want to break the wall to see the source of the glow? (Y/N) ")
    if "y" or "yes" in breakWall.lower():
        time.sleep(2)
        typeText(descText.caveSplitLeftDescriptionTwo)
        pickUpItem = input("\nDo you wish to take this with you? (Y/N)")
        if "y" or "yes" in pickUpItem.lower():
            time.sleep(1)
            typeText("\nYou acquire a magical rapier!")
            playerDictionary["Inventory"].append("Magical Rapier")
            GoblinBossRoom()
        elif "n" or "no" in pickUpItem.lower():
            GoblinBossRoom()
    elif "n" or "no" in breakWall.lower():
        GoblinBossRoom()

#Called upon if the player chooses the right path, also gives the player a new item
def CaveSplitRight():
    time.sleep(2)
    typeText(descText.caveSplitRightDescriptionOne)
    breakWall = input("\nDo you want to break the wall to see the source of the glow? (Y/N) ")
    if "y" or "yes" in breakWall.lower():
        time.sleep(2)
        typeText(descText.caveSplitRightDescriptionTwo)
        pickUpItem = input("\nDo you wish to take this with you? (Y/N)")
        if "y" or "yes" in pickUpItem.lower():
            time.sleep(1)
            typeText("\nYou acquire a Potion of Dragons Blood!")
            playerDictionary["Inventory"].append("Potion of Dragon Blood")
            GoblinBossRoom()
        elif "n" or "no" in pickUpItem.lower():
            GoblinBossRoom()
    elif "n" or "no" in breakWall.lower():
        GoblinBossRoom()

#Description and dialogue before boss fight
def GoblinBossRoom():
    time.sleep(2)
    typeText(descText.goblinBossRoomDescription)
    time.sleep(2)
    typeText("\nGoblin Chief:")
    typeText("\nWell well well... if it isn't our dinner rummaging around the place")
    time.sleep(2)
    typeText("\nGoblin Chief:")
    typeText("\nYou don't really think you're getting out of here alive right???")
    time.sleep(2)
    typeText("\nGoblin Chief:")
    typeText("\nI'll make it easy for the both of us and kill you myself eh?")
    time.sleep(2)
    typeText("\n\nThe goblin chief draws his large club and comes charging to you!")
    time.sleep(2)
    GoblinBossCombat()

#Boss fight combat sequence
def GoblinBossCombat(goblinChiefHealth):
    if "Magical Rapier" in playerDictionary.get("Inventory"):
        attackChief = input("\nThe Chief runs at you but is slow, you get the chance to attack! Will you take it? (Y/N)")
        if "y" or "yes" in attackChief.lower():
            typeText("\nYou swing at the Goblin Chief and deal a large amount of damage with your magical rapier!")
            goblinChiefHealth -= 40
            if goblinChiefHealth <= 0:
                GoblinBossVictory()
            else:
                GoblinBossCombat()
        elif "n" or "no" in attackChief.lower():
            typeText("\nThe chief smashes you with his club, sending you staggering backwards")
            playerDictionary["Health"] -= 30
            print("\nYour current health is: ", playerDictionary.get("Health"))
            if playerDictionary["Health"] <= 0:
                PlayerDeath()
            else:
                GoblinBossCombat()
    elif "Potion of Dragons Blood" in playerDictionary.get("Inventory"):
        attackChief = input("\nThe Chief runs at you but is slow, you get the chance to attack! Will you take it? (Y/N)")
        if "y" or "yes" in attackChief.lower():
            typeText("\nYou swing at the Goblin Chief and deal him a decent blow!")
            goblinChiefHealth -= 20
            if goblinChiefHealth <= 0:
                GoblinBossVictory()
            else:
                GoblinBossCombat()
        elif "n" or "no" in attackChief.lower():
            typeText("\nThe chief smashes you with his club, sending you staggering backwards")
            typeText("\nYour Potion of Dragons Blood protects you and you take less damage than normal")
            playerDictionary["Health"] -= 20
            print("\nYour current health is: ", playerDictionary.get("Health"))
            if playerDictionary["Health"] <= 0:
                PlayerDeath()
            else:
                GoblinBossCombat()
    else:
        typeText("\nWith no defences, the Goblin Chief batters you with his club and you are send flying\n"
                 "Into the cave wall behind you, leaving you with no life left")
        PlayerDeath()

def GoblinBossVictory():

#Begins the game
StartSequence()
