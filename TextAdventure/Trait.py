class Trait:
    def __init__(self, name, text, value):
        self.name = name
        self.text = text
        self.value = value

    def setTraitTrue(self):
        self.value = True

    def setTraitFalse(self):
        self.value = False