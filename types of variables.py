#variable: it will store the memory location of a data
#global variable
a=190
class myname:
    def  __init__(self):
        print("constuctor:",a)
    def mymethod(self):
        print("method:",a) 
def arundathi(self):
        print("function:",a)
class my_name:
    def add(self):
        print(a)
       
obj=myname()
obj.mymethod()
obj.arundathi()
obj1=my_name()
obj1.add()

#local variable

class d19:
    def __init__(self):
        a=10
        print("constructor:",a)
    def value(self):
        b=387
        print("method:",b)
def fun():
    c='sravani'
    print("function:",c)
obj=d19()
obj.value()
fun()

#class variable
class d19r:
    a=19
    def __init__(self):
       
        print("constructor:",d19r.a)
    def mymethod(self):
        print("method:",d19r.a)
def fun():
    print("function:",d19r.a)
obj=d19r()
obj.mymethod()
fun()


#instance variable
class d19r:
    def __init__(self):
        self.a=10
        print("constructor:",self.a)
    def mymethod(self):
        print("method:",self.a)

obj=d19r()
obj.mymethod()

