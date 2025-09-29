class   Car:
    def __init__(self,seats ,doors, colors):
        self.seats=seats
        self.doors=doors
        self.colors=colors
    def forward_car(self):
        print("car is about to be forwarded")
class BMW(Car):
    def __init__(self,model,seats,doors,colors):
        super().__init__(seats,doors,colors)
        self.model=model
    def price(self):
        print("price is about to be printed")
obj=BMW("As18283",4,4,"red")
obj.forward_car()
obj.price()
print(obj.seats)

