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

# print(dog1.age)
# print(cat1.breed)
# print(cat1.makesounds())


class teacher():
    salary=10000

    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        self.email=name+str(age)+'@gmail.com'

    def add_salary_a(self,per):
        self.salary=self.salary *(1+(per/100))

    @staticmethod
    def print_S():
        print("this is static method")
        return "Sucessful"

    @classmethod
    def add_salary(cls,per):
        cls.salary=cls.salary *(1+(per/100))
    
    def __add__(self,obj):
        return self.age+obj.age

t1=teacher('nabin',23)
t2=teacher('aashutosh',25)


print(t1.__dict__)
print(t1.salary,t2.salary,teacher.salary)
t1.salary=10100
print(t1.__dict__)
print(t1.salary,t2.salary,teacher.salary)
teacher.add_salary(10)
print(t1.salary,t2.salary,teacher.salary)
t1.add_salary_a(10)
print(t1.salary,t2.salary,teacher.salary)

print(t1+ t2)