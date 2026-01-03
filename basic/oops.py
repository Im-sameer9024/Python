

#----------------------- Create a Car class with attributes like brand and model . then create a instance of class


# class Car:
#     def __init__(self, brand, model):   #__init__ is a constructor which is call automatically when we create an instance of class
#         self.brand = brand
#         self.model = model
#         print(f"Car {self.brand} {self.model} is created")


# toyota_car = Car("Toyota", "Corolla")

# ---------------------------- create a function in class to print the full name of a car ---------------

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def get_fullname(self,first_name,last_name):
#         return f"{first_name} {last_name} is a Car. {self.brand} {self.model}"


# my_car_name = Car("Toyota","Corolla")

# print(my_car_name.get_fullname("Rahul","Kumar")) # Rahul Kumar is a Car. Toyota Corolla


#------------------------- Inheritance -------------------------

# child class take the properties of the parent class 

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model


# class ElectricCar(Car):
#     def __init__(self,brand,model,battery,size):
#         super().__init__(brand,model)
#         self.battery = battery
#         self.size = size
        
#     def get_full_details(self):
#         return f"{self.brand} {self.model} is a {self.size} electric car with {self.battery} battery"
    
    
# tesla = ElectricCar("Tesla","Model S","1000","Large")

# print(tesla.get_full_details())


#---------------------------- Encapsulation ------------------------

# Encapsulation is a concept in object-oriented programming that allows the bundling of data and methods that operate on that data within a single unit, called an object. It is a way to hide the internal state of an object and expose only the necessary information to the outside world.

# if i add __ before any variable then it will be private variable and we can't access it outside the class 

# class Car:
#     def __init__(self,brand,model):
#         self.__brand = brand # private variable
#         self.model = model
        
#     def get_brand(self):
#         return self.__brand
    
#     def get_model(self):
#         return self.model
    
    
# toyota = Car("Toyota","Corolla")

# print(toyota.get_brand())


# --------------------------- Polymorphism ----------------------------

# Demonstrate polymorphism by defining a method fuel_type in both Car and Electric_car class , but with different behaviors.abs


# class Car:
#     total_car = 0
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         Car.total_car += 1
        

#     def fuel_type(self):
#         return "Petrol or Diesel"
        
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery,size):
#         super().__init__(brand,model)
#         self.battery = battery
#         self.size = size
    
#     def fuel_type(self):
#         return "Electric Charge"
    
    
# # here Car and ElectricCar is different Class but they have same method name fuel_type() but they have different behavior 


# tesla = ElectricCar("Tesla","Model S","1000","Large")

# print(tesla.fuel_type())

# safari = Car("Toyota","Corolla")

# print(safari.total_car)

#----------------------- add a static method to the class that give the description of Car --------------------


# class Car:
#     total_car = 0
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         Car.total_car += 1
        

#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod
#     def description():
#         return "Car is a vehicle that runs on fuel"
        
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery,size):
#         super().__init__(brand,model)
#         self.battery = battery
#         self.size = size
    
#     def fuel_type(self):
#         return "Electric Charge"
    
    
# toyota = ElectricCar("Tesla","Model S","10000","flks")
    
# print(toyota.description())
# print(Car.description())


# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# class Battery:
#     def battery_info(self):
#         return "Battery info"

# class Engine:
#     def engine_info(self):
#         return "Engine info"

# class ElectricCar(Car,Battery,Engine):
#     def __init__(self,brand,model,battery,size):
#         super().__init__(brand,model)
#         self.battery = battery
#         self.size = size


# my_new_tesla = ElectricCar("Tesla","Model S","1000","Large")


# print(my_new_tesla)    
    