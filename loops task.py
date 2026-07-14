# num = int(input("Enter a number: "))

# sum_digits = 0

# while num > 0:
#     digit = num % 10
#     sum_digits = sum_digits + digit
#     num = num // 10

# print("Sum of digits:", sum_digits)




# num = int(input("Enter a number: "))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reverse:", reverse)




# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial:", fact)





# s = input("Enter a string or number: ")

# length = len(s)

# if length % 2 == 0:
#     print(s[length//2 - 1:length//2 + 1])
# else:
#     print(s[length//2])




# num = input("Enter a number: ")

# first = int(num[0])
# last = int(num[-1])

# middle_sum = 0

# for digit in num[1:-1]:
#     middle_sum += int(digit)

# if first + last == middle_sum:
#     print("equal")
# else:
#     print("not equal")




# num = input("Enter a number: ")

# first = int(num[0])
# last = int(num[-1])

# flag = True

# for digit in num[1:-1]:
#     if int(digit) >= first or int(digit) >= last:
#         flag = False
#         break

# print(flag)





# s = input("Enter a string: ")

# vowels = ""

# for ch in s:
#     if ch in "AEIOUaeiou":
#         vowels += ch

# print(vowels[::-1])





# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if ch in "AEIOUaeiou" and ch not in result:
#         result += ch

# print(result)




# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if s.count(ch) == 1:
#         result += ch

# print(result)




# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if 'A' <= ch <= 'Z':
#         result += chr(ord(ch) + 32)
#     elif 'a' <= ch <= 'z':
#         result += chr(ord(ch) - 32)
#     else:
#         result += ch

# print(result)





# s = input("Enter a string: ")

# upper = ""
# lower = ""

# for ch in s:
#     if ch.isupper():
#         upper += ch
#     elif ch.islower():
#         lower += ch

# print(upper[::-1] + lower)





# arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# largest = arr[0]

# for num in arr:
#     if num > largest:
#         largest = num

# print("Largest element:", largest)




# arr = list(map(int, input("Enter numbers: ").split()))

# largest = second = float('-inf')

# for num in arr:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num

# print("Second largest:", second)




# arr = list(map(int, input("Enter numbers: ").split()))

# total = 0

# for num in arr:
#     total += num

# print("Sum:", total)




# arr = list(map(int, input("Enter numbers: ").split()))

# result = []

# for num in arr:
#     if num not in result:
#         result.append(num)

# print(result)




# arr = list(map(int, input("Enter numbers: ").split()))

# flag = True

# for i in range(len(arr) - 1):
#     if arr[i] > arr[i + 1]:
#         flag = False
#         break

# if flag:
#     print("True")
# else:
#     print("False")




# arr = list(map(int, input("Enter numbers: ").split()))

# print(arr[::-1])



# arr = [0, 1, False, 2, "", 3]

# result = []

# for i in arr:
#     if i:
#         result.append(i)

# print(result)




# arr = list(map(int, input("Enter numbers: ").split()))

# result = []

# for num in arr:
#     if arr.count(num) == 1:
#         result.append(num)

# print(result)




# arr = list(map(int, input("Enter numbers: ").split()))

# sum_even = 0

# for num in arr:
#     if num % 2 == 0:
#         sum_even += num

# print("Sum of even numbers:", sum_even)





# s = input("Enter a string: ")

# print("Reverse:", s[::-1])




# s = input("Enter a string: ")

# if s == s[::-1]:
#     print("True")
# else:
#     print("False")





# s = input("Enter a string: ")

# count = 0

# for ch in s:
#     if ch in "AEIOUaeiou":
#         count += 1

# print("Number of vowels:", count)






# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if ch not in "AEIOUaeiou":
#         result += ch

# print(result)




# s = input("Enter a string: ")

# print(s.title())




# s = input("Enter a number: ")

# num = int(s)

# print(num)
# print(type(num))




s = input("Enter a string: ")

if s.isdigit():
    print("True")
else:
    print("False")