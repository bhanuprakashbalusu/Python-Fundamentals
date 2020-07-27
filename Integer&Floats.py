# we know integer is a whole number and float is a decimal
# to find the type of num declared below we use type() method
num_1 = 3
print(type(num_1))  # output will be -> class 'int'
num_2 = 3.14
print(type(num_2))  # output will be -> class 'float

# Arithmetic Operators:
# Addition:
print(3 + 2)  # outputs 5
# Subtraction:
print(3 - 2)  # outputs 1
# Multiplication:
print(3 * 2)  # outputs 6
# Division:
print(3 / 2)  # outputs 1.5
# Floor Division:
print(3 // 2)  # outputs 1 as it removes the decimal .5
# Exponent:
print(3 ** 2)  # outputs 9 which is 3 power 2
# Modulus:
print(3 % 2)  # outputs 1 which is the remainder, used to check whether the num is odd
print(2 % 2)  # outputs 0 which is the remainder, used to check whether the num is even

# Order of arithmetic works properly with python
print(3 * 2 + 1)
print(3 * (2 + 1))

# Ways to increment value by 1
num_3 = 1
num_3 = num_3 + 1
print(num_3)  # prints 2
# the above increment operation can be written as
num_3 += 1
print(num_3)  # prints 3
# the above format can be implemented for other operations as well
num_3 *= 10
print(num_3)  # prints 30

# few builtin functions are
# abs() -> gives positive value
print(abs(-3))  # prints 3

# round() -> rounds to the nearest positive integer
print(round(3.75))  # prints 4
print(round(3.75, 1))  # prints 3.8 -> rounds to the first digit after decimal

# Comparison Operators: -> return boolean values True/False
# Equal:
num_4 = 3
num_5 = 2
print(num_4 == num_5)  # prints False
print(num_4 != num_5)  # prints True
print(num_4 > num_5)  # prints True
print(num_4 < num_5)  # prints False
print(num_4 >= num_5)  # prints True
print(num_4 <= num_5)  # prints False

# casting from string to integer
num_6 = '100'
num_7 = '200'
print(num_6 + num_7)  # prints 100200
num_6 = int(num_6)
num_7 = int(num_7)
print(num_6 + num_7)  # prints 300




