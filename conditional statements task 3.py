# Positive, Negative, or Zero
# Input a number.
# Print whether it is positive, negative, or zero.

# numb=int(input("enter a number: "))
# if numb<0:
#     print("number is positive")
# elif numb>0:
#     print("number is negetive")
# else:
#     print("print number is zero")

# Even or Odd
# Input an integer.
# Print whether it is even or odd.

# numb=int(input("enter a number: "))
# if numb%2==0:
#     print("number is even")
# else :
#     print("number is odd")

# Eligible to Vote
# Input a person's age.
# If the age is 18 or above, print "Eligible to vote", otherwise print "Not eligible".

# age=int(input("enter age: "))
# if age>=18:
#     print("eligible for vote")
# else:
#     print("not eligible")

# Greatest of Two Numbers
# Input two numbers.
# Print the greater number.

# num1=int(input("enter a number: "))
# num2=int(input("enter number: "))
# if num1>num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater")

# Greatest of Three Numbers
# Input three numbers.
# Print the greatest one.

# num1=int(input("enter num1: "))
# num2=int(input("enter num2: "))
# num3=int(input("enter num1: "))
# if num1>num2 and num1>num3:
#     print ("num1 is greater")
# elif num2>num1 and num2>num3:
#     print("num2 is greater")
# else:
#     print("num3 is greater")

# Leap Year Checker
# Input a year.
# Print whether it is a leap year.

# year=int(input(" enter year: "))
# if year%400==0:
#     print("it is leap year")
# else:
#     print("non leap year")

# Grade Calculator
# Input marks (0–100).
# Display the grade:

# marks=int(input("enter marks: "))
# if marks>=85:
#     print(" grade A")
# elif marks>=75:
#     print("grade B")
# elif marks>=65:
#     print("grade C")
# elif marks>=55:
#     print("grade D")
# elif marks>=45:
#     print("grade E")
# else: 
#     print("fail")


# Character Type
# Input a single character.
# Print whether it is:
# Uppercase letter
# Lowercase letter
# Digit
# Special character

# alpha=input("enter a charecter: ")
# if 'A' <= alpha <= 'Z':
#     print("letter is in uppercase")
# elif  'a'  <= alpha <='z':
#     print("letter is in lower case")
# elif '0' <= alpha <= '9':
#     print("letter is in digit")
# else:
#     print("special charecter")

# Largest Among Four Numbers
# Input four numbers.
# Print the largest.

# a=int(input("enter value: "))
# b=int(input("enter value: "))
# c=int(input("enter value: "))
# d=int(input("enter value: "))
# if a>b and a>c and a>d:
#     print("a is largest")
# elif b>a and b>c and b>d:
#     print("b is greater")
# elif c>a and c>b and c>d:
#     print("c is greater")
# else:
#     print("d is greater")

# Divisibility Check
# Input a number.
# Check if it is divisible by both 3 and 5.

# num=int(input("enter value: "))
# if num%3 and num%5:
#     print("divisible by 3 and 5")
# else:
#     print("not divisible")

# Calculator
# Input two numbers and an operator (+, -, *, /).
# Perform the operation using if-elif-else.

# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# o=input("enter operator: ")
# if o=="+":
#     print(a+b)
# elif o=="-":
#     print(a-b)
# elif o=="*":
#     print(a*b)
# else: 
#     print(a/b)

# Triangle Validity
# Input three angles.
# Check whether they can form a triangle.

# a=int(input("enter a value: "))
# b=int(input("enter a value: "))
# c=int(input("enter a value: "))
# if a==b==c:
#     print("it is a traingle")
# else:
#     print("not a traingle")

# Triangle Type
# Input three sides.
# Print whether the triangle is:
# Equilateral
# Isosceles
# Scalene

# a=int(input("enter a value: "))
# b=int(input("enter a value: "))
# c=int(input("enter a value: "))
# if a==b==c:
#     print("equilatral")
# elif a==b or a==c or b==c:
#     print("isosceles")
# else:
#     print("scalene")

# Input units consumed.
# Calculate the bill:
# First 100 units → ₹5/unit
# Next 100 units → ₹7/unit
# Above 200 units → ₹10/unit

# units=int(input("enter units"))
# if units<=100:
#     bill=units*5
# elif units>100:
#     bill=units*7
# else: 
#     bill=units*10

# Find the Smallest of Three Numbers
# a=int(input("enter numb: "))
# b=int(input("enter numb: "))
# c=int(input("enter numb: "))
# if a<b and a<c:
#     print("a is smallest")
# elif b<a and b<c:
#     print("b is smallest")
# else:
#     print("c is smallest")

# Check Whether a Character is a Vowel or Consonant
# charecter=input("enter a charecter: ")
# if charecter=='A' or "E" or "I" or "O" or "U" or "a" or 'e' or 'i' 'o' or 'u':
#     print("vowel")
# else:
#     print("consonent")

# Check Whether a Number is a 2-Digit, 3-Digit, or More

# a=int(input("enter a num: "))
# if a>10 and a<100:
#     print("2 digit num")
# elif a<100 and a>999:
#     print("3 digit num")
# elif a<10:
#     print("1 digit num")
# else:
#     print("out of range")

# Admission Eligibility
# A student is eligible if:
# Marks ≥ 60
# Attendance ≥ 75%
# Print whether the student is eligible.

marks=int(input("enter marks: "))
attendence=int(input("enter attendence: "))
if marks>=60 and attendence>=75:
    print("student is eligible")
else:
    print("not eligible")

# Discount Calculator
# Input purchase amount.
# Apply discount:
# Above ₹5000 → 20%
# ₹2000–₹5000 → 10%
# Below ₹2000 → No discount

amount=int(input("enter amount: "))
if amount>=5000:
    dis=(amount/100)*20
    print(dis)
elif amount>=2000 and amount<5000:
    dis=(amount/100)*10
    print(dis)
else:
    print("no discount")




















