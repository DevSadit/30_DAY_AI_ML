# abstraction: hide unnecesary things on code. like here we just want to start a car. except knowing whats going on under the hood. that is the work of abstraction.

# capsulation: Wrapping data and functions into a single unit (object).


class Car:
    def __init__(self):
        acc = False
        clutch = False
        brk = False

    def start(self):
        clutch = True
        acc = True
        print("Car started...")


car1 = Car()
car1.start()
