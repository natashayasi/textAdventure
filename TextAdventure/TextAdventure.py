# [ ] Make a debug menu class
# [ ] Make a story menu class
# [ ] Accesss story text

import random
import sys

from Counter import Counter
from Interactable import Interactable
from Location import Location
from Player import Player
from Trait import Trait
from Traversal import Traversal

def debugMainMenu():
    while True:
        print ("""
            1. Play Game
            2. Edit Variables
            3. View Variables
            4. Exit
        """)
        response = input("Selct 1 through 4\n")
        if response == "1":
            debugPlayMenu()
        elif response == "2":
            debugMenuChangeStats()
        elif response == "3":
            debugMenuViewStats()
        elif response == "4":
            break

def debugMenuChangeStats():
    while True:
        print ("""
            1. Change Trait True
            2. Change Trait False
            3. Increment Counter
            4. Decrement Counter
            5. Exit
        """)
        response = input("Selct 1 through 5\n")
        if response == "1":
            print("What Trait do you want set to True?\n")
            _userInput = input()        
            player.setTraitTrue(_userInput)
        elif response == "2":
            print("What Trait do you want set to False?\n")
            _userInput = input()        
            player.setTraitFalse(_userInput)
        elif response == "3":
            print("What Counter do you want incremented?\n")
            _userInput = input()        
            player.incrementCounter(_userInput)
        elif response == "4":
            print("What Counter do you want decremented?\n")
            _userInput = input()        
            player.decrementCounter(_userInput)
        elif response == "5":
            break

def debugMenuViewStats():
    while True:
        print ("""
            1. View Traits, All
            2. View Traits, True
            3. View Traits, False
            4. View Counters
            5. View Locations
            6. View Interactables, All
            7. View Interactables, By Location
            8. View Starting Locations
            9. View Visited Locations
            10. View Accessible Locations
            11. View Inaccessible Locations
            12. Exit
        """)
        response = input("Selct 1 through 12\n")
        if response == "1":
            player.reportTraits()
        elif response == "2":
            player.reportTraitsTrue()
        elif response == "3":
            player.reportTraitsFalse()
        elif response == "4":
            player.reportCounters()
        elif response == "5":
            player.reportLocations()
        elif response == "6":
            player.reportInteractables()
        elif response == "7":
            _interactablesResponse = input("Chose a location\n")
            player.reportInteractablesByLocation()
        elif response == "8":
            print("toImplement")#todo
        elif response == "9":
            player.reportVisitedLocations()
        elif response == "10":
            player.reportAccessibleLocations()
        elif response == "11":
            player.reportInaccessibleLocations()
        elif response == "12":
            break

def debugPlayMenu():
    while True:
        print ("""
            1. Start
            2. Report Current Location
            3. Go to a Location, Random
            4. Go to a Location, by Trait
            5. Revist Location
            6. Reconcil Outside Stat Changes
            7. Exit
        """)
        response = input("Selct 1 through 7.\n")
        if response == "1":
            debugPlayMenuStart()
        elif response == "2":
            player.reportCurrentLocation()
        elif response == "3":
            player.travelRandomly()
        elif response == "4":
            _traitResponse = input("Select a trait.\n")
            player.travelRandomlyByTrait(_traitResponse)
        elif response == "5":
            player.reportVisitedLocations()
            _locationResponse = input("Select a location from the list\n")
            player.travelToLocation(_locationResponse)
        elif response == "6":
            player.refreshTraversal()
        elif response == "7":
            break

def debugPlayMenuStart():
    while True:
        print ("""
            1. Books Start
            2. Cookware Start
            3. Keepsakes Start
            4. No Packing Start
            5. Patience Start
            6. Exit
        """)
        response = input("Selct 1 through 7\n")
        if response == "1":
            player.travelToLocation("BooksStart")
        elif response == "2":
            player.travelToLocation("CookwareStart")
        elif response == "3":
            player.travelToLocation("KeepsakesStart")
        elif response == "4":
            player.travelToLocation("NoPackingStart")
        elif response == "5":
            player.travelToLocation("PatienceStart")
        break

