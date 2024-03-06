'''
loops
'''
list_a = [x**2 for x in range(10)]
print(list_a)

list_a = [x**2 for x in range(10)if x%2!=0]
print(list_a)

'''
list comprehension 
'''
dict_desc = { 2 : "exciting",
             3 : "fantastic",
             4 : "virtuous",
             5 : "heart-warming",
             6 : "tear-jerking",
             7 : "beautiful",
             8 : "exhilirating",
             9 : "emotional",
             10 : "inspiring"}

userinput = int(input("Enter any number:"))

list_desc = [ value for key, value in dict_desc.items() if userinput % key == 0]
print(f"the most brilliant {', '.join(list_desc)} number is {userinput}")

user_input = str(input("Enter any name:"))
uppercase_letters = [char.upper() for char in user_input ]
print(uppercase_letters)

'''
Functions in Python
'''
# Call, Arguement, parameter, return 



            
    