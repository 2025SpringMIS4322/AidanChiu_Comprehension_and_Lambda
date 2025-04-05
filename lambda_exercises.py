''' 1)
Write a Python program to filter a list of integers using Lambda.

Expected output:
even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]
'''
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print()
even_numbers = list(filter(lambda num: (num % 2 == 0), original_list))
print(f"even_numbers = {even_numbers}")
odd_numbers = list(filter(lambda num: (num % 2 != 0), original_list))
print(f"odd_numbers = {odd_numbers}\n")



''' 2)
Create a list of days that have exactly 6 characters using a lambda function on the list below. 
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


six_char_list = list(filter(lambda x: len(x) == 6, weekdays))
print(f"{six_char_list}\n")



''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

Expected output
['red', 'green', 'blue', 'white']

'''

og_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_from_list = {'orange', 'black'} #TUPLE
reduced_list = list(filter(lambda word: word not in remove_from_list, og_list)) 
print(f"{reduced_list}\n")


''' 4) 
You are given a list of temperatures in Celsius: [0, 12, 34, 25, -5]. Use map() and a lambda function to convert each temperature to Fahrenheit.

Expected output: [32.0, 53.6, 93.2, 77.0, 23.0]

'''

cel = [0, 12, 34, 25, -5]

fah = list(map(lambda celsius: (celsius * 9/5) + 32, cel)) # map() fct --> applies given fct to every item in an iterable (like a list or tuple)
print(f"{fah}\n")                                          # and returns a map() object (typically converted to a list or another iterable type)


''' 5) Use map() with a lambda function to calculate the final price for each item in the cart after applying a 10% discount.
'''

cart = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Phone', 'price': 800},
    {'name': 'Tablet', 'price': 300},
    {'name': 'Monitor', 'price': 150}
]

disc_applied = list(map(lambda item: {'name': item['name'], 'price': round(item['price'] * 0.90, 2)}, cart))
for item in disc_applied:
    print(f"{item['name']} discounted price = ${item['price']:.2f}")
print()




''' 6)
Write a lambda function that takes two arguments x and y and returns:

    "x is greater" if x > y
    "y is greater" if y > x
    "Equal" if x == y

 '''

compare = lambda x,y: 'x is greater' if x > y else 'y is greater' if y > x else 'Equal'

print(compare(5, 3))  # Output: 'x is greater'
print(compare(3, 7))  # Output: 'y is greater'
print(compare(4, 4))  # Output: 'Equal'
print()




''' 7)
Write a lambda function to sort the list by the length of each string.
Expected Output: ['C', 'Java', 'Ruby', 'Python', 'JavaScript']


'''
languages = ['Python', 'Java', 'C', 'Ruby', 'JavaScript']

ascending_lang = sorted(languages, key=lambda asc: len(asc))
print(f"{ascending_lang}\n\n")




''' 8)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
new_tuples = sorted(original_scores, key=lambda x: x[1]) #This structure of Tuples sorts the OG scores list by the 'x' key, which lambda acts on
print(f"{new_tuples}\n\n")                                 #and sorts it ascending by x[1], which refers to tuple's number element at index 1



''' 9)
Given a dictionary of student names and their scores, use a lambda function to increase each score by 5:

Expected output:
curved scores = {'Alice': 90, 'Bob': 92, 'Charlie': 83}

'''

students = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
curved_scores = {student: (lambda score: score + 5)(score) for student, score in students.items()}
print(f"{curved_scores}\n")



#CHALLENGE QUESTION (Not required)!!
''' 10)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
str1 = "HELLO"
str1= "hello"