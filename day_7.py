'''
OOPS in python
'''

class Vehicle():
    def __init__(self, window=0, wheels=2, door=3):
        self.door = door
        self.window = window
        self.wheels = wheels
        
    def add_wheels(self):
        self.wheels += 1

# Create an instance of the Vehicle class
V1 = Vehicle(2, 3, 2)

# Print the number of wheels before adding
# print("Number of wheels before adding:", V1.wheels)

# Add a wheel
V1.add_wheels()

# Print the number of wheels after adding
# print("Number of wheels after adding:", V1.wheels)


class Teacher():

    def __init__(self,name,age,salary) -> None:
        self.name=name
        self.age=age
        self.salary=salary

    def add_salary(self,new_salary):
        self.salary=self.salary+new_salary
    
    def minus_salary(self,minus):
        self.salary=self.salary-minus

    def __str__(self) -> str:
        return self.name

T1=Teacher('nabin',27,10000)
T2= Teacher('aashutosh',21,15000)
username = input('Enter the Name for Teacher 3: ')
age = int(input('Enter the Age for Teacher 3: '))
salary = int(input('Enter the salary for Teacher 3: '))

T3 = Teacher(username, age, T1.salary+T2.salary)
T3.add_salary(1000)

print(T3.name, T3.salary)

# print(T1.name,T1.salary,T2.name,T2.salary)
# T1.add_salary(1000)
# T2.minus_salary(1000)
# print(T1.name,T1.salary,T2.name,T2.salary)
# print(T1)
