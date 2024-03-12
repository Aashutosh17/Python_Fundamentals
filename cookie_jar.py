class jar:
    def __init__(self,capacity=30):
        if capacity<0:
            print("ValueError")
        else:
            self._capacity=capacity
        self._size=0

    def __str__(self) -> str:
        return self._size*'🍪'
    
    def deposit(self,n):
        if (self._size+n)>self._capacity:
            print("ValueError")
        else:
            self._size=self._size+n
    
    def withdraw(self,n):
        if (self._size-n)<0:
            print("ValueError")
        else:
            self._size=self._size-n  

    # def copy(self,obj,copy_no):
    #     self.deposit(copy_no)
    #     obj.withdraw(copy_no)

    @property
    def capacity(self):
        return self._capacity
    
    @property   
    def size(self):
        return self._size

j1=jar(capacity=30)
# j2=jar(capacity=30)
print("cookie in",j1)
j1.deposit(10)
print("cookie in",j1)
# j2.deposit(5)
# print("cookie in",j2)

# j1.copy(j2,4)
j1.withdraw(5)
print("cookie in",j1)
# print("cookie in",j2)