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
        self.travels.refreshTraversal(listTraitNamesTrue())

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

    def travelRandomlyByTrait(self):
        self.refreshTraversal()
        _locationName = self.travels.getRandomLocationNameByTraitPrerequisite()
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

    def reportTraitsTrue(self):     #debug function
        for trait in self.traitDictionary.values():
            if trait.value == True:
                print('Trait: {} {}\n'.format(trait.name,trait.value))

    def reportTraitsFalse(self):     #debug function
        for trait in self.traitDictionary.values():
            if trait.value == False:
                print('Trait: {} {}\n'.format(trait.name,trait.value))

    def reportCounters(self):        #debug function
        for counter in self.counterDictionary.values():
            print('Counter: {} - {}\n'.format(counter.name,counter.counter))

    def reportLocationDict(self):     #debug function
        for location in self.travels.locationDictionary.values():
            print('Location: {}, Text: {}\n'.format(location.name,location.text))

    def reportVisitedLocations(self):     #debug function
        for location in self.travels.visitedLocationNameList:
            print('Location: {}'.format(location))

    def reportAccessibleLocationsDict(self):     #debug function
        for location in self.travels.accessibleLocationNameList:
            print('Location: {}'.format(location))

    def reportInaccessibleLocationsDict(self):     #debug function
        for location in self.travels.inaccessibleLocationNameList:
            print('Location: {}'.format(location))

    def reportCurrentLocation(self):
        print('Current Location: {}'.format(self.travels.currentLocation))



