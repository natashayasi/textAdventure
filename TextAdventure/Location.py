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

    def listInteractables(self):
        for interactable in self.interactablesList:
            print('Name: {}, Text: {}, CounterName: {}').format(interactable.name, interactable.text, interatable.counterName)
