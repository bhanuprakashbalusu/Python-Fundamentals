import my_module  # we can directly import this my_module since it is in the same directory as this file. It runs
# all of the code present in my_module when we import.

# Standard Library Modules:
import sys
import random
import math
import datetime
import calendar
import os

# we can write import statement in multiple different ways:
# import my_module as mm -> and call find_index function using mm.find_index

# we can import the function itself as below
# from my_module import find_index -> and call it directly as find_index()
# in this approach we can only access find_index function
# if we want to import test variable also we can write as below
# from my_module import find_index, test
# now we can access both find_index function and test variable

# If we want to import everything from my_module we write as below
# from my_module import * -> But this way of importing is not recommended

# we can call find_index function present in my_module from this file using my_module.find_index() and pass arguments
courses = ['History', 'Math', 'Physics', 'CompSci']
index = my_module.find_index(courses, 'Math')  # calls function find_index present in my_module
print('index')  # prints index -> 1

# to see where the program is looking for when it executes import my_module we use sys.path
print(sys.path)  # it prints different paths it looks at while executing import my_module statement

# directories that are added in sys.path are first the current file directory importing module, directories
# containing python path environment variable, then standard library directories because of which we can import
# standard library modules and lastly it looks at the site-packages directory for third party packages

# using random standard library module to get random value
random_course = random.choice(courses)
print(random_course)  # if we run multiple times we get different value of courses list each time

# using math module to convert degrees to radians
rads = math.radians(90)
print(rads)  # prints -> 1.5707963267948966
print(math.sin(rads))  # prints -> 1.0

# datetime module allow us to work with dates and time
today = datetime.date.today()
print(today)

# with calendar module we can find out whether 2020 is a leap year
print(calendar.isleap(2020))

# os module gives us access to underlying operating system
print(os.getcwd())  # prints current working directory where the script is located
print(os.__file__)  # prints the location of os.py in the system

# we can explore entire standard library modules in python38 directory and explore the code of different
# functions provided in those modules
