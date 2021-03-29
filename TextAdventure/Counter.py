class Counter:
    def __init__(self, name):
        self.name = name
        self.counter = 0

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1