# Initialize the game's values

player = Player()
player.travels.setupTraversal()

player.traitDictionary.update({"Bold":Trait("Bold", "Bold",False)})
player.traitDictionary.update({"Brave":Trait("Brave", "Brave",False)})
player.traitDictionary.update({"Competent":Trait("Competent", "Competent",False)})
player.traitDictionary.update({"Contientious":Trait("Contientious", "Contientious",False)})
player.traitDictionary.update({"Curious":Trait("Curious", "Curious",False)})
player.traitDictionary.update({"Daring":Trait("Daring", "Daring",False)})
player.traitDictionary.update({"Dutiful":Trait("Dutiful", "Dutiful",False)})
player.traitDictionary.update({"Fearless":Trait("Fearless", "Fearless",False)})
player.traitDictionary.update({"Impulsive":Trait("Impulsive", "Impulsive",False)})
player.traitDictionary.update({"Inquisitive":Trait("Inquisitive", "Inquisitive",False)})
player.traitDictionary.update({"Passionate":Trait("Passionate", "Passionate",False)})
player.traitDictionary.update({"Private":Trait("Private", "Private",False)})
player.traitDictionary.update({"Proud":Trait("Proud", "Proud",False)})
player.traitDictionary.update({"Sentimental":Trait("Sentimental", "Sentimental",False)})
player.traitDictionary.update({"Trepidatious":Trait("Trepidatious", "Trepidatious",False)})
player.traitDictionary.update({"Start" : Trait("Start", "Start",True)})
player.traitDictionary.update({"Hub" : Trait("Hub", "Hub",True)})

player.counterDictionary.update({"castleCounter":Counter("castleCounter","Castle",0)})
player.counterDictionary.update({"feralCounter":Counter("feralCounter","Feral",0)})
player.counterDictionary.update({"pastCounter":Counter("pastCounter","Past",0)})
player.counterDictionary.update({"seekCounter":Counter("seekCounter","Seek",0)})
player.counterDictionary.update({"townCounter":Counter("townCounter","Town",0)})

