class Trait:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.value = False

    def setTraitTrue(self):
        self.value = True

    def setTraitFalse(self):
        self.value = False