#logical operators
# AND operation


print(3>4 and 45>90 and 10<9)
print(10==10 and 3>2)

# OR operator
print(4==4 or 4>5)    # atleast one condition must be true among multiple conditions
print(3<4 or 45<90 or 10<9)

# NOT OPETATOR
print(not 3<4 or 45<90 or 10<9 )    # 3<4 or 45<90 or 10<9 are false so not will be applied for that so it will be true
print(10<=10 and (not 10!=10))


#identity operator

# IS OPERATOR

a=10
b=10
print(id(a))
print(id(b))
print(a==b)
print(a is b)  # it will check the address of the variable is same or not #140731863582104 #140731863582104


a=10
b=10.0
print(a is b)
print(id(a))   
print(id(b))

# IS NOT OPERATOR

a=10
b=10.0
print(a is not b)


# MEMBERSHIP OPERATORS

#IN  AND NOT IN OPERATOR
print(10 in ["10","20","30"])    # the first 10 is integer value the 2nd 10 is a string. in operator perform == operation
print(10 in [10.0,"20","30"])
print(10 in [10.98,"20","30"])
print(10 not in ["10","20","30"])
print(10 not in [10.0,"20","30"])

# bitwise operators

#bitwise AND operator(&)
print(20&48)

#bitwise OR operator(|)
print(90|49)
print(10&5)

#bitwise NOT operator(~)

print(~3)
a=89
print(~a)

#bitwise XOR operation(^)

print(20^30)
print(10^5)
print(78^59)
print(16^13)

#bitwise left shift(<<)
print(20<<2)
print(8<<2)
print(10<<16)

#bitwise right shift(>>)
print(89>>2)

a=10
b=29
if a>b:
    print("A is big")
else:
    print("B is big")