player.travels.locationDictionary.update({"Hub" : Location("Hub","Central Location","Hub")})
player.travels.locationDictionary.update({"Start" : Location("Start","Starting Location","Start")})
player.travels.locationDictionary.update({"BooksStart" : Location("BooksStart","Pack only books","Start")})
player.travels.locationDictionary.update({"CookwareStart" : Location("CookwareStart","Pack only cookware","Start")})
player.travels.locationDictionary.update({"KeepsakesStart" : Location("KeepsakesStart","Pack only keepsakes","Start")})
player.travels.locationDictionary.update({"NoPackingStart" : Location("NoPackingStart","Don't pack; just leave","Start")})
player.travels.locationDictionary.update({"PatienceStart" : Location("PatienceStart","Ask for patience","Start")})
player.travels.locationDictionary.update({"AdminBedroom" : Location("AdminBedroom","Town Administrator Bedroom","Inquisitive")})
player.travels.locationDictionary.update({"Apiary" : Location("Apiary","Apiary and Sericulture Hut","Inquisitive")})
player.travels.locationDictionary.update({"AquacultureBuilding" : Location("AquacultureBuilding","Fish Supply House and Hatchery","Trepidatious")})
player.travels.locationDictionary.update({"ArcheryRange" : Location("ArcheryRange","Archery Range","Daring")})
player.travels.locationDictionary.update({"Armory" : Location("Armory","Armor Room","Daring")})
player.travels.locationDictionary.update({"ArtStudio" : Location("ArtStudio","Art Studio","Passionate")})
player.travels.locationDictionary.update({"Cave" : Location("Cave","Cave","Brave")})
player.travels.locationDictionary.update({"DivingPlatform" : Location("DivingPlatform","High Tower with Diving Platform","Fearless")})
player.travels.locationDictionary.update({"FictionLibrary" : Location("FictionLibrary","Fiction Library","Passionate")})
player.travels.locationDictionary.update({"FireplaceLounge" : Location("FireplaceLounge","Fireplace Lounge","Private")})
player.travels.locationDictionary.update({"GallowStage" : Location("GallowStage","Gallows Renovated into a Tiny Stage","Fearless")})
player.travels.locationDictionary.update({"GameRoom" : Location("GameRoom","Casual Games Room","Bold")})
player.travels.locationDictionary.update({"GameYard" : Location("GameYard","Games Yard","Proud")})
player.travels.locationDictionary.update({"Garden" : Location("Garden","Vegetable Garden","Competent")})
player.travels.locationDictionary.update({"HedgeMaze" : Location("HedgeMaze","Hedge Maze","Bold")})
player.travels.locationDictionary.update({"HotSpring" : Location("HotSpring","Hot Spring","Daring")})
player.travels.locationDictionary.update({"HuntersBedroom" : Location("HuntersBedroom","Hunting Bedroom","Brave")})
player.travels.locationDictionary.update({"JewelsBedroom" : Location("JewelsBedroom","Jewels Bedroom","Proud")})
player.travels.locationDictionary.update({"MilitaryGamesRoom" : Location("MilitaryGamesRoom","Military Games Room","Dutiful")})
player.travels.locationDictionary.update({"MusicRoom" : Location("MusicRoom","Music Room","Sentimental")})
player.travels.locationDictionary.update({"NonFictionLibrary" : Location("NonFictionLibrary","NF Library","Inquisitive")})
player.travels.locationDictionary.update({"NookKitchen" : Location("NookKitchen","Nook Kitchen","Private")})
player.travels.locationDictionary.update({"Observatory" : Location("Observatory","Observatory","Curious")})
player.travels.locationDictionary.update({"Orchard" : Location("Orchard","Fruit Orchard","Dutiful")})
player.travels.locationDictionary.update({"PoetryLibrary" : Location("PoetryLibrary","Poetry Library","Sentimental")})
player.travels.locationDictionary.update({"ProductionKitchen" : Location("ProductionKitchen","Production Kitchen","Competent")})
player.travels.locationDictionary.update({"RecipeRoom" : Location("RecipeRoom","Kitchen Recipe Room","Competent")})
player.travels.locationDictionary.update({"SecretPassage" : Location("SecretPassage","Secret Passage behind Bookcase","Curious")})
player.travels.locationDictionary.update({"SpookyBedroom" : Location("SpookyBedroom","Bats and Potions Bedroom","Bold")})
player.travels.locationDictionary.update({"Stables" : Location("Stables","Stables and Coach House","Contientious")})
player.travels.locationDictionary.update({"TreeBedroom" : Location("TreeBedroom","Under the Trees Bedroom","Private")})
player.travels.locationDictionary.update({"UnderwaterBedroom" : Location("UnderwaterBedroom","Underwater Bedroom","Impulsive")})
player.travels.locationDictionary.update({"WineCellar" : Location("WineCellar","Wine and Spirits Cellar","Impulsive")})

