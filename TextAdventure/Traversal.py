import random

class Traversal:
    def __init__(self, roomsDict, startingDict):
        self.locationDict = roomsDict.copy()
        self.locationDict.update(startingDict) #might cause an issue if the roomsDict is changed
        self.startingLocationsDict = startingDict.copy()
        self.visitedLocationsDict = {}
        self.accessibleLocationsDict = {}
        self.inaccessibleLocationsDict = roomsDict.copy()
        self.currentLocation = "Start"

    def addToVisited(self, location):
        self.visitedLocationsDict.update({location: self.locationDict[location]})

    def RemovefromVisited(self, location): #debug function
        if location in self.visitedLocationsDict:
            self.visitedLocationsDict.pop(location)

    def addToAccessible(self, location):
        self.accessibleLocationsDict.update({location: self.locationDict[location]})
    
    def removeFromAccessible(self, location):
        if location in self.accessibleLocationsDict:
            self.accessibleLocationsDict.pop(location)

    def addToInaccessible(self, location): #debug function
        self.inaccessibleLocationsDict.update({location: self.locationDict[location]})

    def removeFromInaccessible(self, location):
        if location in self.inaccessibleLocationsDict:
            self.inaccessibleLocationsDict.pop(location)

    def updateAccess(self, traitDict):
        for location in self.inaccessibleLocationsDict.values():
            if self.traitDict[location.prerequisite].value == True:
                self.addToAccessible(location)
                self.removeFromInaccessible(location)

    def updateVisited(self, currentLocation):
        self.removeFromAccessible(currentLocation)
        self.addToVisited(currentLocation)

    def getAccessibleLocation(self):
        _location = random.choice(list(self.accessibleLocationsDict.values()))
        return _location.name
