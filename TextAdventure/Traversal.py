import random

from Counter import Counter
from Interactable import Interactable
from Location import Location
from Trait import Trait

class Traversal:
    def __init__(self):
        self.locationDictionary = {}
        self.currentLocationName = "Start"
        self.visitedLocationNameList = []
        self.accessibleLocationNameList = []
        self.inaccessibleLocationNameList = []
        self.setupTraversal

    def setupTraversal(self):
        for location in self.locationDictionary.values():
            self.inaccessibleLocationNameList.append(location.name)

    def addToVisitedLocationNameList(self, locationName):
        if locationName not in self.visitedLocationNameList:
            self.visitedLocationNameList.append(locationName)

    def addToAccessibleLocationNameList(self, locationName):
        if locationName not in self.accessibleLocationNameList:
            self.accessibleLocationNameList.append(locationName)

    def addToInaccessibleLocationNameList(self, locationName):
        if locationName not in self.inaccessibleLocationNameList:
            self.inaccessibleLocationNameList.append(locationName)

    def removeFromVisitedLocationNameList(self, locationName):
        if locationName in self.visitedLocationNameList:
            self.visitedLocationNameList.remove(locationName)

    def removeFromAccessibleLocationNameList(self, locationName):
        if locationName in self.accessibleLocationNameList:
            self.accessibleLocationNameList.remove(locationName)

    def removeFromInaccessibleLocationNameList(self, locationName):
        if locationName in self.inaccessibleLocationNameList:
            self.inaccessibleLocationNameList.remove(locationName)

    def refreshTraversal(self, traitNameList):
        if self.currentLocationName not in self.visitedLocationNameList:
            self.visitedLocationNameList.append(self.currentLocationName)
        for location in self.locationDictionary.values():
            if location.prerequisiteTraitName in traitNameList:
                if location.name not in self.accessibleLocationNameList:
                    self.accessibleLocationNameList.append(location.name)
                    if location.name in self.inaccessibleLocationNameList:
                        self.inaccessibleLocationNameList.remove(location.name)
    
    def visitLocation(self, locationName):
        if locationName in self.accessibleLocationNameList:
            if self.currentLocationName not in self.visitedLocationNameList:
                self.visitedLocationNameList.append(self.currentLocationName)
            self.currentLocationName = locationName
            self.displayLocation(self.currentLocationName)
            return True
        else:
            return False

    def displayLocation(self, locationName):
        self.locationDictionary[locationName].displayLocationText()
        availableInteractables = self.locationDictionary[locationName].listAvailableInteractables()
        if len(availableInteractables) > 0:
            print("For Debug Only: ")
            for interactable in availableInteractables:
                print('Interactable Object: {}'.format(interactable.name))

    def checkInteractableExists(self, interactableName):
        exists = False
        for interactable in self.locationDictionary[self.currentLocationName].interactablesList:
            if interactable.name == interactableName:
                exists = True
        return exists

    def touchInteractable(self, interactableName):
        if self.checkInteractableExists(interactableName):
            self.locationDictionary[self.currentLocationName].touchInteractable(interactableName)

    def getInteractableCounterName(self, interactableName):
        counterName = ""
        if self.checkInteractableExists(interactableName):
            counterName = self.locationDictionary[self.currentLocationName].getInteractableCounterName(interactableName)
        return counterName


    def returnLocationTraitNameList(self, locationName):
        _traitNameList = []
        for location in self.locationDictionary.values():
            if location.name == locationName:
                _traitNameList = location.traitNameList.copy()
                break
        return _traitNameList

    def getRandomLocationNameByAccessibility(self):
        _possibleLocationNamesList = [locationName for locationName in self.accessibleLocationNameList if locationName not in self.visitedLocationNameList]
        if len(_possibleLocationNamesList) > 0:
            _locationName = random.choice(_possibleLocationNamesList)
            return _locationName
        else: 
            return "empty"

    def getRandomLocationNameByTraitPrerequisite(self, traitName):
        _traitAssociatedNamesList = []
        for location in self.locationDictionary.values():
            if location.prerequisiteTraitName == traitName:
                _traitAssociatedNamesList.append(location.name)
        _possibleLocationNamesList = [locationName for locationName in self.accessibleLocationNameList if locationName not in self.visitedLocationNameList and locationName in _traitAssociatedNamesList]
        if len(_possibleLocationNamesList) > 0:
            _locationName = random.choice(_possibleLocationNamesList)
            return _locationName
        else:
            return "empty"

