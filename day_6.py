'''
Lambda function, try/ catch, filter
'''

# sum = lambda a,b : a+b

# print(sum(1,2))
# print(sum(2,3))

# p=float(input('enter principle:'))
# r=float(input('enter rate:'))/100.0
# t=float(input('enter time:'))

# A= lambda p,t,r : p*((1+r)**t)

# print(A(p,t,r))
# A=1.0
# B=6.0
# C=-5.0
# p= lambda a,b,c : (-b+((b*b-4*a*c)**(1/2)))/(2*a)
# r= lambda a,b,c : (-b-((b*b-4*a*c)**(1/2)))/(2*a)
# print('{:.3f} {:.3f}'.format(p(A,B,C),r(A,B,C)))

# a=1
# b='2'

# try:
#     print(a+b)
# except TypeError:
#     print(str(a)+b)
# except ZeroDivisionError:
#     print('cannot be divisible by zero')
# except:
#     print('unknown error')

# print('hello ')

def square(num):
    return num*num

def add (num1,num2):
    return num1+num2

def even(num):
    if num%2==0:
        return num

list_a=[2,4,56,12,56]
list_b =[2,3,5,6,7]
list_c=['nabin','sushant','saurav','prabesh']

out=list(map(square,list_a))
out_2=list(map(lambda num:num*num ,list_a))
add_o=list(map(add,list_a,list_b))
split_a=list(map(list,list_c))

even_o=list(filter(even,list_b))

print(out)
print(out_2)
print(add_o)
print(split_a)
print(even_o)