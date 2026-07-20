Create a list of 5 integers and print it.
Write a program to find the length of a list without using len().
Access and print the last element of a list.
Add an element to the end of a list.
Insert an element at the 2nd position in a list.


l=[1,2,3,4,5]
print(l)
print(type(l))


l=[10,20,30,40,50]
print(l)
print(len(l))

l=[10,20,30,40,50,60]
print(l[-1])

numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)


numbers = [10, 20, 30, 40, 50]
numbers.insert(1, 15)
print(numbers)


numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)

numbers = [10, 20, 30, 40, 50]
numbers.pop(3)
print(numbers)


numbers = [10, 20, 10, 30, 10, 40]
count = numbers.count(10)
print(count)


numbers = [50, 20, 10, 40, 30]
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)


numbers = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])
print(reversed_list)


numbers = [10, 50, 20, 5, 40]
maximum = numbers[0]
minimum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number
print("Maximum:", maximum)
print("Minimum:", minimum)


list1 = [10, 20, 30]
list2 = [40, 50, 60]
merged_list = list1 + list2
print(merged_list)


numbers = [10, 20, 10, 30, 20, 40, 30]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)



numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total = total + number
print("Sum:", total)


even_numbers = [number for number in range(1, 51) if number % 2 == 0]
print(even_numbers)


numbers = [1, 2, 3, 4, 5]
k = 2
k = k % len(numbers)
rotated_list = numbers[-k:] + numbers[:-k]
print(rotated_list)


numbers = [10, 50, 20, 40, 30]

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("Second largest:", second_largest)



numbers = [1, 2, 3, 2, 1]

if numbers == numbers[::-1]:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")



nested_list = [[1, 2], [3, 4], [5]]
flat_list = []
for sublist in nested_list:
    for number in sublist:
        flat_list.append(number)

print(flat_list)



numbers = [1, 2, 2, 3, 1, 2, 4, 3]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1
print(frequency)