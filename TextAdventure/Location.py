import os

from Counter import Counter
from Interactable import Interactable
from Trait import Trait

class Location:
    def __init__(self, name, text, prerequisite):
        self.name = name
        self.text = text
        self.prerequisiteTraitName = prerequisite
        self.traitNameList = []
        self.interactablesList = []

    def displayLocationText(self):
        textfile = "./Text Files/" + self.name + ".txt"
        if os.path.isfile(textfile):
            with open(textfile) as file:
                for line in file:
                    print(line)

    def listAvailableInteractables(self):
        availableInteractables = []
        for interactable in self.interactablesList:
            if interactable.touched == False:
                availableInteractables.append(interactable)
        return availableInteractables

    def touchInteractable(self, interactableName):
        for interactable in self.interactablesList:
            if interactable.name == interactableName:
                interactable.interactWith()

    def getInteractableCounterName(self, interactableName):
        for interactable in self.interactablesList:
            if interactable.name == interactableName:
                return interactable.counterName