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
        self.visitedLocationsDict.append(location)

    def RemovefromVisited(self, location): #debug function
        self.visitedLocationsDict.pop(location)

    def addToAccessible(self, location):
        self.accessibleLocationsDict.append(location)
    
    def removeFromAccessible(self, location):
        self.accessibleLocationsDict.pop(location)

    def addToInaccessible(self, location): #debug function
        self.inaccessibleLocationsDict.append(location)

    def removeFromInaccessible(self, location):
        self.inaccessibleLocationsDict.pop(location)

    def updateAccess(self, traitDict):
        for location in self.inaccessibleLocationsDict.values():
            if self.traitDict[location.prerequisite].value == True:
                addToAccessible(location)
                removeFromInaccessible(location)

    def updateVisited(self, currentLocation):
        removeFromAccessible(currentLocation)
        addToVisited(currentLocation)

    def getAccessibleLocation(self):
        _location = random.choice(list(accessibleLocationsDict.values()))
        return _location.name
