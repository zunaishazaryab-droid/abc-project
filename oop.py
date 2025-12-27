class Car:
    name="BMW"
    color="black"
    def forward(self):
        print("car is about to br forwarded")
obj=Car()
obj.forward()
print(obj.name)


class Computer:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def quailty(self):
        print("this is the best quailty of computer")
obj=Computer("hp","i3","black")
obj.quailty()
print(obj.name)
print(obj.model)
print(obj.color)



class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def forward(self):
        print("car is about to be forwarded")
    @staticmethod
    def booster_mode():
        print("you enabled the booster mode")
obj=Car("bmw","i34484","black")
obj.forward()
print(obj.name)
print(obj.model)
print(obj.color)
Car.booster_mode()


class Computer:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
        self.__hardware_type="type a"
    def hardware_type(self):
        print(self.__hardware_type)
obj=Computer("Arizona","Arizona","red")

print(obj.name)
print(obj.model)



class Car:
    def __init__(self,doors,seats,color):
        self.doors=doors
        self.seats=seats
        self.color=color
    def forward(self):
            print("car is about to be forwarded")
class BMW(Car):
    def __init__(self,model,doors,seats,color):
        super().__init__(doors,seats,color)
        self.model=model
    def price(self):
        print("car price")
obj=BMW(model="BMW",doors=5,seats=5,color="red")


class Animal:
    def sound(self):
        print("Some generic sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")

obj = Animal()
obj.sound()

obj2 = Cat()
obj2.sound()
obj3 = Dog()
obj3.sound()


class Car:
    def fuel_type(self):
        print("car uses some fuel type")

class electric_car(Car):
    def fuel_type(self):
        print("electric car uses some fuel type")
class truck(Car):
    def fuel_type(self):
        print("truck uses some fuel type")
obj = Car()
obj.fuel_type()
obj2 = truck()
obj2.fuel_type()
obj3 = electric_car()
obj3.fuel_type()