player.travels.locationDictionary["BooksStart"].traitNameList.extend(["Passionate","Inquisitive"])
player.travels.locationDictionary["CookwareStart"].traitNameList.extend(["Contientious","Proud"])
player.travels.locationDictionary["KeepsakesStart"].traitNameList.extend(["Private","Sentimental"])
player.travels.locationDictionary["NoPackingStart"].traitNameList.extend(["Brave","Daring","Impulsive"])
player.travels.locationDictionary["PatienceStart"].traitNameList.extend(["Trepidatious","Contientious","Dutiful"])
player.travels.locationDictionary["AdminBedroom"].traitNameList.extend(["Bold"])
player.travels.locationDictionary["Apiary"].traitNameList.extend(["Brave"])
player.travels.locationDictionary["AquacultureBuilding"].traitNameList.extend(["Impulsive"])
player.travels.locationDictionary["ArcheryRange"].traitNameList.extend(["Brave"])
player.travels.locationDictionary["Armory"].traitNameList.extend(["Brave"])
player.travels.locationDictionary["ArtStudio"].traitNameList.extend(["Private","Daring"])
player.travels.locationDictionary["Cave"].traitNameList.extend(["Contientious"])
player.travels.locationDictionary["DivingPlatform"].traitNameList.extend(["Impulsive"])
player.travels.locationDictionary["FictionLibrary"].traitNameList.extend(["Daring"])
player.travels.locationDictionary["FireplaceLounge"].traitNameList.extend(["Dutiful"])
player.travels.locationDictionary["GallowStage"].traitNameList.extend(["Inquisitive","Passionate"])
player.travels.locationDictionary["GameRoom"].traitNameList.extend(["Passionate"])
player.travels.locationDictionary["GameYard"].traitNameList.extend(["Private"])
player.travels.locationDictionary["Garden"].traitNameList.extend(["Proud"])
player.travels.locationDictionary["HedgeMaze"].traitNameList.extend(["Fearless"])
player.travels.locationDictionary["HotSpring"].traitNameList.extend(["Fearless"])
player.travels.locationDictionary["HuntersBedroom"].traitNameList.extend(["Fearless"])
player.travels.locationDictionary["JewelsBedroom"].traitNameList.extend(["Contientious"])
player.travels.locationDictionary["MilitaryGamesRoom"].traitNameList.extend(["Bold","Competent"])
player.travels.locationDictionary["MusicRoom"].traitNameList.extend(["Curious"])
player.travels.locationDictionary["NonFictionLibrary"].traitNameList.extend(["Curious"])
player.travels.locationDictionary["NookKitchen"].traitNameList.extend(["Competent","Daring"])
player.travels.locationDictionary["Observatory"].traitNameList.extend(["Sentimental"])
player.travels.locationDictionary["Orchard"].traitNameList.extend(["Sentimental"])
player.travels.locationDictionary["PoetryLibrary"].traitNameList.extend(["Inquisitive"])
player.travels.locationDictionary["ProductionKitchen"].traitNameList.extend(["Trepidatious"])
player.travels.locationDictionary["RecipeRoom"].traitNameList.extend(["Proud"])
player.travels.locationDictionary["SecretPassage"].traitNameList.extend(["Sentimental"])
player.travels.locationDictionary["SpookyBedroom"].traitNameList.extend(["Trepidatious"])
player.travels.locationDictionary["Stables"].traitNameList.extend(["Proud"])
player.travels.locationDictionary["TreeBedroom"].traitNameList.extend(["Inquisitive"])
player.travels.locationDictionary["UnderwaterBedroom"].traitNameList.extend(["Bold"])
player.travels.locationDictionary["WineCellar"].traitNameList.extend(["Dutiful"])

