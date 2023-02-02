# x= 1 # int
# y= 2.3 # float
# name= 'Tunde Adegoke' #string
# is_cool= True  #boolean or bool

# multiple assignment
# x, y, name, is_cool =(10, 20.5, 'Adegoke', False)

# basic math for the above multiple assignment

# print(x + y)
# casting
# x=str(x)
# y=int(y)
# z=float(y)
# print(type(z), y)

# print(is_cool)


#string
name='Naski'
age=10

# concatination
# print('my name is ' + name + ' and age is ' + str(age))
# print('my name is {name} and age is {age}'.format(name=name, age=age))
# print(f'Hello my name is {name} and age is {age}')


name2='adegoke babatunde'
# print(name2[1:6:2])
# print(name2.capitalize())
# print(name2.upper())
# print(name2.lower())
# sub= 'a'
# print(name2.count('a'))
# print(name2.count(name2))
# print(name2.startswith('babatunde'))
# print(name2.endswith('babatunde'))
# print(name2.split())
# newName=name2.split(' ')
# newName.reverse()
# print(newName)
# print(name2.isalnum())
# print(name2.isalpha())
# print(name2.isnumeric())

# print(name2.find(''))

# print(len(name2))

# my_list = [1,2,3,1,1,3,2,3,1,2,3,1,2,3,1]
# num1 = {1,2,3, 4}
# num2 = {3,4,5}
# print(set(my_list))
# print(num1.union(num2))
# print(num1.intersection(num2))




# list

# colors= ['red', 'green', 'yellow', 'blue', 'pink']
# colors[1]='blueberries'
# print(colors)
# print(colors[1])
# print(len(colors))
# print(colors.index('green'))
# colors.append('brown')
# print(colors)
# colors.remove('yellow')
# print(colors)
# colors.insert(2, 'strawberry')
# print(colors)
# colors.pop(2)
# print(colors)
# colors.reverse()
# print(colors)
# colors.sort()
# print(colors)
# colors.sort(reverse=True)
# print(colors)


#tuple

# tuple is not changeable

# fruits =('apple', 'orange', 'mango', 'grapes')

# fruits2=tuple(('apple', 'orange', 'mango', 'grapes'))
# fruit2=('papaya',)

# print(type(fruit2))
# del fruits
# set

# fruits_set={'grapes', 'orange', 'mango', 'grapes', 'orange'}

# print('mango' in fruits_set)
# fruits_set.add('papaya')
# print(fruits_set)
# print('papaya' in fruits_set)
# fruits_set.remove('papaya')
# print(fruits_set)
# fruits_set.clear()
# print(fruits_set)

# del fruits_set
# print(fruits_set)




# dictionary

person={
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
# person2=dict(first_name='Titi', last_name='Jojoge',)

# print(type(person))
# print(person['first_name'])
# print(person.get('last_name'))
person['phone']= '08165717300'
# print(person)
# print(person.keys())
# print(person.items())

# person2=person.copy()
# person2['city']= 'Lagos'
# print(person2)

# del person['age']
# print(person)

# person.pop('first_name')
# print(person)

# person.clear()
# print(person)

# print(len(person))

# list dict

# people =[
#     {'name':'tunde', 'age':10, 'gender': 'male'},
#     {'name':'shope', 'age':12, 'gender': 'female'},
#     {'name':'Olukunbi', 'age':20, 'gender': 'bisextual'}
# ]
# print(people[0])


# functions

# def welcome():
#     print('today is monday')
# welcome()

# def greeting(name='Olu'):
#     print(f'{name} Hello world!')
# greeting()

# def greet(x, y):
#     return f'Mr {x} good {y}'
# print(greet('shola', 'morning'))

# def get_sum(x, y):
#     return x + y
# print(get_sum(10, 5))


# lamda function
# get_sum= lambda num1,num2: num1 + num2
# print(get_sum(10,5))












