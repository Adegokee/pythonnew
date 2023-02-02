# software development
# devops automation
# cybersecurity
# data analysis
# artificial intelligence
# robotics
# games


# installation
# introduction
# variables
# data types
# - strings
# - lists
# - dictionary
# - numbers
# - tuple
# - sets
# operators
# control flow
# Loops
# functions
# working with file

# Introduction
# variables - a container for storing information in a computer

x = 5
first_name = 'John'

# rules for naming variables
#1. variable names must NOT contain space between them
#2. You cannot use a reserved words as variable name
#3. variable names are case sensitive
#4. use meaningful words as variable name
#5. variables cannot start with numbers,or symbols except _ eg. 2number = 4 will give error

print(x)
print(first_name)

#data types - the format you can store variables
#string - sequence of characters denoted by '', "", """ """
address ="70c Allen Avenue, Ikeja"
first_name = 'John'

#length of string
print(len(address))

# # indexing - bringing out a character in particular location
print(first_name[3])
print(address[4])
print(address[-1]) #indexing from behind

# slicing - bring out multiple characters in particular location
print(address[10:16])
print(first_name[1:3])
print(first_name[:])
print(first_name[:3])
print(first_name[2:])

numbers = '12345678'
print(numbers[1::2])
print(numbers[-9:-1:2])
print(numbers[::-1])
# string methods
address ="70c Allen Avenue, Ikeja"
print(address.upper())
print(address.count('a'))
print(address.endswith('a'))
print(address.isdigit())
print(address.replace("Ikeja", "Dubai"))
print(address.split())

last_name = "  Wale  "
print(last_name.strip())
print(first_name +"-"+ last_name.strip())

# accepting input from users
# age = input("Enter your age:\n")
# print("Your age is ", age)

# List - storing multiple values in a variable
colors = ["red", "green", "yellow"]

# indexing a list
print(colors[1])

# slicing a list
print(colors[1:3])

# list methods
colors.append("orange") # add new item
print(colors)
colors.pop() # remove an item
print(colors)
colors.pop(1) # remove item in particular index position
print(colors)

colors.insert(0,"black")
print(colors)

colors.remove("red")
print(colors)

colors.extend(numbers)
print(colors)

new_colors = colors.copy()
print(new_colors)

colors.sort()
print(colors)

colors.reverse()
print(colors)
print(colors[::-1])
print("".join(colors))

# Dictionary - storing key value pair
# greatness- to be powerful

staff = { 
    "gender": "Female",
    "age": 20,
    "location": {
        "state":"Lagos", 
        "country":"Nigeria"
        }
    }

print(staff["age"])
print(staff["location"]["country"])

print(staff.keys())
print(staff.values())
print(staff.items())
print(staff.get("age"))

staff["continent"] = "Africa"
print(staff)
staff["age"] = 18
print(staff)

age = 10
print(age - 2)

staff.update({"age": 10})
staff.update({"test": 10})
print(staff)

employee = [{"name": "wale", "gender":"male"},
{"name": "Mary", "gender":"female"},
{"name": "Paul", "gender":"male"}]

# python Assignment

# 1. Bring out "python" from the code below
greeting = "Welcome to python"
print(greeting[-6:])

# 2.  Create 2 variables. one for storing your name and the
# other for storing your age. print it out to say eg. My
# name is wale. I am 18 years old. Where wale is your
# name. NB: You can use any number to represent your age
first_name = "Wale"
age = 18
print("My name is " , first_name, "I am", age, "years old")

# 3. Save the first_name and last_name in a variable called
# full_name and print it in the terminal with space in
# between them
first_name = "Wale"
last_name = "Olajumoke"
full_name = first_name + " " + last_name
print(full_name)

# 4. 
words = "I am here"
# print out the word in reverse to read "here am I"
words = words.split()
words.reverse()
print(" ".join(words))

# 5. Bring out only the digits in the data below
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
# Eg. 12345678
print(data[::5])

# 6. print out tech365 from the record below
record = {'k1':[{'nest_key':['this is deep',['tech365']]}]}
print(record['k1'][0]['nest_key'][1][0])

# 7. bring out python from the info below
info = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['python']]}]}]}
print(info["k1"][2]['k2'][1]['tough'][2][0])

#number
age = 18
salary = 5000.90

print(salary.__floor__())
print(salary.__ceil__())

#set - to store unique values
numbers = {1,2,3,1,1,3,2,3,1,2,3,1,2,3,1}
names = {"wale", "wale", "wale", "wale", "wale", "wale"}
print(numbers)
print(names)

my_list = [1,2,3,1,1,3,2,3,1,2,3,1,2,3,1]
num1 = {1,2,3}
num2 = {3,4,5}

print(set(my_list))
print(num1.union(num2))
print(num1.intersection(num2))

#tuple - storing values that are immutable (does not change)
days_of_the_week = (1,2,3,4,5,6,7)
print(days_of_the_week.index(4))

# operators - symbols for performing aoperations eg. arithmentic, comparison, logical
x = 5
y = 3
#arithmetic operations
print(x+ y)
print(x- y)
print(x/ y)
print(x* y)
print(x// y)
print(x% y) # modulo
print(x** y)

#comparison operations - comparing 2 or more values

a = 7
b = 2
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# logical operations
x = 5
y = 4
print(x > y and y < 2)
print(x > y or y < 2)
print(not(x > y and y < 2))

# control flow - it is for putting condition in your code
# age = int(input("Enter your age: "))
# if age > 18:
#     print("You can vote")
# else:
#     print("Not eligible")


# num = int(input("enter a number"))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")

# else:
#     print("zero")

# Loops - repeating a task until certain condition is met

#while loop
# x = 1 # initialization
# while x <= 50: # condition
#     print(x) # task
#     x = x + 1 # increment

# 2 x 1 = 2
# ...
# 2 x 12 = 24

# x = 1
# while x <= 12:
#     print("2 x", x, "=", 2 *x)
#     x = x + 1 

# for loop
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in numbers:
#     print(i)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# range
print(range(10))
print(list(range(10)))

for i in range(11):
    print(i)

# Function - for prevention of repeating code

def test():
    print("Good morning")

test()
test()

# function parameter
def add_two_numbers(x,y):
    print(x + y)

# add_two_numbers(2,3)
# add_two_numbers(7,8)
# add_two_numbers(10,11)

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
add_two_numbers(num1,num2)

from sample import  multiply_it
multiply_it(8,8)