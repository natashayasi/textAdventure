import random
import sys

from Counter import Counter
from Location import Location
from Player import Player
from Trait import Trait
from Traversal import Traversal

# [x] Create room prototype
# [x] Create player prototype
# [ ] Make a debug menu class
# [ ] Make a story menu
# [ ] Figure out how to accesss story text
# [x] Create a Linked list/array for room traversal/history

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

# Initialize game values

traits = {}
traits.update({"isBrave":Trait("Brave", "isBrave")})
traits.update({"isFearless":Trait("Fearless", "isFearless")})
traits.update({"isImpulsive":Trait("Impulsive", "isImpulsive")})
traits.update({"isPrivateIntrospective":Trait("PrivateIntrospective", "isPrivateIntrospective")})
traits.update({"isInquisitive":Trait("Inquisitive", "isInquisitive")})
traits.update({"isPassionate":Trait("Passionate", "isPassionate")})
traits.update({"isCheerful":Trait("Cheerful", "isCheerful")})
traits.update({"isBold":Trait("Bold", "isBold")})
traits.update({"isCurious":Trait("Curious", "isCurious")})
traits.update({"isSentimental":Trait("Sentimental", "isSentimental")})
traits.update({"isDaring":Trait("Daring", "isDaring")})
traits.update({"isContientious":Trait("Contientious", "isContientious")})
traits.update({"isDutiful":Trait("Dutiful", "isDutiful")})
traits.update({"isSelfSufficient":Trait("SelfSufficient", "isSelfSufficient")})
traits.update({"isTrepadacious":Trait("Trepadacious", "isTrepadacious")})
traits.update({"isProud":Trait("Proud", "isProud")})

counters = {}
counters.update({"feralCounter":Counter("feralCounter")})
counters.update({"townCounter":Counter("townCounter")})
counters.update({"castleCounter":Counter("castleCounter")})
counters.update({"seekCounter":Counter("seekCounter")})
counters.update({"pastCounter":Counter("pastCounter")})

starts = {}
starts.update({"Start" : Location("Start","Starting Location","","","","","","","")})
starts.update({"FirstStart" : Location("FirstStart","First Start Location","","isBrave","isDaring","isImpulsive","","","")})
starts.update({"SecondStart" : Location("SecondStart","Second Start Location","","isTrepadacious","isContientious","isPrivate","","","")})
starts.update({"ThirdStart" : Location("ThirdStart","Third Start Location","","isDutiful","isContientious","isProud","","","")})
starts.update({"FourthStart" : Location("FourthStart","Fourth Start Location","","isSelfSufficient","","","","","")})
starts.update({"FifthStart" : Location("FifthStart","Fifth Start Location","","isPassionate","","","","","")})
starts.update({"SixthStart" : Location("SixthStart","Sixth Start Location","","isSentimental","","","","","")})

