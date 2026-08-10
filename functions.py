# function withought parameters
def adding():
    print(10+20+30+55)
adding()

def even():
    a=int(input("enter a value: "))
    if a%2==0:
        print("even")
    else:
        print("odd")
even()


def rectangleornot():
    height=int(input("enter height of a rectangle:"))
    width=int(input("enter width of a rectangle:"))
    if height!=width:
        print("it is rectangle")
    else:
        print("not a rectangle")
rectangleornot()
    

# functions with parameters
def certificate(name,age,branch,year,marks,college):
    print("         certificate           ")
    print("fullname        :",name)
    print("age             :",age)
    print("marks           :",marks)
    print("branch          :",branch)
    print("college         :",college)
    print("year of passing :",year)
certificate("sravani",21,"cse",2026,87,"mlwec")

# types of with parameter function

# positional arguments
def math(a,b,c,d):
    if a>b and a>c and a>d:
        print("a is greater")
    elif b>a and b>c and b>d:
        print("b is greater")
    elif c>a and c>b and c>d:
        print("c is greater")
    else:
        print("d is greater")
math(87,764,9835,764532)

# default arguments
# default argument must be declare in the last positions 
def certificate (name,branch,marks,age=21,year=2026,college='mlwec'):
    print("         certificate           ")
    print("fullname        :",name)
    print("age             :",age)
    print("marks           :",marks)
    print("branch          :",branch)
    print("college         :",college)
    print("year of passing :",year)
certificate('sravani','cse',76)

# keyword arguments
# we can change the position of an argument
def details(name,age,location,salary):
    if location =="hyd" and age>18:
        print("eligible for apllication")
        print("name:",name)
        print("salary:",salary)
details(location="hyd",name="sravani",salary=60000,age=21)

# * arguments
def math(*a):
    print(a+a)
    print(a+a+a)
    print(a+a+a+a)
math(10,39,47,85)

def math(*a):
    total=0
    for i in a:
        total=total+i
        print(total)
math(20,43,67,98)
# ** kwarguments 
# it will take values in the form of key and value pairs which is nothing but dictionary
def details(**a):
    print(a)
details(name="prabha",age=45,identity="hero")


