'''
Inheritance in Python
'''

class Grandfather():
    def __init__(self, House, Cash, Land) -> None:
        self.House = House
        self.Cash = Cash
        self.Land = Land

class Father(Grandfather):
    def __init__(self, House, Cash, Land) -> None:
        super().__init__(House, Cash, Land)

class Son(Father):
    def __init__(self, House, Cash, Land) -> None:
        super().__init__(House, Cash, Land)

G1 = Grandfather(5, 20000, 12)
F1 = Father(G1.House, G1.Cash, G1.Land)
S1 = Son(G1.House, G1.Cash, G1.Land)

print(G1.House)
print(F1.House, F1.Cash)
print (S1.Cash)






    
