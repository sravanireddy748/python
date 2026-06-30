# Assignment Operators
# Take a number and perform the following operations using assignment operators:
# Add 10
# Subtract 5
# Multiply by 2
# Divide by 3

a=97
print(a-5)
print(a+10)
print(a*2)
print(a/3)

# Swap two numbers without using a third variable.

a=2
b=4
temp=a
a=b
b=temp
print(a)
print(b)

# Check whether a given number is greater than, less than, or equal to another number.

# a=int(input("enter first value: "))
# b=int(input("enter second value: "))
# if(a>b):
#     print("a is greater than b")
# elif(a<b):
#     print("b is greater than  a")
# else:
#     print("a is equals to b")

# Write a program to determine whether a student has passed (marks >= 35).
# a=int(input("enter student marks: "))
# if(a>=35):
#     print("student passed")
# else:
#     print("student failed")

# Check whether a person is eligible to vote (age >= 18) and has valid ID proof.
# age=int(input(" enter person age: "))
# if(age>=18):
#     print("person is eligible to vote")
# else:
#     print("person is not eligible to vote")

#Check whether a number lies between 1 and 100 using logical operators.
numb=int(input("enter a number: "))
if numb>=1 and numb<=100:
    print("the number lies between 1 and 100")
else:
    print("the number not lies between 1 to 100")


# Perform bitwise AND, OR, XOR, and NOT operations on two numbers.

print(3>4 and 45>90 and 10<9)
print(10==10 and 3>2)

# OR operator
print(4==4 or 4>5)    # atleast one condition must be true among multiple conditions
print(3<4 or 45<90 or 10<9)

# NOT OPETATOR
print(not 3<4 or 45<90 or 10<9 )    # 3<4 or 45<90 or 10<9 are false so not will be applied for that so it will be true
print(10<=10 and (not 10!=10))
