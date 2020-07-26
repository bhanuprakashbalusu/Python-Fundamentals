# printing welcome message using print() function
print('Hello World')

# printing welcome message using print() function by passing variable
message = 'Hello World'
print(message)

# if there is single quote in your text you can use double quotes and vice versa
msg_1 = "Bobby's World"
print(msg_1)

# or you can handle with single quote in your text is by using backslash before single quotes
msg_2 = 'Bobby\'s World'
print(msg_2)

multi_line_msg = """Bobby's World was a good cartoon
in the 1990's"""
print(multi_line_msg)

# finding length of the string using len() function
print(len(message))  # we get total length of string 'Hello World' which is  -> 11

# accessing character of the string by passing the location/index in [] next to string variable
print(message[0])  # we get the first character which is -> H
print(message[10])  # we get the last character which is -> d

# we get index error if we access the location of the character that doesn't exist
# print(message[11])  # It will show index error

# we can access range of characters of the string as below
print(message[0:5])  # here first index 0 is inclusive but second index 5 is not. so output will be -> Hello

# if we place nothing in the first index it will assume 0
print(message[:5])  # we get same result as above which is -> Hello

# if we leave second index it will assume end of the ect index
print(message[6:])  # it will print -> World

# let's go through few useful string methods

# for making text to be in all lowercase we use lower() method
print(message.lower())  # we get -> hello world

# for making text to be in all uppercase we use upper() method
print(message.upper())  # we get -> HELLO WORLD

# to find out how many times characters the text are repeated we use count() method which takes
# characters as argument
print(message.count('Hello'))  # output will be -> 1
print(message.count('l'))  # output will be -> 3

# to find index of a characters in the text we use find() method
print(message.find('World'))  # output will be -> 6 since World starts at index 6
print(message.find('Universe'))  # output will be -> -1 since it can't find Universe in the message variable

# in order to replace we use replace() method which takes two arguments
print(message.replace('World', 'Universe'))  # still prints -> Hello World -> since it is not replacing it in the
# original message instead returns the changed value
changed_msg = message.replace('World', 'Universe')
print(changed_msg)  # output will be -> Hello Universe

# in order to change the original message we can use the same variable and assign it to the returned value
message = message.replace('World', 'Universe')  # now the text inside message variable is changed permanently

# to concatenate two strings
greeting = 'Hello'
name = 'Micheal'
my_msg_1 = greeting + name
print(my_msg_1)  # it will print -> HelloMicheal
my_msg_2 = greeting + ', ' + name + '. ' + 'Welcome!'
print(my_msg_2)  # it will print -> Hello, Micheal. Welcome!

# instead of using + it's better to use format() method with placeholders to place the variables
my_msg_3 = '{}, {}. Welcome!'.format(greeting, name)
print(my_msg_3)  # it will print -> Hello, Micheal. Welcome!

# for 3.0 or higher version of python we can use fstrings
my_msg_4 = f'{greeting}, {name}. Welcome!'
print(my_msg_4)  # it will print -> Hello, Micheal. Welcome!

# we can manipulate strings within place holders when we use fstrings
my_msg_5 = f'{greeting}, {name.upper()}. Welcome!'
print(my_msg_5)  # it will print -> Hello, MICHEAL. Welcome!

# to see all the attributes and methods available for strings we can use dir() method and pass the string variable
print(dir(message))

# to see more information about string method we can use help() method passing string itself
print(help(str))  # for all string methods
print(help(str.lower))  # for a particular string method

# string formatting in detail

person = {'name': 'Jenn', 'age': 23}
sentence_1 = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence_1)  # My name is Jenn and I am 23 years old

# we can place values in the placeholders to get the same result as above
sentence_2 = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])

# we can use [] with values inside placeholders to get the same result as above
sentence_3 = 'My name is {0[name]} and I am {0[age]} years old'.format(person)

# accessing values from a list and getting the same result as above
person_1 = ['Jenn', 23]
sentence_4 = 'My name is {0[0]} and I am {0[1]} years old'.format(person_1)

# use of placing 0, 1 etc inside the placeholder is seen clearly in the below example
tag = 'h1'
text = 'This is a headline'
sentence_5 = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence_5)  # it wil print -> <h1>This is a headline</h1>

# accessing values from class variables
class Person():

    def __init__(self, name_1, age_1):
        self.name = name_1
        self.age = age_1


p1 = Person('Jack', '33')
sentence_6 = 'My name is {0.name} and I am {0.age} years old'.format(p1)
print(sentence_6)

# using keyword arguments to get the same result
sentence_7 = 'My name is {name} and I am {age} years old'.format(name='Jenn', age='30')
print(sentence_7)

# using unpacking dictionary to fill in keyword arguments which is a best way to use dictionary values
sentence_8 = 'My name is {name} and I am {age} years old'.format(**person)
print(sentence_8)  # Output will be -> My name is Jenn and I am 23

# zero padding the digits using format() method in placeholders
for i in range(1, 11):
    sentence_9 = 'The value is {:03}'.format(i)
    print(sentence_9)  # prints -> The value is 001, The value is 002 and so on up to The value is 010

# format to do decimal places
pi = 3.14159265
sentence_10 = 'Pi is equal to {:.2f}'.format(pi)
print(sentence_10)
sentence_01 = 'Pi is equal to {:05.2f}'.format(pi)
print(sentence_01)

# printing large numbers with comma separators for being more easily readable
sentence_11 = '1MB is equal to {:,} bytes'.format(1000**2)
print(sentence_11)

# using both decimal and comma separators
sentence_12 = '1MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence_12)

# formatting and printing out dates
import datetime
my_date = datetime.datetime(2020, 7, 26, 7, 21, 30)
print(my_date)

# formatting as July 26, 2020
sentence_13 = '{:%B %d, %Y}'.format(my_date)
print(sentence_13)

# formatting as July 26, 2020 fell on a Sunday and was the 208th day of the year
sentence_14 = '{0:%B %d, %Y} fell on {0:%A} and was the {0:%j}th day of the year'.format(my_date)
print(sentence_14)
