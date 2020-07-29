# os module is a built-in module which allows us to interact with underlying operating system in
# several different ways
import os
from datetime import datetime  # this is used in the later part of the file


# to see all the attributes and methods available in os module we can use dir() function
print(dir(os))

# to get the current working directory we use getcwd() method
print(os.getcwd())  # prints -> C:\Bhanu_Applications\Python\Tutorial\Beginner

# to navigate to new location in our file system we use chdir() method
os.chdir('C:\Bhanu_Applications\Python\Tutorial')
print(os.getcwd())

# to see what files and folders are present we use listdir() method
print(os.listdir())  # we can also pass path as argument to see the files and folders in that path

# to create a new directory we can use mkdir() method or makedirs() method:
# mkdir() method will create only create main directory and cannot create sub level directories at same time
os.mkdir('MainDir')
print(os.listdir())

# makedirs() method will create main directory as well as sub level directories at the same time
os.makedirs('Main-dir/Sub-dir')
print(os.listdir())

# to delete a directory we can use rmdir() method and removedirs() method
# os.rmdir() method removes only main directory which have no sub level directories
os.rmdir('MainDir')
print(os.listdir())

# os.removedirs() method removes all main and sub level directories
os.removedirs('Main-dir/Sub-dir')
print(os.listdir())

# to rename a file or folder name we use rename() method
# os.rename('test.txt', 'demo.txt')  # renaming directory name from test to demo
# print(os.listdir())

# to get all the information related to a file we use stat() method
print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_size)  # prints size of the file in bytes
print(os.stat('demo.txt').st_mtime)  # prints modification timestamp

# to get this modified time in a readable format we use fromtimestamp() method of datetime module
readable_timestamp = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(readable_timestamp))  # prints timestamp in a human readable format

# to entire directory tree and the files within the directory we us e walk() method
# os.walk() is a generator which yields a tuple of 3 values -> directory path, directories within that path and
# files within that path
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

# to access all environment variables we use os.environ
print(os.environ)
print(os.environ.get('HOMEPATH'))  # prints the path present in the environment variable HOMEPATH

# if we want to create a new file within that HOMEPATH we use join() method from os.path module
file_path = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
print(file_path)

# few other useful methods with os.path module are basename(), dirname(), split():
# basename() method prints the basename of the entire path
print(os.path.basename('/tmp/demo.txt'))  # prints base name -> demo.txt

# dirname() method prints the directory name of that path
print(os.path.dirname('/tmp/demo.txt'))  # prints directory name of that path -> /tmp

# split() method gives both directory name and also base name
print(os.path.split('/tmp/demo.txt'))  # prints directory name and file name -> ('/tmp', 'demo.txt')

# to check whether the path exists we use exists() method in os.path module
print(os.path.exists('/tmp/demo.txt'))  # prints -> False

# to check if something is a directory we use isdir() method in os.path module
print(os.path.isdir('/tmp/asdf'))  # prints -> False

# to check if something is a file we use isfile() method in os.path module
print(os.path.isfile('/tmp/asdf'))  # prints -> False

# to split the extension with the root of the path we use splitext() method in os.path module
print(os.path.splitext('/tmp/demo.txt'))

# to see all the attributes and methods in os.path module we can use dir() function
print(dir(os.path))
