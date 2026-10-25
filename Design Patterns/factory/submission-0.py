# things to know before we answer this question
#           class vs object 

# class would be blueprint from where you would create somethin like a house and an object is the actual house being build, let me give you an example 

# class ->  blueprint 
# object -> thing build from it 

# example: 

    # class Car: 

        # def getType(self):

            # return "Car"

# my_car = Car() -> card being build 

# my_car.getType() -> this will return Car


# ----------------------- method ------------------------------------------# 

# a method is the function that you lives inside a class. 

# you would call a method in an object. 


# -------------------- self --------------------------------------------- # 

# self = the object this method is being called on 
# my_car.getType() -> inside getType, self IS my_car.  self is the body that is use for the object 

# every method need self as a first parameter 



# --------------------- inheritance --------------------------- 

# class Car(Vehicles) - means car is a vehicle

# so every that vehicles has, car gets it too 



# ------------------- ABSTRACT CLASS (abc + @abstractmethod) --------------- 

# a contract class. you cant build it directly. it says: every child must write this method 

# class vehicle(abc):
# @abstractmethod 
#     def getType(self): pass 
# means every vehi
# vehicle() alone -> error. Car() -> works, becasue Car wrote getype 


# ----------------------- factory method pattern ---------------------------- 

#  a factory is a class whose only job is to build and return and object. 

# class carfactory(vehicleFactory): 
#       def createVehicle(self):
#            return Car()               # builds a car and hands it back 


# why bother_ the code using the factory doestn need to know which vehicle it gets. it just calls createVehicle()
# swap the factoyy, get a different vehicle, and change no other code.


# so is the same thing as: 

# my_car = car(), is the same idea, the only difference is that we do that in the actual class, the reason we do it like that, is becasue we if we need to change something from the that class, inteado of doing in code for a really long time, what you would do, you would do it there so that you change that instead of chaging the whole thing 

# every function using it will update 








class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()
    
class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
    # Write your code here
        return Bike()

class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
    # Write your code here
        return Truck()


# the whole idea is to have a class that creates the object, that way if you want to change something gloabally for that one thing you can do so. 