class Water:
    def display(self):
        print("Filled - not empty")


class Bottle:
    def __init__(self):
        self.filled_with = Water()

    def fill(self):
        self.filled_with.display()


bottle_obj = Bottle()
bottle_obj.fill()
