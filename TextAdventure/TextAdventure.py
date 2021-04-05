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
            1. Change stats
            2. View stats
            3. Traverse Path 
            4. Exit
        """)
        response = input("Selct 1 through 4\n")
        if response == "1":
            debugMenuChangeStats()
        elif response == "2":
            debugMenuViewStats()
        elif response == "3":
            debugMenuTraverseLocation()
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
            print("What Trait do you want set to True?")
            _userInput = input()        
            player.setTraitTrue(_userInput)
        elif response == "2":
            print("What Trait do you want set to False?")
            _userInput = input()        
            player.setTraitFalse(_userInput)
        elif response == "3":
            print("What Counter do you want incremented?")
            _userInput = input()        
            player.incrementCounter(_userInput)
        elif response == "4":
            print("What Counter do you want decremented?")
            _userInput = input()        
            player.decrementCounter(_userInput)
        elif response == "5":
            break

def debugMenuViewStats():
    while True:
        print ("""
            1. View Traits, True
            2. View Traits, False
            3. View Counters
            4. View Locations
            5. View Starting Locations
            6. View Visited Locations
            7. View Accessible Locations
            8. View Inaccessible Locations
            9. Exit
        """)
        response = input("Selct 1 through 9\n")
        if response == "1":
            player.reportTraitsTrue()
        elif response == "2":
            player.reportTraitsFalse()
        elif response == "3":
            player.reportCounters()
        elif response == "4":        
            player.reportLocationDict()
        elif response == "5":
            player.reportStartingLocationsDict()
        elif response == "6":
            player.reportVisitedLocationsDict()
        elif response == "7":
            player.reportAccessibleLocationsDict()
        elif response == "8":
            player.reportInaccessibleLocationsDict()
        elif response == "9":
            break

def debugMenuTraverseLocation():
    while True:
        print ("""
            1. Start
            2. Report Current Location
            3. Go to a new Location
            4. Revist Location
            5. Reconcil Outside Stat Changes
            6. Exit
        """)
        response = input("Selct 1 through 5\n")
        if response == "1":
            debugMenuTraverseLocationStart()
        elif response == "2":
            player.reportCurrentLocation()
        elif response == "3":
            player.travelToRandomLocation()
        elif response == "4":        
            print("to Implement")
        elif response == "5":
            print("to Implement")
        elif response == "6":
            break

def debugMenuTraverseLocationStart():
    while True:
        print ("""
            1. First Start
            2. Second Start
            3. Third Start
            4. Fourth Start
            5. Fifth Start
            6. Sixth Start
            7. Exit
        """)
        response = input("Selct 1 through 7\n")
        if response == "1":
            player.travelToLocation("FirstStart")
        elif response == "2":
            player.travelToLocation("SecondStart")
        elif response == "3":
            player.travelToLocation("ThirdStart")
        elif response == "4":
            player.travelToLocation("FourthStart")
        elif response == "5":
            player.travelToLocation("FifthStart")
        elif response == "6":
            player.travelToLocation("SixthStart")
        break

# Initialize the game's values

player = Player()

player.traitDictionary.update({"isBold":Trait("Bold", "isBold",False)})
player.traitDictionary.update({"isBrave":Trait("Brave", "isBrave",False)})
player.traitDictionary.update({"isCompetent":Trait("Competent", "isCompetent",False)})
player.traitDictionary.update({"isContientious":Trait("Contientious", "isContientious",False)})
player.traitDictionary.update({"isCurious":Trait("Curious", "isCurious",False)})
player.traitDictionary.update({"isDaring":Trait("Daring", "isDaring",False)})
player.traitDictionary.update({"isDutiful":Trait("Dutiful", "isDutiful",False)})
player.traitDictionary.update({"isFearless":Trait("Fearless", "isFearless",False)})
player.traitDictionary.update({"isImpulsive":Trait("Impulsive", "isImpulsive",False)})
player.traitDictionary.update({"isInquisitive":Trait("Inquisitive", "isInquisitive",False)})
player.traitDictionary.update({"isPassionate":Trait("Passionate", "isPassionate",False)})
player.traitDictionary.update({"isPrivate":Trait("Private", "isPrivate",False)})
player.traitDictionary.update({"isProud":Trait("Proud", "isProud",False)})
player.traitDictionary.update({"isSentimental":Trait("Sentimental", "isSentimental",False)})
player.traitDictionary.update({"isTrepidatious":Trait("Trepidatious", "isTrepidatious",False)})
player.traitDictionary.update({"isStarted" : Trait("Start", "Start",True)})

player.counterDictionary.update({"castleCounter":Counter("castleCounter","Castle",0)})
player.counterDictionary.update({"feralCounter":Counter("feralCounter","Feral",0)})
player.counterDictionary.update({"pastCounter":Counter("pastCounter","Past",0)})
player.counterDictionary.update({"seekCounter":Counter("seekCounter","Seek",0)})
player.counterDictionary.update({"townCounter":Counter("townCounter","Town",0)})

player.travels.locationDictionary.update({"Hub" : Location("Hub","Central Location","")})
player.travels.locationDictionary.update({"Start" : Location("Start","Starting Location","")})
player.travels.locationDictionary.update({"BooksStart" : Location("BooksStart","Pack only books","")})
player.travels.locationDictionary.update({"CookwareStart" : Location("CookwareStart","Pack only cookware","")})
player.travels.locationDictionary.update({"KeepsakesStart" : Location("KeepsakesStart","Pack only keepsakes","")})
player.travels.locationDictionary.update({"NoPackingStart" : Location("NoPackingStart","Don't pack; just leave","")})
player.travels.locationDictionary.update({"PatienceStart" : Location("PatienceStart","Ask for patience","")})
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

player.travels.locationDictionary["BooksStart"].traitNameList.append(["Passionate","Inquisitive"])
player.travels.locationDictionary["CookwareStart"].traitNameList.append(["Contientious","Proud"])
player.travels.locationDictionary["KeepsakesStart"].traitNameList.append(["Private","Sentimental"])
player.travels.locationDictionary["NoPackingStart"].traitNameList.append(["Brave","Daring","Impulsive"])
player.travels.locationDictionary["PatienceStart"].traitNameList.append(["Trepidatious","Contientious","Dutiful"])
player.travels.locationDictionary["AdminBedroom"].traitNameList.append(["Bold"])
player.travels.locationDictionary["Apiary"].traitNameList.append(["Brave"])
player.travels.locationDictionary["AquacultureBuilding"].traitNameList.append(["Impulsive"])
player.travels.locationDictionary["ArcheryRange"].traitNameList.append(["Brave"])
player.travels.locationDictionary["Armory"].traitNameList.append(["Brave"])
player.travels.locationDictionary["ArtStudio"].traitNameList.append(["Private","Daring"])
player.travels.locationDictionary["Cave"].traitNameList.append(["Contientious"])
player.travels.locationDictionary["DivingPlatform"].traitNameList.append(["Impulsive"])
player.travels.locationDictionary["FictionLibrary"].traitNameList.append(["Daring"])
player.travels.locationDictionary["FireplaceLounge"].traitNameList.append(["Dutiful"])
player.travels.locationDictionary["GallowStage"].traitNameList.append(["Inquisitive","Passionate"])
player.travels.locationDictionary["GameRoom"].traitNameList.append(["Passionate"])
player.travels.locationDictionary["GameYard"].traitNameList.append(["Private"])
player.travels.locationDictionary["Garden"].traitNameList.append(["Proud"])
player.travels.locationDictionary["HedgeMaze"].traitNameList.append(["Fearless"])
player.travels.locationDictionary["HotSpring"].traitNameList.append(["Fearless"])
player.travels.locationDictionary["HuntersBedroom"].traitNameList.append(["Fearless"])
player.travels.locationDictionary["JewelsBedroom"].traitNameList.append(["Contientious"])
player.travels.locationDictionary["MilitaryGamesRoom"].traitNameList.append(["Bold","Competent"])
player.travels.locationDictionary["MusicRoom"].traitNameList.append(["Curious"])
player.travels.locationDictionary["NonFictionLibrary"].traitNameList.append(["Curious"])
player.travels.locationDictionary["NookKitchen"].traitNameList.append(["Competent","Daring"])
player.travels.locationDictionary["Observatory"].traitNameList.append(["Sentimental"])
player.travels.locationDictionary["Orchard"].traitNameList.append(["Sentimental"])
player.travels.locationDictionary["PoetryLibrary"].traitNameList.append(["Inquisitive"])
player.travels.locationDictionary["ProductionKitchen"].traitNameList.append(["Trepidatious"])
player.travels.locationDictionary["RecipeRoom"].traitNameList.append(["Proud"])
player.travels.locationDictionary["SecretPassage"].traitNameList.append(["Sentimental"])
player.travels.locationDictionary["SpookyBedroom"].traitNameList.append(["Trepidatious"])
player.travels.locationDictionary["Stables"].traitNameList.append(["Proud"])
player.travels.locationDictionary["TreeBedroom"].traitNameList.append(["Inquisitive"])
player.travels.locationDictionary["UnderwaterBedroom"].traitNameList.append(["Bold"])
player.travels.locationDictionary["WineCellar"].traitNameList.append(["Dutiful"])

player.travels.locationDictionary["Stables"].interactablesList.append([Interactable("caparison","Caparison","Town")])
player.travels.locationDictionary["ArcheryRange"].traitNameList.append([Interactable("bowAndArrows","Bow and arrows","Feral")])
player.travels.locationDictionary["UnderwaterBedroom"].traitNameList.append([Interactable("fishSkeletons","Fish skeletons","Feral"), Interactable("stainedCoral","Stained coral","Seek")])
player.travels.locationDictionary["MilitaryGamesRoom"].traitNameList.append([Interactable("familyTree","Military family tree","Past")])
player.travels.locationDictionary["DivingPlatform"].traitNameList.append([Interactable("portrait","Portrait","Past")])
player.travels.locationDictionary["Cave"].traitNameList.append([Interactable("bat","Bat","Feral"), Interactable("townInsignia","Town insignia","Town")])
player.travels.locationDictionary["Orchard"].traitNameList.append([Interactable("appleCart","Apple cart","Town"), Interactable("berryBasket","Berry basket","Castle")])
player.travels.locationDictionary["Apiary"].traitNameList.append([Interactable("silkwormCocoons","Silkworm cocoons","Feral")])
player.travels.locationDictionary["SecretPassage"].traitNameList.append([Interactable("chestOfRobes","Chest of robes","Past")])
player.travels.locationDictionary["WineCellar"].traitNameList.append([Interactable("yourEmptyHome","Your empty home","Town")])
player.travels.locationDictionary["NookKitchen"].traitNameList.append([Interactable("spices","Spices","Town"), Interactable("exoticMeat","Exotic meat","Castle")])
player.travels.locationDictionary["AdminBedroom"].traitNameList.append([Interactable("townLedger","Town ledger","Town")])
player.travels.locationDictionary["ArtStudio"].traitNameList.append([Interactable("paints","Paints","Seek"), Interactable("lockedChest","Locked chest","Past")])
player.travels.locationDictionary["Garden"].traitNameList.append([Interactable("labelStakes","Label stakes","Castle"), Interactable("bushel","Bushel","Town")])
player.travels.locationDictionary["GameYard"].traitNameList.append([Interactable("bucketOfWater","Bucket of water","Castle")])
player.travels.locationDictionary["NonFictionLibrary"].traitNameList.append([Interactable("mapTome ","Giant tome of world maps","Seek")])
player.travels.locationDictionary["JewelsBedroom"].traitNameList.append([Interactable("serpentRuby","The Serpent Ruby","Past"), Interactable("bagOfPearls","Bag of pearls","Town")])
player.travels.locationDictionary["MusicRoom"].traitNameList.append([Interactable("boxOfSheetMusic","Box of sheet music","Town"), Interactable("conductorsScore","Conductor's score","Seek")])
player.travels.locationDictionary["ProductionKitchen"].traitNameList.append([Interactable("emptyPlates","Empty plates","Seek")])
player.travels.locationDictionary["SpookyBedroom"].traitNameList.append([Interactable("occultTome","Occult tome","Seek"), Interactable("handwrittenScroll","Scroll with handwritten notes","Past")])
player.travels.locationDictionary["FictionLibrary"].traitNameList.append([Interactable("contactInfo","Contact information of a publisher","Seek")])
player.travels.locationDictionary["RecipeRoom"].traitNameList.append([Interactable("recipeBox","Castle recipe box","Seek")])
player.travels.locationDictionary["HedgeMaze"].traitNameList.append([Interactable("yourClothes","Your own clothing (removed)","Feral")])
player.travels.locationDictionary["PoetryLibrary"].traitNameList.append([Interactable("wornVolume","Most worn volume","Past")])
player.travels.locationDictionary["GallowStage"].traitNameList.append([Interactable("trapdoor","Trapdoor","Castle")])
player.travels.locationDictionary["GameRoom"].traitNameList.append([Interactable("embroideredQuilt","Embroidered quilt","Castle")])
player.travels.locationDictionary["Armory"].traitNameList.append([Interactable("suitOfArmor","Suit of armor","Feral")])
player.travels.locationDictionary["FireplaceLounge"].traitNameList.append([Interactable("servingBell","Serving bell","Castle"), Interactable("architecturalPlans","Architectural plans","Seek")])
player.travels.locationDictionary["AquacultureBuilding"].traitNameList.append([Interactable("preservedFishEggs","Preserved fish eggs","Town"), Interactable("basketOfFish","Basket of adult fish","Castle")])
player.travels.locationDictionary["Observatory"].traitNameList.append([Interactable("birthCharts","Birth charts","Castle"), Interactable("starMap","Star map with handwriting","Past")])
player.travels.locationDictionary["TreeBedroom"].traitNameList.append([Interactable("moss","Patch of moss","Seek")])
player.travels.locationDictionary["HuntersBedroom"].traitNameList.append([Interactable("rrophy","Stuffed trophy","Feral")])
player.travels.locationDictionary["HotSpring"].traitNameList.append([Interactable("giantAnimals","Gigantic animals","Feral"), Interactable("lockets","Princes' lockets","Castle")])

debugMainMenu()

#for room in roomList:
#    print('Name : {}, Text : {}').format(room.name,room.text)