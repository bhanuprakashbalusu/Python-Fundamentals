# Functions are basically some instructions packaged together to perform specific task and allow us to reuse
# code without repeating.

# we use def keyword to create a function
def hello_func():
    pass  # pass keyword tells that we don't want to do anything now and carry on without throwing any error

hello_func()  # here we are calling the function to execute
print(hello_func)  # prints -> hello_func is function at particular location in memory -> But it do not
# execute function because there is no parenthesis
print(hello_func())  # now it executes the function and prints None since hello_func is not returning anything


def hi_func():
    print("Hi Function!")

hi_func()  # prints -> Hi Function!.


# Functions also allow us to send some data, they operate on data and return the result
def hithere_func():
    return 'HiThere Function!'

hithere_func()  # It does not print anything.
print(hithere_func())  # prints the returned string -> HiThere Function!
print(hithere_func().upper())  # converts the returned string into upper case and prints -> HITHERE FUNCTION!

# passing arguments to a function
def greet_func(greeting):  # here greeting parameter is a required argument since we didnot provide any default value
    return '{} Function!'.format(greeting)

# print(greet_func())  # it gives an error since we are calling function without passing argument
print(greet_func('Hi'))  # prints -> Hi Function!

# passing multiple arguments and providing a default value to one of them
def greeting_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

print(greeting_func('Hi'))  # prints -> Hi, You -> It took the default name value
print(greeting_func('Hi', name='Bhanu'))  # prints -> Hi, Bhanu

# Functions that allow any arbitrary positional and keyword arguments:
def student_info(*args, **kwargs):  # here * represents any number of arguments, args represents positional
    # arguments, kwargs represents key word arguments
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)  # prints positional arguments as tuple ('Math', 'Art') and
# key word arguments as dictionary {'name': 'John', 'age': 22}

# if we pass the arguments as below
courses = ['Science', 'Philosophy']
info = {'name': 'Martin', 'age': 24}

student_info(courses, info)  # prints -> (['Science', 'Philosophy'], {'name': 'Martin', 'age': 24}) and {}
# which is not what we expected instead we need to pass as below so that it unpacks the values

student_info(*courses, **info)  # prints -> ('Science', 'Philosophy') and {'name': 'Martin', 'age': 24}
