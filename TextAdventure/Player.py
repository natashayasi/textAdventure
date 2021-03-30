class Player:
    def __init__(self, name, trait, counter, traversal):
        self.name = name
        self.traitDict = trait
        self.counterDict = counter
        self.travels = traversal
        self.currentLocation = "Start"

    def setTraitTrue(self, traitName):
        if traitName in self.traitDict:
            self.traitDict[traitName].setTraitTrue()     

    def setTraitFalse(self, traitName):
        if traitName in self.traitDict:
            self.traitDict[traitName].setTraitFalse()

    def incrementCounter(self, counterName):
        if counterName in self.counterDict:
            self.counterDict[counterName].increment()

    def decrementCounter(self, counterName):
        if counterName in self.counterDict:
            self.counterDict[counterName].decrement()

    def addRoomToVisited(self, location):
        self.travels.addToVisited(location)

    def addRoomToAccessible(self, location):
        self.travels.addToAccessible(location)
    
    def removeRoomFromAccessible(self, location):
        self.travels.removeFromAccessible(location)

    def removeRoomFromInaccessible(self, location):
        self.travels.removeFromInaccessible(location)

    def triggerLocationTraitAdd(self, locationName):
        self.setTraitTrue(self.travels.locationDict[locationName].trait1)
        self.setTraitTrue(self.travels.locationDict[locationName].trait2)
        self.setTraitTrue(self.travels.locationDict[locationName].trait3)

    def leaveLocation(self):
        self.travels.addToVisited(self.currentLocation)
        self.travels.removeFromAccessible(self.currentLocation)

    def travelToRandomLocation(self):
        self.leaveLocation()
        self.currentLocation = self.travels.getAccessibleLocation()
        self.triggerLocationTraitAdd(self.currentLocation)

    def travelToLocation(self, location):
        self.leaveLocation()
        self.currentLocation = location
        self.triggerLocationTraitAdd(self.currentLocation)

    def reportTraitsTrue(self):     #debug function
        for trait in self.traitDict.values():
            if trait.value == True:
                print('Trait: {} {}\n'.format(trait.name,trait.value))

    def reportTraitsFalse(self):     #debug function
        for trait in self.traitDict.values():
            if trait.value == False:
                print('Trait: {} {}\n'.format(trait.name,trait.value))

    def reportCounters(self):        #debug function
        for counter in self.counterDict.values():
            print('Counter: {} - {}\n'.format(counter.name,counter.counter))

    def reportLocationDict(self):     #debug function
        for location in self.travels.locationDict.values():
            print('Location: {}, Text: {}\n'.format(location.name,location.text))

    def reportStartingLocationsDict(self):     #debug function
        for location in self.travels.locationDict.values():
            print('Location: {}, Text: {}\n'.format(location.name,location.text))

    def reportVisitedLocationsDict(self):     #debug function
        for location in self.travels.visitedLocationsDict.values():
            print('Location: {}, Text: {}\n'.format(location.name,location.text))

    def reportAccessibleLocationsDict(self):     #debug function
        for location in self.travels.accessibleLocationsDict.values():
            print('Location: {}, Text: {}\n'.format(location.name,location.text))

    def reportInaccessibleLocationsDict(self):     #debug function
        for location in self.travels.inaccessibleLocationsDict.values():
            print('Location: {}, Text: {}\n'.format(location.name,location.text))

    def reportCurrentLocation(self):
        print('Current Location: {}'.format(self.currentLocation))