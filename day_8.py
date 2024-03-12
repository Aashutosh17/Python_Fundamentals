'''
Inheritance in Python
'''

class Grandfather():
    def __init__(self, House, Cash, Land) -> None:
        self.House = House
        self.Cash = Cash
        self.Land = Land

    def minus_cash(self, minus):
        self.Cash -= minus

    def add_land(self, add):
        self.Land += add
  
class Father(Grandfather):
    def __init__(self, House, Cash, Land) -> None:
        super().__init__(House, Cash, Land)

class Son(Father):
    def __init__(self, House, Cash, Land) -> None:
        super().__init__(House, Cash, Land)

G1 = Grandfather(5, 20000, 12)
F1 = Father(G1.House, G1.Cash, G1.Land)
S1 = Son(G1.House, G1.Cash, G1.Land)

# print(G1.House)
# print(F1.House, F1.Cash)
# print(S1.Cash)


G1.minus_cash(5000)
G1.add_land(10)

# print(G1.Cash)
# print(G1.Land)

class Animal ():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age 
        
    def makesounds (self):
        pass
    
class Dog (Animal):
    def __init__(self, name, age,breed) -> None:
        super().__init__(name, age)
        self.breed= breed
        
    def makesounds(self):
        return "Bhau Bhau!"
    
class Cat (Animal):
    def __init__(self, name, age,breed) -> None:
        super().__init__(name, age)
        self.breed= breed
        
    def makesounds(self):
        return "Meow!"
    
dog1 = Dog("Jenny", 4, "Golden retriver")
cat1 = Cat("Kiyo", 3, "Persian Cat")

print(dog1.age)
print(cat1.breed)
print(cat1.makesounds())