player.travels.locationDictionary["Stables"].interactablesList.extend([Interactable("caparison","Caparison","Town")])
player.travels.locationDictionary["ArcheryRange"].traitNameList.extend([Interactable("bowAndArrows","Bow and arrows","Feral")])
player.travels.locationDictionary["UnderwaterBedroom"].traitNameList.extend([Interactable("fishSkeletons","Fish skeletons","Feral"), Interactable("stainedCoral","Stained coral","Seek")])
player.travels.locationDictionary["MilitaryGamesRoom"].traitNameList.extend([Interactable("familyTree","Military family tree","Past")])
player.travels.locationDictionary["DivingPlatform"].traitNameList.extend([Interactable("portrait","Portrait","Past")])
player.travels.locationDictionary["Cave"].traitNameList.extend([Interactable("bat","Bat","Feral"), Interactable("townInsignia","Town insignia","Town")])
player.travels.locationDictionary["Orchard"].traitNameList.extend([Interactable("appleCart","Apple cart","Town"), Interactable("berryBasket","Berry basket","Castle")])
player.travels.locationDictionary["Apiary"].traitNameList.extend([Interactable("silkwormCocoons","Silkworm cocoons","Feral")])
player.travels.locationDictionary["SecretPassage"].traitNameList.extend([Interactable("chestOfRobes","Chest of robes","Past")])
player.travels.locationDictionary["WineCellar"].traitNameList.extend([Interactable("yourEmptyHome","Your empty home","Town")])
player.travels.locationDictionary["NookKitchen"].traitNameList.extend([Interactable("spices","Spices","Town"), Interactable("exoticMeat","Exotic meat","Castle")])
player.travels.locationDictionary["AdminBedroom"].traitNameList.extend([Interactable("townLedger","Town ledger","Town")])
player.travels.locationDictionary["ArtStudio"].traitNameList.extend([Interactable("paints","Paints","Seek"), Interactable("lockedChest","Locked chest","Past")])
player.travels.locationDictionary["Garden"].traitNameList.extend([Interactable("labelStakes","Label stakes","Castle"), Interactable("bushel","Bushel","Town")])
player.travels.locationDictionary["GameYard"].traitNameList.extend([Interactable("bucketOfWater","Bucket of water","Castle")])
player.travels.locationDictionary["NonFictionLibrary"].traitNameList.extend([Interactable("mapTome ","Giant tome of world maps","Seek")])
player.travels.locationDictionary["JewelsBedroom"].traitNameList.extend([Interactable("serpentRuby","The Serpent Ruby","Past"), Interactable("bagOfPearls","Bag of pearls","Town")])
player.travels.locationDictionary["MusicRoom"].traitNameList.extend([Interactable("boxOfSheetMusic","Box of sheet music","Town"), Interactable("conductorsScore","Conductor's score","Seek")])
player.travels.locationDictionary["ProductionKitchen"].traitNameList.extend([Interactable("emptyPlates","Empty plates","Seek")])
player.travels.locationDictionary["SpookyBedroom"].traitNameList.extend([Interactable("occultTome","Occult tome","Seek"), Interactable("handwrittenScroll","Scroll with handwritten notes","Past")])
player.travels.locationDictionary["FictionLibrary"].traitNameList.extend([Interactable("contactInfo","Contact information of a publisher","Seek")])
player.travels.locationDictionary["RecipeRoom"].traitNameList.extend([Interactable("recipeBox","Castle recipe box","Seek")])
player.travels.locationDictionary["HedgeMaze"].traitNameList.extend([Interactable("yourClothes","Your own clothing (removed)","Feral")])
player.travels.locationDictionary["PoetryLibrary"].traitNameList.extend([Interactable("wornVolume","Most worn volume","Past")])
player.travels.locationDictionary["GallowStage"].traitNameList.extend([Interactable("trapdoor","Trapdoor","Castle")])
player.travels.locationDictionary["GameRoom"].traitNameList.extend([Interactable("embroideredQuilt","Embroidered quilt","Castle")])
player.travels.locationDictionary["Armory"].traitNameList.extend([Interactable("suitOfArmor","Suit of armor","Feral")])
player.travels.locationDictionary["FireplaceLounge"].traitNameList.extend([Interactable("servingBell","Serving bell","Castle"), Interactable("architecturalPlans","Architectural plans","Seek")])
player.travels.locationDictionary["AquacultureBuilding"].traitNameList.extend([Interactable("preservedFishEggs","Preserved fish eggs","Town"), Interactable("basketOfFish","Basket of adult fish","Castle")])
player.travels.locationDictionary["Observatory"].traitNameList.extend([Interactable("birthCharts","Birth charts","Castle"), Interactable("starMap","Star map with handwriting","Past")])
player.travels.locationDictionary["TreeBedroom"].traitNameList.extend([Interactable("moss","Patch of moss","Seek")])
player.travels.locationDictionary["HuntersBedroom"].traitNameList.extend([Interactable("rrophy","Stuffed trophy","Feral")])
player.travels.locationDictionary["HotSpring"].traitNameList.extend([Interactable("giantAnimals","Gigantic animals","Feral"), Interactable("lockets","Princes' lockets","Castle")])

debugMainMenu()

#for room in roomList:
#    print('Name : {}, Text : {}').format(room.name,room.text)