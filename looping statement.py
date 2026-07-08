# print numbers 1-100,100-1,even numbers,and odd numbers

# for i in range(1,101,1):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# for i in range(0,101,2):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# Write a program to print numbers from 1 to 10 using a for loop.
# Write a program to print even numbers between 1 and 20.
# Write a program to print odd numbers from 1 to 15.
# Write a program to print the multiplication table of 5.
# Write a program to calculate the sum of numbers from 1 to 100.
# Write a program to print numbers from 10 to 1 in reverse order.
# Write a program to count how many numbers are there from 1 to 50.
# Write a program to print the square of each number from 1 to 10.
# Write a program to print all numbers between 1 and 30 that are divisible by 3.
# Write a program to print the first 10 natural numbers.

for i in range(1,11):
    print(i)

for i in range (0,21,2):
    print(i)

for i in range (1,16,2):
    print(i)

for i in range(1,6,1):
    print(i)
    for j in range(1,11,1):
        print(i,'x',j,'=',i*j)
a=5
for i in range(1,11):
    print(a,'x',i,'=',a*i)

sum=0
for i in range(1,101):
    sum=sum+i
    print(sum)

for i in range(11,0,-1):
    print(i)

a=int(input("enter a value: "))
c=0
for i in range(0,2,1):
    a=a//10
    c=c+1
print(c)



for i in range(1,11):
    print(i**2)

for i in range(1,30,1):
    if i%3==0:
        print(i)

for i in range(1,11,1):
    print(i)



