# inheritance
# multi level inheritance
# multipal inherentance

class Math1:
    def __init__(self,x,y):  
        self.x=x
        self.y=y


    def sum(self):
        z=self.x + self.y
        print(z)

class Math2(Math1):
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def sub(self):
        q=self.x - self.y
        print(q)

obj_1= Math2(6,4)
obj_1.sub()
obj_1.sum()


# multipal inherentance

class Rifat:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self):
        z=self.x+self.y
        print(z)

class Rifat1:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sub(self):
        q=self.x-self.y
        print(q)

class Claculator(Rifat,Rifat1):
    pass

obj=Claculator(10,5)
obj.sum()
obj.sub()

        
# multi level inheritance

class Person:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self):
        c=self.x+self.y
        print(c)

class Person1(Person):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sub(self):
        v=self.x-self.y
        print(v)

class Person2(Person1):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def mulipal(self):
        v=self.x*self.y
        print(v)

object_1=Person2(10,4)
object_1.sum()
object_1.sub()
object_1.mulipal()
