# Lists and Tuples allows us to work with sequential data. Sets are unordered collection of values with no duplicates

# Lists:

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)  # prints entire list

# for length of the list we use len()
print(len(courses))  # prints 4

# to access the list items we use [] after list variable and pass in the index of the value we want
print(courses[0])  # gets the first item of the list -> History
print(courses[3])  # gets the last item of the list -> CompSci

# we can also use negative indexes with last item starting with -1
print(courses[-1])  # gets the last item of the list -> CompSci

# we get index error if we try access the item which is not present in the list
# print(courses[4])  # gives list index out of range error

# to access the range of values of the list in [] we pass included index : not included index
print(courses[0:2])  # gets included index value until before not included index value -> ['History', 'Math']

# we get the same above result even if we not mention starting index since it is index 0
print(courses[:2])  # gets -> ['History', 'Math']

# we need not mention ending index if we want to get the values till the end of the index
print(courses[2:])  # gets -> ['Physics', 'CompSci']

# to add item to the end of the list we use append() method passing item as argument
courses.append('Art')
print(courses)  # prints entire list with Art appended at the end

# to add item at a specific location we use insert() method passing index and item as arguments
courses.insert(0, 'Economics')  # prints entire list with Economics inserted at the beginning

# to add multiple items or list of items to another list we use extend() method that takes one argument
courses_1 = ['Education', 'Philosophy']
courses.extend(courses_1)
print(courses) # prints a list with Education and Philosophy appending each item at the end

# to remove the last value from the list by default we use pop() method
popped_item = courses.pop()
print(courses)  # prints list by removing Art
print(popped_item)  # prints removed item -> Art

# to remove any item from the list we use remove() method passing item tobe removed as argument
courses.remove('CompSci')
print(courses)  # prints the list without CompSci

# Sorting the list using different methods:
# to reverse the list we use reverse() method
courses.reverse()
print(courses)  # prints the list in reverse order with last item at first till first item at last

# to sort the list in alphabetical order or numbers list in ascending order we use sort() method
courses.sort()
print(courses)  # prints the list in alphabetical order
nums_1 = [1, 5, 2, 4, 3]
nums_1.sort()
print(nums_1)  # prints the numbers list in ascending order

# to sort in reverse order we pass reverse=True in sort() method
courses.sort(reverse=True)
print(courses)  # prints in reverse alphabetical order
nums_1.sort(reverse=True)
print(nums_1)  # prints in descending order

# to get sorted list without altering the original list we use sorted() in-built function
sorted_courses = sorted(courses)
print(courses)  # it will not print the sorted list since courses list is not altered
print(sorted_courses)  # prints the sorted version of the courses list

# using min(), max() and sum() to get minimum, maximum and sum of the numbers in the list
print(min(nums_1))  # prints minimum value which is -> 1
print(max(nums_1))  # prints maximum value which is -> 5
print(sum(nums_1))  # prints sum of all the values in the list -> 15

# to find the index of certain value we can use index() method passing value as argument
print(courses.index('Physics'))  # prints 0

# if we search for the value that is not present in the list we get value error
# print(courses.index('Philosophy))  # we get ValueError saying Philosophy is not in the list

# to check whether value/item is present in the list or not we use below procedure
print('Philosophy' in courses)  # it prints -> False -> since Philosophy is not there in the courses list
print('Math' in courses)  # it prints -> True -> since Math is there in the courses list

# to loop through each value in the list we use for loop as below which prints each item of courses in a new line
for item in courses:
    print(item)  # we can use any variable in place of item

# to access the index and the value of each item of the list we use enumerate() method as below
# it prints the index starting with 0 and corresponding value in each line
for index, course in enumerate(courses):
    print(index, course)

# to start the index with 1 we can mention as below
for index, course in enumerate(courses, start=1):
    print(index, course)

# to convert list of values into string separated by , we use join() method by passing list as argument
course_str = ', '.join(courses)  # in place of , we can use any separator
print(course_str)  # prints -> Physics, Math, History, Education, Economics, Art

# to convert string back into list we use split() method by passing separator as argument
new_courses_list = course_str.split(', ')
print(new_courses_list)


# Tuples:
# Tuples are very similar to lists but with one major difference that is we can't modify tuples hence they are immutable
# below is the example for mutable objects which are lists
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)  # both print same values
list_1[0] = 'Art'
print(list_1)  # prints the list with changed value
print(list_2)  # also prints the list with changed value since lists are mutable

# below is the example for immutable objects which are tuple
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)  # both print same values
# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)  # we get TypeError saying tuple does not support item assignment since it is immutable

# accessing and looping through the values of tuple is same as that of list


# Sets:
# Sets are values that are unordered and also have no duplicates.
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)  # prints values that may or may not be in order and order changes with each execution

# sets are mainly used to get rid of duplicates
cs_courses_1 = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses_1)  # prints the values without duplicates

# the other main use is to test whether a value is part of the set or not
print('Math' in cs_courses)  # prints True -> we can do this with lists and tuples also but sets are optimised for this

# to see what values are in common between two sets intersection() method
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))  # prints -> ['History', 'Math']

# to see values that are not in common compared to other we use difference() method
print(cs_courses.difference(art_courses))  # prints -> ['Physics', 'CompSci']

# to combine all the courses in both the sets we use union() method
print(cs_courses.union(art_courses))  # prints all the course in both sets without duplicates


# Creating empty lists, tuples and sets:
# Empty lists:
empty_list_1 = []
empty_list_2 = list()

# Empty tuples:
empty_tuple_1 = ()
empty_tuple_2 = tuple()

# Empty lists:
# empty_set_1 = {}  # This is not an empty set. It's an empty dictionary
empty_set_2 = list()
