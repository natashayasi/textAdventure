class Interactable(object):
    def __init__(self, name, text, counterName):
        self.name = name
        self.text = text
        self.counterName = counterName
        self.touched = False

    def interactWith(self):
        self.touched = True