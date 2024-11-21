# Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.
for num in range(2, 21,2):
        print(num)        

# Use a while loop to ask the user to input a number until they provide a number greater than 10.    
number = int(input(f"Please enter a number: "))
while number <= 10:
    number = int(input("The number is not greater than 10. Please enter a number greater than 10: "))

print("Thank you! You entered a number greater than 10:", number)
#Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.
for i in range(1, 6):
    print(f"Multiplication table for {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    
#Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.
numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0
for number in numbers:
    if number % 2 != 0: 
        print(number)
        odd_sum += number
print("Sum of all odd numbers:", odd_sum)

 
