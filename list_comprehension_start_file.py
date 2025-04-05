'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

#There are 3 parts to list comprehension:
#*result*  = [*transform/expression*    *iteration*         *filter*/*condition*     ]         You don't necessarily need commas between the items. Just a space is fine.
#                                       #for x in list_1          if x> 7

#The filter part answers the question if the item should be transformed.

# Order of list sytax execution****
#ITERATION FIRST
#CONDITION SECOND
#EXPRESSION LAST

#Create a list of numbers between 1 and 10 using LIST COMPREHENSION
x = [i for i in range(1,11)]
print(x)

#add an expression to the above 
squares = [i**2 for i in range(1,11)]
print(squares)

list1 = [3,4,5]
multiplied = [item*3 for item in list1] #Iterator is ITEM --> naming MUST be consistent
print(multiplied)

#Working with strings
listofwords = ['this', 'is', 'a', 'list', 'of', 'words']
output = [word[0].upper() for word in listofwords]  #APPLY INDEX VALUES FOR getting the SPECIFIC LETTERS OF WORDS.  APPLY .upper() in Transform/Expression
print(output)

# Add in an IF condition.             ****Iteration is MANDATORY. Expression and Condition OPTIONAL****
# Find the square of all even numbers from 1-20
result = [i*i for i in range(1,21) if i % 2 == 0]  # i % 2 checks remainders of numbers. If remainder = 0, number is even, and you know the rest
print(result)


# Practice List comprehension
string = 'Hello 12345 World'
# Use list Comp to EXTRACT THE NUMBERS ONLY - [1,2,3,4,5]
numbers = [int(num) for num in string if num.isdigit()]  # Convert item types in EXPRESSION. 
print(numbers)
# Extract letters only - ['h', 'e']
letters = [str(letter) for letter in string if letter.isalpha()]  
print(letters)
# Extract whole words only - ['Hello', 'World']
words = [word for word in string.split() if word.isalpha()]   # Use SPLIT function in ITERATION. Iteration splits up string first, then condition applies.
print(words)


# Look for and extract text from a file
infile = open('test.txt', 'r')
result = [i.rstrip() for i in infile if 'line3' in i] #Directly apply infile. 
print(result) 


# We can use list comp with a function
def double(x): 
    return x*2

result = [double(x) for x in range(1,11) if x % 2 == 0] 
print(result)


# Work with multiple iterables 
result = [(x,y) for x in [10,30,50] for y in [20,40,60] if x+y > 70] # (x,y) is tuple
print(f"{result}\n")




## Exercise ##                PART OF HW ASSIGNMENT

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

print('Exercises - HW')
newlist = [int(num) for num in numbers if num > 0]
print(f"{newlist}\n")



## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

word_lengths = [len(word) for word in words if word != 'the']
print(f"{word_lengths}\n")


## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

vehicles = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110} # I changed the name of the dictionary to prevent TypeErrors

light_vehicles = [vehicle.upper() for vehicle, weight in vehicles.items() if weight < 5000]
print(f"{light_vehicles}\n")


## Find all the numbers from 1 to 1000 that have a 4 in them
num_with_4 = [num for num in range(1,1001) if '4' in str(num)]
print(f"{num_with_4}\n")


## count how many times the word 'the' appears in the text file - 'sometext.txt'
wanted_word = 'the' #define target word
infile2 = open('sometext.txt', 'r') # open and read text file
words = infile2.read().split() #split file content into words
wanted_word_count = sum([1 for word in words if word.lower() == wanted_word.lower()]) # Count occurrences of a target word
print(f"The word {wanted_word} appears {wanted_word_count} times in the sometext.txt file\n")



## Extract the numbers from the following phrase ##

phrase = 'In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each event, with about 3 or 4 that were classifled as serious per event.'

extract_num = [int(word) for word in phrase.split() if word.isdigit()] 
print(f"{extract_num}\n")



