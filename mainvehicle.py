class Vehicle:                                                                   # Created a Base class Vehicle.
    def __init__(self, model, rental_rate):                                      # A function created and its attributes are model and rental rate.
        self.model = model
        self.rental_rate = rental_rate
    def Calculate_rental_cost(self, days):                                       # Another function created to calculate rental rate.
        return days * self.rental_rate

class Car(Vehicle):                                                              # Created a child  class from base class called vehicle.
    def __init__(self, model, rental_rate,):
        super().__init__(model, rental_rate)                                     # Used super init method to access the  parent class.
    def Calculate_rental_cost(self, days):
        return f" for rent car {self.model} , {self.rental_rate * 3} per day "

class Bike(Vehicle):                                                             # Used a child  class called Bike.
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)                                     # Using super keyword for access the elements in parent class.
    def Calculate_rental_cost(self, days):
        return f" for rent Bike {self.model} , {self.rental_rate * 0.5} per day " # Used to return the rental rate according to days used.

class Truck(Vehicle):                                                             # Created a child class called Truck and its inherited some attributes from Vehicle which is base class.
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)
    def Calculate_rental_cost(self, days):
        return f" for rent truck {self.model} , {self.rental_rate * 4} per day "
car = Car("BMW", 1000)                                            # Assigning values to produce  suitable output for the program.
bike = Bike("Kawasaki z9", 5000)
truck = Truck("Toyota", 1500)
print(car.Calculate_rental_cost(3))
print(bike.Calculate_rental_cost(0.4))
print(truck.Calculate_rental_cost(4))