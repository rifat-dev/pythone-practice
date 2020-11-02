class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"My name is {self.name}.I am {self.age} years old")
    
    def chng(self):
        self.age=self.age+1


pr=Person("Rifat",24)
pr.chng()
pr.info()