# Let's explore how to interact with file objects

# to get a file object we can use built-in open command
f = open('test.txt', 'r')  # if the file is not in the current directory we need to pass exact path
# if we don't mention the mode of the file then it will open the file in read mode 'r' by default

print(f.name)  # prints -> test.txt
print(f.mode)  # prints -> r

f.close()  # once the file is open using above process we need to explicitly close the file using close() method

# Recommended way of opening a file is by using context manager which uses with keyword. This will automatically
# closes the file. We need work with the file within this context manager. We cannot access the file outside
# this context manager.
with open('test.txt', 'r') as f:
    f_contents = f.read()  # this will load all the contents of the file into the memory
    print(f_contents)

    f.seek(0)  # it repositions the current position back to the beginning of the file
    f_contents_1 = f.readlines()  # reads all the lines of the file
    print(f_contents_1)  # prints the list of all lines in the file

    f.seek(0)
    f_contents_2 = f.readline()  # reads the first line of the file from the current position
    print(f_contents_2, end='')  # prints the first line of the file from the current position
    f_contents_2 = f.readline()  # reads the first line of the file from the current position
    print(f_contents_2)  # prints the first line of the file from the current position

    f.seek(0)
    # The efficient way to read the contents of the file is to simply iterate through each line of the file
    for line in f:
        print(line, end='')

    f.seek(0)
    # to have more control over exactly what we are reading from a file we acn use read() method and pass size
    # as argument
    f_contents_3 = f.read(100)
    print(f_contents_3, end='')  # prints the first 100 characters of the file
    f_contents_3 = f.read(100)
    print(f_contents_3, end='')  # prints the next 100 characters of the file

    f.seek(0)
    # instead of hard-coding we can use a variable which holds the number of characters to read and loop
    # through until the end of the file
    size_to_read = 10
    f_contents_4 = f.read(size_to_read)
    print('\n', f.tell())  # prints the current position -> 10
    while len(f_contents_4) > 0:
        print(f_contents_4, end='*')
        f_contents_4 = f.read(size_to_read)


# Let's look at how to write on to a file
# we need to open a file in write mode in order to write on to a file
with open('test2.txt', 'w') as f1:  # this will create a file write in to it if file doesn't exist and opens a file
    # if it does exist and overwrites it. If we do not want to overwrite the existing data in a file we must
    # use append 'a' mode so that it adds the data to the existing data in the file
    f1.write('Test')  # writes -> Test -> on to the file
    f1.write('File')  # writes -> File -> from the previous final position of the cursor in the file
    f1.seek(0)  # we can also use seek() method in write mode to manipulate the current position
    f1.write('Your')  # writes -> Your -> in place of Test as current position is changed to starting of the file


# Let's read from one file and write on to another file:
with open('test.txt', 'r') as rf:
    with open('test_copy', 'w') as wf:
        for line in rf:
            wf.write(line)


# Copying a picture file can be done in a similar way but we need to read and write image files in binary mode:
with open('white-tiger.jpg', 'rb') as rbf:
    with open('white-tiger-copy.jpg', 'wb') as wbf:
        for line in rbf:
            wbf.write(line)
