'''
Enter your Name, DOB and Age. Calculate whether the correct age from the DOB 
'''
# current_year = 2024
# your_Name = str(input('Enter your name: '))
# your_Age = int(input('Enter your age: '))
# your_DOB = int(input('Enter your DOB: '))

# print(f"The correct age is {current_year-your_DOB}")



current_year = 2024
your_Name = str(input('Enter your name: '))
your_Age = int(input('Enter your age: '))
your_DOB = int(input('Enter your DOB: '))
calculated_age = current_year-your_DOB

if your_Age == calculated_age:
    print(f"{your_Name}, Your Age is correct!")

else :
    print ('Liar Liar pants on fire! Please enter the correct age!')

