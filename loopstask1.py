# Sum of Digits
number=int(input())

digit_sum=0
while number:
    digit_sum+=number%10
    number//=10
print(digit_sum)
# Middle Character(s) of String/Number
number=int(input())
reverse=0
while number:
    reverse=reverse*10+number%10
    number//=10
print(reverse)
# Sum of Middle Digits == First + Last
number=int(input())
factorial=1
for value in range(2,number+1):
    factorial*=value
print(factorial)
# Middle Digits Less Than First and Last
text=input()
length=len(text)
if length%2:
    print(text[length//2])
else:
    print(text[length//2-1:length//2+1])
# Reverse Order of Vowels
text=input()
print("".join(character for character in text if character.lower() in "aeiou")[::-1])

# Print Unique Vowels Only
text=input()
result=""
for character in text:
    if character.lower() in "aeiou" and character not in result:
        result+=character
print(result)
# Remove Duplicate Characters
text=input()
print("".join(character for character in text if text.count(character)==1))
# Change Uppercase to Lowercase and Vice Versa
text=input()
print(text.swapcase())
# Print Uppercase Letters in Reverse Order Followed by Lowercase Letters
text=input()
print("".join(character for character in text if character.isupper())[::-1]+"".join(character for character in text if character.islower()))
# Find the Largest Element in an Array
numbers=list(map(int,input().split()))
print(max(numbers))

# Find the Second Largest Element
numbers=list(map(int,input().split()))
print(sorted(set(numbers))[-2])

# Sum of All Elements
numbers=list(map(int,input().split()))
print(sum(numbers))
# Remove Duplicates from an Array
numbers=list(map(int,input().split()))
result=[]
for number in numbers:
    if number not in result:
        result.append(number)
print(result)

# Check if Array is Sorted
numbers=list(map(int,input().split()))
print(numbers==sorted(numbers))
# Reverse an Array
numbers=list(map(int,input().split()))
print(numbers[::-1])
# Remove Falsy Values
values=eval(input())
print([value for value in values if value])
# Find Unique Elements
numbers=list(map(int,input().split()))
print([number for number in numbers if numbers.count(number)==1])
# Sum of Even Numbers
numbers=list(map(int,input().split()))
print(sum(number for number in numbers if number%2==0))
# Reverse a String
text=input()
print(text[::-1])
# Check if a String is a Palindrome
text=input()
print(text==text[::-1])
# Count Vowels in a String
text=input()
print(sum(character.lower() in "aeiou" for character in text))
# Remove Vowels from a String
text=input()
print("".join(character for character in text if character.lower() not in "aeiou"))
# Convert String to Title Case
text=input()
print(text.title())
# Convert String to Number
text=input()
number=0
for character in text:
    number=number*10+ord(character)-48
print(number)
# Check if String Contains Only Digits
text=input()
print(text.isdigit())
# Count Occurrences of a Character
text=input()
character=input()
print(text.count(character))
# Convert Array to Object
pairs=eval(input())
print(dict(pairs))
# Merge Two Objects
first_object=eval(input())
second_object=eval(input())
print(first_object|second_object)
# Count Object Properties
dictionary=eval(input())
print(len(dictionary))
# Get Object Keys
dictionary=eval(input())
print(list(dictionary.keys()))
# Get Object Values
dictionary=eval(input())
print(list(dictionary.values()))
# Check if Object is Empty
dictionary=eval(input())
print(len(dictionary)==0)

