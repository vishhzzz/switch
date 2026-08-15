# we can play with os file system via python.

# 2 of the most basic thing which we can do right now is:
# ---> read [r]: read from file, file must be present.
# ---> write [w]: write to file, if file not present it will create that file.
# ---> append [a]: append to file, if file not present it will create that file.
# ---> read + write [r+]: read and write to file
# ---> write + read [w+]: erase all content and write from start.
# ---> append + read [a+]: read and append 

# open is an in-built method in python for this use-case i.e., used for reading a file
# return a file-like object which provides us functions to work with files
file = open("Day24-Files_Directories_PATH/my_file.txt")

# we can now read the content of that file via read method.
# this return the content in form of string.
content = file.read()

# see the content
print(content)



# after working with files, we should close it too. 
# Although Python automatically does that but when will it do is not known.

file.close()



# there is another way to deal with this....

# this is very manual and Python offers us a way to deal with this..
# we can use with as
with open("Day24-Files_Directories_PATH/my_file.txt", "r+") as file:
    content = file.read()
    print(content)

    # write into file
    file.write("This text came fron write operation.")

    # after writing pointer set to end of file. 
    # so if we wish to read now, it will not read anything
    # to reset the ptr, use seek
    file.seek(0)

    # write clears the existing content and then write with given data.
    # append (a) writes without clearing original content
    # r+ means reading + writing
    # w+ writing + reading
    # a+ append + reading

    content = file.read()
    print(content)



    # as soon as we come out of while loop then Python automatically closes the file.

# with uses 'Python's context manager mechanism which automatically calls close() when u leave with block.

# this works becoz open returns an object which supports this 'context-manager' protocol.

# open creates and returns file object.
# with takes that object.
# return object is assigned to file.
# when block end, python closes the file.
# and perform cleanup...
