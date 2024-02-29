'''
Mutable Objects vs Immutable objects
'''

list_A = [1,2,3]
str_A = "Deer"

list_B = list_A [:]
str_B = str_A

# # print (list_A,list_B)
# # print (str_A, str_B)

str_A = "Dog"
list_A.append(6) # add 6 in list_A
# # print(list_A,str_A)


list_A [0]=10 # replace 0 with 10 
# # print(list_A)

'''
Python Operations
'''
# print(list_A == list_B )
# print(list_A is list_B)
# print ( 5 in list_A)


''' String Operations'''

a = ["Bachelors", "Masters", "PostGrad"]
# print(A[0])
# print(A[2][0:2])
c= [1,2,3]
b = '    motorcycle  bike'
# print (b.upper())
# print (b.lower())
# print(b.strip())
# print(b.replace('oto', 'bb'))
print(b.split('e'))

'''List Operations '''
a.append(30)
# print(a)
# a.clear()
# print(a)
b= a.copy()
# print(b)
# print(id(b), id(a))
# print(a.count('Masters'))


