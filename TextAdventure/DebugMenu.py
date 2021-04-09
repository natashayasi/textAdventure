from Counter import Counter
from Interactable import Interactable
from Location import Location
from Player import Player
from Trait import Trait
from Traversal import Traversal

class DebugMenu:
    def __init__(self, player):
        self.player = player
        self.debugMainMenu()

    def debugMainMenu(self):
        while True:
            print("""
Main Menu
    1. Play Game
    2. Settings
    0. Exit
            """)
            response = input("What would you like to do? ")
            if response == "1":
                self.debugGameMenu()
            elif response == "2":
                self.debugSettingsMenu()
            elif response == "0":
                break

    def debugPlayMenuStart(self):
        self.player.readTextFromFile("Start")
        self.player.readTextFromFile("IntroductoryChapter")
        while True:
            print ("""
Start Menu
    1. Books Start
    2. Cookware Start
    3. Keepsakes Start
    4. No Packing Start
    5. Patience Start
            """)
            response = input("Selct 1 through 5\n")
            if response == "1":
                self.player.travelToLocation("BooksStart")
            elif response == "2":
                self.player.travelToLocation("CookwareStart")
            elif response == "3":
                self.player.travelToLocation("KeepsakesStart")
            elif response == "4":
                self.player.travelToLocation("NoPackingStart")
            elif response == "5":
                self.player.travelToLocation("PatienceStart")
            break


    def debugGameMenu(self):
        while True:
            print("""
Game Menu
    1. Start
    2. View Current Location
    3. Travel By Trait
    4. Travel By Random
    5. Travel By Name
    6. Go Back
    7. Go Forwards
    8. Touch something
    0. Exit
            """)
            response = input("What would you like to do? ")
            if response == "1":
                self.debugPlayMenuStart()
            elif response == "2":
                self.player.reportCurrentLocation()
            elif response == "3":
                _input = input("Select a trait to guide your travels.\n")
                self.player.travelRandomlyByTrait(_input)
            elif response == "4":
                self.player.travelRandomly()
            elif response == "5":
                self.player.reportAccessibleLocations()
                _input = input("Select an accessible location.\n")
                self.player.travelToLocation(_input)
            elif response == "6":
                print("To Implement")
            elif response == "7":
                print("To Implement")
            elif response == "8":
                _input = input("What do you try to touch? ")
                self.player.interactWithInteractable(_input)
            elif response == "0":
                break

    def debugSettingsMenu(self):
        while True:
            print("""
Settings Menu
    1. Traits
    2. Counters
    3. Locations
    4. Interactables
    5. Endings
    6. Reset Game
    0. Exit
            """)
            response = input("What would you like to do? ")
            if response == "1":
                self.debugTraitsMenu()
            elif response == "2":
                self.debugCountersMenu()
            elif response == "3":
                self.debugLocationsMenu()
            elif response == "4":
                self.debugInteractablesMenu()
            elif response == "5":
                self.player.checkCountersForEndCondition()
            elif response == "6":
                print("To Be Implemented")
            elif response == "0":
                break

    def debugTraitsMenu(self):
        while True:
            print("""
Traits Menu
    1. View Traits, All
    2. View Traits, True
    3. View Traits, False
    4. Set Trait True
    5. Set Trait False
    0. Exit
            """)
            response = input("What would you like to do? ")
            if response == "1":
                self.player.reportTraits()
            elif response == "2":
                self.player.reportTraitsTrue()
            elif response == "3":
                self.player.reportTraitsFalse()
            elif response == "4":
                _input = input("What Trait do you want set to True?\n")        
                self.player.setTraitTrue(_input)
            elif response == "5":
                _input = input("What Trait do you want set to False?\n")        
                self.player.setTraitFalse(_input)
            elif response == "0":
                break

    def debugCountersMenu(self):
        while True:
            print("""
Counters Menu
    1. View Counters
    2. Increment Counter
    3. Decrement Counter
    0. Exit
            """)
            response = input("What would you like to do? ")
            if response == "1":
                self.player.reportCounters()
            elif response == "2":
                _input = input("What Counter do you want incremented?\n")        
                self.player.incrementCounter(_input)
            elif response == "3":
                _input = input("What Counter do you want decremented?\n")        
                player.decrementCounter(_input)
            elif response == "0":
                break

    def debugLocationsMenu(self):
        while True:
            print("""
Locations Menu
    1. View Current Location
    2. View Locations
    3. View Visited Locations
    4. View Accessible Locations
    5. View Inaccessible Locations
    0. Exit
            """)
            response = input("What would you like to do? ")
            if response == "1":
                self.player.reportCurrentLocation()
            elif response == "2":
                self.player.reportLocations()
            elif response == "3":
                self.player.reportVisitedLocations()
            elif response == "4":
                self.player.reportAccessibleLocations()
            elif response == "5":
                self.player.reportInaccessibleLocations()
            elif response == "0":
                break

    def debugInteractablesMenu(self):
        while True:
            print("""
Interactables Menu
    1. View Interactables
    2. View Interactables by Location
    0. Exit 
            """)
            response = input("What would you like to do? ")
            if response == "1":
                 self.player.reportInteractables()
            elif response == "2":
                _interactablesResponse = input("Chose a location\n")
                self.player.reportInteractablesByLocation(_interactablesResponse)
            elif response == "0":
                break

def debugEndingMenu(self):
    while True:
        print("""
Ending Menu
    1. View Endings Reached
    0. Exit       
        """)
        response = input("What would you like to do? ")
        if response == "1":
            self.player.checkCountersForEndCondition()
        elif response == "0":
            break
