#Create a list of 5 fruits and print each fruit on a new line using a for loops
fruits = ['Apples', 'Cherry', 'Mangoes', 'Grapes', 'Pineapples']
for fruit in fruits:
     print(fruit) 

# Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = []
for i in range(len(list1)):

  combined.append(list1[i])
combined.append(list2[i])
print(combined)

# Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without using the max() function.
# List of numbers
numbers = [3, 1, 4, 1, 5, 9, 2]

largest = second_largest = float('-inf')  

for num in numbers:
    if num > largest:
        second_largest = largest 
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("The two largest numbers are:", largest, "and", second_largest)
