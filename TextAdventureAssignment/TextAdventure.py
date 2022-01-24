#Looking around lets them find a small sword that a goblin left behind and begin escaping.
#They face some goblins and a goblin boss in the cave as well as find some items.
#Goblin chief fight
#When they leave the cave they find a forest with a shrine at the end of it.
#The player inspecting the shrine causes them to find a magical amulet within the holy water in the shrine
#There is then a conversation/speech from the deity the shrine pertains to. The game ends with future adventures layed out for the player
#(Cliffhanger) "You prepare for future adventure!"

###################################################

import time
import TextAdventureDescriptionText as discText

playerDictionary = {"Inventory": [], "Health": 100}

playerAlive = True

restraintsEscaped = False
storageInputList = ["barrel", "barrels", "crate", "crates", "storage"]

def typeText(text):
    for ch in text:
        print(ch, end="")
        time.sleep(0.005)

def StartSequence():
    time.sleep(1)
    typeText("""
  ______   ______    __   __       __  .__   __.   _______      ______     ___   ____    ____  _______     _______.
 /      | /  __  \  |  | |  |     |  | |  \ |  |  /  _____|    /      |   /   \  \   \  /   / |   ____|   /       |
|  ,----'|  |  |  | |  | |  |     |  | |   \|  | |  |  __     |  ,----'  /  ^  \  \   \/   /  |  |__     |   (----`
|  |     |  |  |  | |  | |  |     |  | |  . `  | |  | |_ |    |  |      /  /_\  \  \      /   |   __|     \   \    
|  `----.|  `--'  | |  | |  `----.|  | |  |\   | |  |__| |    |  `----./  _____  \  \    /    |  |____.----)   |   
 \______| \______/  |__| |_______||__| |__| \__|  \______|     \______/__/     \__\  \__/     |_______|_______/    
                                                                                                                   """)
    time.sleep(3)
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

def RestraintEscape():
    time.sleep(2)
    typeText(discText.restraintEscapeText)
    restraintsEscaped = True
    UserInputRoomActions()

def StartRoomInspect():
    time.sleep(2)
    typeText(discText.startRoomLookText)
    if restraintsEscaped == True:
        UserInputRoomActions()
    else:
        UserInputStartingActions()

def StorageInspect():
    time.sleep(2)
    typeText(discText.storageInspectText)
    UserInputRoomActions()


def UserInputStartingActions():
    userInputStarting = input("\n\nWhat would you like to do? ")
    if "restraints" in userInputStarting.lower():
        RestraintEscape()
    elif "room" in userInputStarting.lower():
        StartRoomInspect()
    else:
        print("Invalid input")
        UserInputStartingActions()

def UserInputRoomActions():
    userInputRoom = input("\n\nWhat would you like to do? ")
    if "take" and "sword" in userInputRoom.lower():
        typeText("You acquire a Short Sword!")
        playerDictionary["Inventory"].append("Sword")
        print("Current inventory: ", playerDictionary["Inventory"])
    elif "leave" or "door" in userInputRoom.lower():
        CaveCorridor()
    else:
        print("Invalid input")
        UserInputRoomActions()

def CaveCorridor():

StartSequence()
