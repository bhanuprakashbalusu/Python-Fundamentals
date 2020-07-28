# Looping through list using for loop
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
# prints each number of the list looping through entire list

# Two important keywords while working with the loops are break and continue:
# break keyword will completely break out of the loop
# continue keyword stop the current iteration and move onto the next iteration of the loop
# using break:
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)
# prints 1 2 and Found and break out of the loop continue without printing 3, 4 and 5

# using continue:
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)
# prints 1 2 Found 4 5 without printing 3 by skipping to next iteration on executing continue statement

# Loop within a loop:
for num in nums:
    for letter in 'abc':
        print(num, letter)
# prints each combination of letter with number and move to next number and its combination with letter and so on

# If we want to go through the loop a certain number of times we have built-in function called range()
for i in range(10):
    print(i)
# prints numbers from 0 to 9

# If we want to start range from 1 instead of 0 we can specify 0 until excluded number
for i in range(1, 11):
    print(i)
# prints numbers from 1 to 10 since 11 is not inclusive

# While loops are similar to for loops but while loops keep going until certain condition is met or hit break statement:
x = 0
while x < 10:
    print(x)
    x += 1
# prints 0 to 9 and breaks the loop. If we forgot to increment x by 1 for every iteration loop goes on forever

y = 0
while y < 10:
    if y == 5:
        break
    print(y)
    y += 1
# prints 0 to 4 and breaks the loop.

# If we struck in an infinite loop by any case we must press Ctrl c to come out of it
