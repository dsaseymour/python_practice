class Car: 
    def __init__(self,color,mileage):
        self.color=color 
        self.mileage=mileage
    def __repr__(self):
        return f"This car is {self.color}. It has {self.mileage} miles"
    def drive(self,n):
        self.mileage+=n
