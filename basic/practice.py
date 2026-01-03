

# Create a class with attributes like brand and model 
# self keyword is a reference of current object 
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def full_name(self,firstName,lastName):
#         return f"{firstName} {lastName} is Car. {self.brand} and model {self.model}"


# toyota_car = Car("Toyota","Corolla")


# print(toyota_car.full_name("Fortuner","lengender"))


# ---------------------Inheritance ------------------------------- 

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def full_name(self,first_name,last_name):
#         return f"{first_name} {last_name} is the fullname of car"


# class ElectricCar(Car):
#     def __init__(self,brand,model,battery,size):
#         super().__init__(brand,model)
#         self.battery = battery
#         self.size = size
    
#     def full_info(self):
#         return f"{self.brand} {self.model} {self.battery} {self.size}"

    

# toyota_car = ElectricCar("Tesla","V4","1000","5v")

# print(toyota_car.full_info())

# ------------------------Encapsulation -------------------------- 

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand

toyota_car = Car("toyota","v4")

print(toyota_car.get_brand())