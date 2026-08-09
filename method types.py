
1)python :-- create static,class,instace method

class sravani:
    def student(self,name,branch,age,college):
        print("name:",name)
        print("branch:",branch)
        print("age:",age)
        print("college:",college)
obj1=sravani()
obj1.student('sravani',"cse",21,"mlwec")

class sravani:
    name='sravani'
    age=21
    branch='cse'
    college='mlwec'
    def student(self):
        print("name:",sravani.name)
        print("age:",sravani.age)
        print("branch:",sravani.branch)
        print("college:",sravani.college)
obj1=sravani()
obj1.student()

class sravani:
    name='sravani'
    age=21
    branch='cse'
    college='mlwec'
    @classmethod
    def student(cls):
        cls.name="arya"
        print("name:",sravani.name)
        print("age:",sravani.age)
        print("branch:",sravani.branch)
        print("college:",sravani.college)
    def stud1(self):
        print("name:",sravani.name)
        print("age:",sravani.age)
obj1=sravani()
obj1.student()
obj1.stud1()


class sravani:
    @staticmethod
    def mymethod(a,b):
        print("welcome to Data Science")
        print(a+b)
obj=sravani()
obj.mymethod(10,20)