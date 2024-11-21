#  Create a dictionary with three key-value pairs representing a student's information: 
# name, age, and grade. Print each key-value pair on a new line.
student_info = {
    'name': 'John Doe',
    'age': 20,
    'grade': 'A'
}
for key, value in student_info.items():
    print(f"{key}: {value}")
# Write a function that takes a dictionary of people's names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.    
def filter_adults(people):
     return [name for name, age in people.items() if age >= 21]

people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
adults = filter_adults(people)
print(adults)
 #Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
def calculate_total_cost(prices, items_bought):
    total_cost = 0 
    for item in items_bought:
        total_cost += prices.get(item, 0)  
    
    return total_cost
prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
items_bought = ['apple', 'orange', 'banana', 'banana']
total_cost = calculate_total_cost(prices, items_bought)
print(f'Total cost: ${total_cost:.2f}')
 #Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count
sentence = "hello world hello"
word_counts = count_word_occurrences(sentence)
print(word_counts)
