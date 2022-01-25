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

PlayerInventory = {}

playerAlive = True

def typeText(text):
    for ch in text:
        print(ch, end="")
        time.sleep(0.1)

def StartSequence():
    time.sleep(1)
    typeText("Welcome to this Text Adventure Game")
    time.sleep(3)
    typeText("\n\nLocation: ???")
    time.sleep(2)
    typeText("\n\nYou wake up, dazed and confused with hands and feet tied.\n"
          "As you start to wake up you hear the grunts of goblins around you and stiffen into alertness.")
    time.sleep(3)
    typeText("\n\nGoblin 1:")
    typeText("\nWell look who finally woke up. Dinner!")
    time.sleep(3)
    typeText("\n\nGoblin 2:")
    typeText("\nKnock em' out good you did, what are we thinking... Human Soup? Barbeque?")
    time.sleep(3)
    typeText("\n\nGoblin Boss")
    typeText("\nShut it you two, that's for the chief to decide")
    time.sleep(3)
    typeText("\n\nGoblin Boss")
    typeText("\nCome on, lets go tell the chief that our new friend here is awake")
    time.sleep(3)
    typeText("\n\nThe three goblins leave the damp dingy cave you are captive in and slam the door shut.")
    UserInput()

def RestraintEscape():
    time.sleep(2)
    typeText(discText.restraintEscapeText)
    UserInput()

def StartRoomInspect():
    time.sleep(2)
    typeText(discText.startRoomLookText)
    UserInput()

def BarrelInspect():
    time.sleep(2)
    typeText(discText.barrelInspectText)
    UserInput()

def CrateInspect():
    time.sleep(2)
    typeText(discText.crateInspectText)
    UserInput()

def UserInput():
    userInput = input("What would you like to do?")
    if "escape" in userInput.lower():
        RestraintEscape()
    elif "look" in userInput.lower():
        StartRoomInspect()
    elif "barrel" or "barrels" in userInput.lower():
        BarrelInspect()
    elif "crate" or "crates" in userInput.lower():
        CrateInspect()
    elif "take" and "sword" in userInput.lower():
        typeText("You acquire a Short Sword!")
        playerInventory["Short Sword"] = {Damage: 3, Magic: 0}
    else:
        print("Invalid input")

while playerAlive != False:
    StartSequence()