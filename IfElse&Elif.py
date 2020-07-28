# Depending on certain values evaluate to true or false we can can control what statement gets executed
if True:
    print('Conditional was true')  # prints -> Conditional was true

if False:
    print('Conditional was true')  # doesnot print anything since boolean is False in condition

# we generally do comparison using comparison operators which gives boolean values True or False
language = 'Python'
if language == 'Python':
    print('Language is Python')
else:
    print('No Match')
# output will be -> Language is Python

# to check multiple conditionals we use elif
language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'JavaScript':
    print('Language is JavaScript')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')
# output will be -> Language is Java

# In addition to comparison operators we have boolean operations which are -> and, or, not
user_1 = 'Admin'
logged_in = True
if user_1 == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad credentials')
# output will be -> Admin Page -> since both conditions are true

user_2 = 'Admin'
logged_in = False
if user_2 == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad credentials')
# output will be -> Bad credentials -> since only one condition is true

user_3 = 'Admin'
logged_in = False
if user_3 == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad credentials')
# output will be -> Admin Page -> since any one condition can be true for or

# not operator is used to switch the boolean that is True to False and False to True
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
# outputs -> Please Log In -> since logged_in is False so not logged_in is True

# Difference between == operator and is operator:
# == operator compares the values
# is operator compares the objects inside the memory
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # prints -> True -> since it compares the values of a and b
print(a is b)  # prints -> False -> since it compares the id(a) and id(b)
print(id(a))
print(id(b))
# if we run we can observe both have different ids for a and b in memory

c = [4, 5, 6]
d = c
print(c == d)  # prints -> True
print(id(c))
print(id(d))
print(c is d)  # prints -> True -> since both c and d have same ids in memory -> it is same as print statement below
print(id(c) == id(d))  # prints -> True

# Following are the values evaluated by python as False everything else are evaluated as True:
# False
condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# prints -> Evaluated to False

# None
condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# prints -> Evaluated to False

# Zero of any numeric type
condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# prints -> Evaluated to False

# Any empty sequence. For example, '', (), []
condition = []
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# prints -> Evaluated to False

# Any empty mapping. For example, {}.
condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# prints -> Evaluated to False
