from Counter import Counter
from Interactable import Interactable
from Location import Location
from Trait import Trait
from Traversal import Traversal

class Player:
    def __init__(self):
        self.name = "Player"
        self.traitDictionary = {}
        self.counterDictionary = {}
        self.travels = Traversal()

    def setTraitTrue(self, traitName):
        if traitName in self.traitDictionary:
            self.traitDictionary[traitName].setTraitTrue()     

    def setTraitFalse(self, traitName):
        if traitName in self.traitDictionary:
            self.traitDictionary[traitName].setTraitFalse()

    def incrementCounter(self, counterName):
        if counterName in self.counterDictionary:
            self.counterDictionary[counterName].increment()

    def decrementCounter(self, counterName):
        if counterName in self.counterDictionary:
            self.counterDictionary[counterName].decrement()

    def listTraitNamesTrue(self):
        _traitNameList = []
        for trait in self.traitDictionary.values():
            if trait.value == True:
                _traitNameList.append(trait.name)
        return _traitNameList

    def refreshTraversal(self):
        _traitsTrueList = self.listTraitNamesTrue()
        self.travels.refreshTraversal(_traitsTrueList)

    def updateTraitFromLocation(self, locationName):
        _traitNameList = self.travels.returnLocationTraitNameList(locationName)
        for traitName in _traitNameList:
            self.setTraitTrue(traitName)

    def travelRandomly(self):
        self.refreshTraversal()
        _locationName = self.travels.getRandomLocationNameByAccessibility()
        if _locationName == "empty":
            print("There are no rooms left to explore. getRandomLocationNameByAccessibility returned 'empty'") #todo
        else:
            self.travels.visitLocation(_locationName)
            self.updateTraitFromLocation(_locationName)

    def travelRandomlyByTrait(self, traitName):
        self.refreshTraversal()
        _locationName = self.travels.getRandomLocationNameByTraitPrerequisite(traitName)
        if _locationName == "empty":
            print("There are no rooms left to explore with that trait. getRandomLocationNameByTraitPrerequisite returned 'empty'") #todo
        else:
            self.travels.visitLocation(_locationName)
            self.updateTraitFromLocation(_locationName)

    def travelToLocation(self, locationName):
        self.refreshTraversal()
        if self.travels.visitLocation(locationName) == True:
            self.updateTraitFromLocation(locationName)
        else:
            print("Couldn't travel to {}\n".format(locationName)) #todo

    def reportTraits(self):
        for trait in self.traitDictionary.values():
            print(trait.name)

    def reportTraitsTrue(self):     #debug function
        for trait in self.traitDictionary.values():
            if trait.value == True:
                print('Trait: {} {}'.format(trait.name,trait.value))

    def reportTraitsFalse(self):     #debug function
        for trait in self.traitDictionary.values():
            if trait.value == False:
                print('Trait: {} {}'.format(trait.name,trait.value))

    def reportCounters(self):        #debug function
        for counter in self.counterDictionary.values():
            print('Counter: {} - {}'.format(counter.name,counter.counter))

    def reportLocations(self):     #debug function
        for location in self.travels.locationDictionary.values():
            print('Location: {}, Text: {}\n'.format(location.name,location.text))

    def reportVisitedLocations(self):     #debug function
        for location in self.travels.visitedLocationNameList:
            print('Location: {}'.format(location))

    def reportAccessibleLocations(self):     #debug function
        for location in self.travels.accessibleLocationNameList:
            print('Location: {}'.format(location))

    def reportInaccessibleLocations(self):     #debug function
        for location in self.travels.inaccessibleLocationNameList:
            print('Location: {}'.format(location))

    def reportCurrentLocation(self):     #debug function
        print('Current Location: {}'.format(self.travels.currentLocationName))

    def reportInteractables(self):     #debug function
        for location in self.travels.locationDictionary.values():
            print(location.text)
            for interactable in location.interactablesList:
                print("     {}".format(interactable.text))

    def reportInteractablesByLocation(self, locationName):     #debug function
        if locationName in self.travels.locationDictionary:
            _location = self.travels.locationDictionary[locationName]
            for interactable in _location.interactablesList:
                print(interactable.text)
        else:
            print("{} isn't in the locationDictionary".format(locationName))
