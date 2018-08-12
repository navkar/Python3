
# Vehicle class and instance methods
class Vehicle():
    # self is like this
    def engine(self):
        print("This vehicle has an engine")
    
    def color(self, color):
        print("The color of this vehicle is " + color)

class Car(Vehicle):
    def engine(self):
        Vehicle.engine(self)
        print("This is a car and not a vehicle")

    # Overrides the implementation of base class
    def color(self, color):
        print("Car's color is " + color)

def main():
    vehicle = Vehicle()
    # no need to pass self
    vehicle.engine()
    vehicle.color("White")

    car = Car()
    car.engine()
    car.color("Red")


if __name__ == "__main__":
    main()


