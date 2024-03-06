'''
if else conditions in python
'''
marks = int(input('Enter your marks: '))
if (marks>=100):
    print("Distinction")
elif(marks>60 and marks<80):
    print("First division")
elif(marks>40 and marks<60):
    print('Pass')
else:
    print("Go for re-exam")
    
    
    
a = int(input('Enter your num a: '))
b = int(input('Enter your num b: '))
c = int(input('Enter your num c: '))

if (a>=b and a>=c):
    print(f'a {a} is greater!')
    if(b<c):
        print(f'b {b} is smallest!')
    else:
        print(f'c {c} is smallest!')
elif(b>=c):
    print(f'b {b} is greater!')
    if(a<c):
        print(f'a {a} is smallest!')
    else:
        print(f'c {c} is smallest')

else:
  print(f'c {c} is greater!')
  
  
if (a>=b ):
    greatest = a 
    smallest = b
    if(b<c):
        smallest = b
elif(b>=c):
    greatest = b
    smallest = c 
    if(a<c):
       smallest = a 
else:
    greatest = c 
    smallest = b 
    if (a<b):
        smallest = a 

print('smallest' + str(smallest) + 'largest'+str(greatest))
 

n = int(input('Enter your num n: '))




   
    