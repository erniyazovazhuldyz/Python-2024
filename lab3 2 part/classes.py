class myClass:
    def _init_(self) :
        self.inputstr = ""
    def getstring(self) :
        self.inputstr = input("enter: ")
    def printstring(self) :
        print(self.inputstr.upper())
myClass = myClass()
myClass.getstring()
myClass.printstring()
#classes task1

class Shape :
    def _init_(self) :
        pass
    def area(self):
        return 0
class square(Shape) :
    def _init_(self, length):
        self.length=length
    def area(self):
        return self.length ** 2
Shape = Shape()
print("area of shape: " , Shape.area())
square = square(3)
print("area of square: ", square.area())
#2task

class shape :
    def _init_(self) :
        pass
    def area(self):
        return 0
class rectangle(shape):
    def _init_(self,length, width):
        self.length=length
        self.width=width
    def area(self) :
        return self.length * self.width
shape = shape()
print("area of shape: ", shape.area())
rectangle = rectangle(3,5)
print("area of rectangle: ", rectangle.area())
#3task

import math 
class point :
    def _init_(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print("coordinates: ",(self.x, self.y))
    def move(self, newx, newy):
        self.x=newx
        self.y=newy
    def dist(self,point2):
        dx=self.x-point2.x
        dy=self.y-point2.y
        distance = math.sqrt(dx*2 + dy*2)
        return distance
point1=point(1,2)
pointt2 = point( 3, 4)
point1.show()
pointt2.show()
distance = point1.dist(pointt2)
print("distance between two points: ", distance)
point1.move(2,3)
pointt2.move(4,5)
point1.show()
pointt2.show()
#4task

class account :
    def _init_(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,sum):
        if sum>0:
            self.balance+=sum
            print("deposit: ", self.balance)
        else:
            print("error")
    def withdraw(self,sum):
        if sum>0:
            if sum<=self.balance:
                self.balance-=sum
                print("deposit after withdraw: ", self.balance)
            else:
                print("insufficient funds")
        else:
            print("error")
account=account("Aya", 360000)
account.deposit(500)
account.withdraw(500)
#5task

def is_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n%i==0:
                return False
        return True
    
numbers = {1, 2, 3, 4, 5, 6, 7, 8}
filter_func=lambda x:is_prime(x)
prime_num=list(filter(filter_func, numbers))

print("numbers: ", numbers)
print("prime numbers: ", prime_num)
#6task


