# Dictionaries allow us to work with key-value pairs where key is the unique identifier of data and value is the data
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)  # prints student dictionary keys and values

# to get value of one key we use [] after the dictionary variable and specify the key in it
print(student['courses'])  # prints the list of courses

# we can use integers as data types of keys
student_1 = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student_1[1])  # prints -> John

# if we try to access the key which is not present in dictionary we get key error
# print(student['phone'])  # we get key error

# we can use get method to access the values of a key
print(student.get('name'))  # prints -> John

# if we try to access the key which is not present in dictionary using get method we get None instead of error
print(student.get('phone'))  # prints -> None

# we can also pass default value as second argument to get method if key is not present as below
print(student.get('phone', 'Not Found'))  # prints -> Not Found

# we can add a new entry to the dictionary as below
student['phone_num'] = '555-5555'

# we can also update the existing entry as below
student['name'] = 'Rocky'
print(student)  # prints the updated values

# to update multiple entries on to the dictionary we use update method and pass the dictionary of entries
student.update({'name': 'Bobby', 'age': 30, 'phone_num': '555-6666'})
print(student)  # prints the updated dictionary

# to delete the existing key-value we can use del keyword
del student['phone_num']
print(student)  # prints the dictionary after deleting age key and its value

# we can also delete the key-value using pop method and it returns the deleted value
age = student.pop('age')
print(age)  # prints removed value -> 30

# Looping through all the keys and values of dictionary
# to see how many keys we have in our dictionary we can use len() built-in function
print(len(student_1))  # prints -> 3

# to see all the keys we use keys() method
print(student_1.keys())  # prints all the keys of dictionary

# to see all the values we use values() method
print(student_1.values())  # prints all the values of dictionary

# to print the list of key-value pairs we use items() method
print(student_1.items())  # prints list of key-value pairs

# if we loop through normally like that of list it will only loop through all keys get keys
for key in student_1:
    print(key)

# so we need to use items method while looping through dictionary to access both key and value
for key, value in student_1.items():
    print(key, value)