rooms = {}
rooms.update({"HuntersBedroom" : Location("HuntersBedroom","Hunter's Bedroom","Brave","Fearless","","","FeralCounter","","")})
rooms.update({"Cave" : Location("Cave","Cave","Brave","Contientious","","","FeralCounter","","")})
rooms.update({"CremeMarbleKingStyleBathroom" : Location("CremeMarbleKingStyleBathroom","Creme Marble King-Style Bathroom","Brave","Fearless","","","FeralCounter","","")})
rooms.update({"RecipeRoomKitchen" : Location("RecipeRoomKitchen","Recipe Room 1 - Kitchen","Self-Sufficient","Proud","","","CastleCounter","","")})
rooms.update({"KitchenProduction" : Location("KitchenProduction","Kitchen 2 - Production","Self-Sufficient","Trepadacious","","","SeekCounter","","")})
rooms.update({"VegetableGarden" : Location("VegetableGarden","Vegetable Garden","Self-Sufficient","Proud","","","CastleCounter","TownCounter","")})
rooms.update({"KitchenNook" : Location("KitchenNook","Kitchen 1 - Nook","Private","Daring","","","TownCounter","CastleCounter","")})
rooms.update({"UnderTheTreesBedroom" : Location("UnderTheTreesBedroom","Under the Trees Bedroom","Private","Inquisitive","","","SeekCounter","","")})
rooms.update({"FireplaceLounge" : Location("FireplaceLounge","Fireplace Lounge","Private","Dutiful","","","CastleCounter","","")})
rooms.update({"LibraryPoetry" : Location("LibraryPoetry","Library 1 - Poetry","Sentimental","Inquisitive","","","PastCounter","","")})
rooms.update({"RoyalStandingTubBathroom" : Location("RoyalStandingTubBathroom","Royal Standing Tub Bathroom","Sentimental","Passionate","","","CastleCounter","SeekCounter","")})
rooms.update({"MusicRoom" : Location("MusicRoom","Music Room","Sentimental","Cheerful","","","TownCounter","CastleCounter","")})
rooms.update({"UnderwaterBedroom" : Location("UnderwaterBedroom","Underwater Bedroom","Impulsive","Contientious","","","FeralCounter","SeekCounter","")})
rooms.update({"WineSpiritCellar" : Location("WineSpiritCellar","Wine/Spirit Cellar","Impulsive","Dutiful","","","TownCounter","","")})
rooms.update({"OutdoorHotSpringBathroom" : Location("OutdoorHotSpringBathroom","Outdoor Hot Springs Bathroom","Daring","Dutiful","","","FeralCounter","CastleCounter","")})
rooms.update({"ArmorRoom" : Location("ArmorRoom","Armor Room","Daring","Brave","","","CastleCounter","","")})
rooms.update({"ArcheryRange" : Location("ArcheryRange","Archery Range","Daring","Brave","","","FeralCounter","","")})
rooms.update({"LibraryFiction" : Location("LibraryFiction","Library 2 - Fiction","Passionate","Daring","","","TownCounter","","")})
rooms.update({"SunlightBedroom" : Location("SunlightBedroom","Sunlight Bedroom","Passionate","Cheerful","","","TownCounter","","")})
rooms.update({"ArtStudio" : Location("ArtStudio","Art Studio","Passionate","Private","Daring","","SeekCounter","PastCounter","")})
rooms.update({"ServantsUtilityShowerRoom" : Location("ServantsUtilityShowerRoom","Servants' Utility Shower Room","Contientious","Proud","","","CastleCounter","","")})
rooms.update({"StablesCoachHouse" : Location("StablesCoachHouse","Stables and Coach House","Contientious","Proud","","","TownCounter","","")})
rooms.update({"GiantGameFloorRoom" : Location("GiantGameFloorRoom","Giant Game Floor Room","Bold","Passionate","","","SeekCounter","CastleCounter","")})
rooms.update({"HedgeMaze" : Location("HedgeMaze","Hedge Maze","Bold","Fearless","","","FeralCounter","","")})
rooms.update({"BatsPotionsBedroom" : Location("BatsPotionsBedroom","Bats & Potions Bedroom","Bold","Trepadacious","","","SeekCounter","","")})
rooms.update({"LibraryNonFiction" : Location("LibraryNonFiction","Library 3 - Non-Fiction","Inquisitive","Curious","","","SeekCounter","","")})
rooms.update({"TownAdministratorBedroom" : Location("TownAdministratorBedroom","Town Administrator's Bedroom","Inquisitive","Bold","","","TownCounter","","")})
rooms.update({"ApiarySilkwormNest" : Location("ApiarySilkwormNest","Apiary / Silkworm Nest","Inquisitive","Brave","","","FeralCounter","","")})
rooms.update({"Terrarrium" : Location("Terrarrium","Terrarrium","Cheerful","Private","","","TownCounter","FeralCounter","")})
rooms.update({"Aquarium" : Location("Aquarium","Aquarium","Trepadacious","Impulsive","","","TownCounter","CastleCounter","")})
rooms.update({"GreenhouseUnderDivingPond" : Location("GreenhouseUnderDivingPond","Greenhouse Under the Diving Pond","Trepadacious","Bold","Daring","","SeekCounter","","")})
rooms.update({"JewelsBedroom" : Location("JewelsBedroom","Jewels Bedroom","Proud","Contientious","","","PastCounter","SeekCounter","")})
rooms.update({"GameYard" : Location("GameYard","Game Yard","Proud","Private","","","CastleCounter","","")})
rooms.update({"FruitOrchard" : Location("FruitOrchard","Fruit Orchard","Dutiful","Sentimental","","","TownCounter","CastleCounter","")})
rooms.update({"MilitaryGamesRoom" : Location("MilitaryGamesRoom","Military Games Room","Dutiful","Proud","Bold","","PastCounter","","")})
rooms.update({"SecretPassageBehindBookcase" : Location("SecretPassageBehindBookcase","Secret Passage Behind Bookcase","Curious","Sentimental","","","PastCounter","","")})
rooms.update({"Observatory" : Location("Observatory","Observatory","Curious","Sentimental","","","CastleCounter","PastCounter","")})
rooms.update({"HighWindowTower" : Location("HighWindowTower","High Window Tower with Diving Platform","Fearless","Inquisitive","","","PastCounter","","")})
rooms.update({"GallowsTinyStage" : Location("GallowsTinyStage","Gallows Renovated into a Tiny Stage","Fearless","Curious","","","CastleCounter","","")})


# object instance
player = Player("Lonk", traits.copy(), counters.copy(), Traversal(rooms.copy(),starts.copy()))


debugMainMenu()




#for room in roomList:
#    print('Name : {}, Text : {}'.format(room.name,room.text))


#player.travels.reportLocationList()

#player.setTraitTrue("isBrave")
#player.setTraitTrue("isDaring")
#player.reportTraitsTrue()
#player.setTraitFalse("isBrave")
#player.reportTraitsTrue()

#player.incrementCounter("feralCounter")
#player.incrementCounter("townCounter")
#player.incrementCounter("townCounter")
#player.reportCounters()
#player.decrementCounter("feralCounter")
#player.reportCounters()