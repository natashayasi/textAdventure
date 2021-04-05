class Counter:
    def __init__(self, name, text, counter):
        self.name = name
        self.text = text
        self.counter = counter

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1

    #add win condition check?