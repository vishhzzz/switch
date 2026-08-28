'''
We have seen a lot of errors
1. File Error - FileNotFound
with open("file_not_present_path") as f:
    f.read()

2. Key Error - KeyError
a_dict = {'key': 'value'}
print(a_dict['not_present_key'])

3. Index Error - IndexError
fruit_list = ['apple', 'banana', 'orange']
print(fruit_list[4])

4. Type Error
text = 'abc'
print(text + 3)

In programming, we can stop failing hard, we can 'catch exceptions' and decide what to do instead of failing hard.

We have 4 imp keywords:
1. try: use where exception can occur, basically anything where exception can occur.
2. except: do this when there is an exception.
3. else: do this when there is no exception.
4. finally: do this, no matter what happens.
5. raise: raise my own exception.
'''

# we will look into filenotfound error
# file = open("random.txt") #by default its read only mode.
# this line of code can cause error so, we will put it into try block.

try:
    file = open("random.txt")
except: #bare except is a very large pool for handling errors or exceptions, basically it will catch all the exceptions and errors. We need to narrow it down for our usecase.
    # if file is not present, create it after logging an error.
    file = open("random.txt", 'w') #if file not present then in w:write mode, it will create that file.
    file.write("Hi data written in file.")

try:
    file = open("random.txt")
    a_dict = {'key': 'value'}
    print(a_dict['not_present_key'])
except: #Here i'll show u the exact issue of using bare except
    # if file is not present, create it after logging an error.
    file = open("random.txt", 'w') #if file not present then in w:write mode, it will create that file.
    file.write("Hi data written in file.")
    print("Exception happened.\n")

'''
The flow of try except is
try - executes line by line, if any error occurs, goes inside except
except - handles the very 1st exception.

if in try, we have another exception then it does not even execute becoz program never returns to try again.

Now for the issue of bare except is:
for the very 1st time, there is 'filenotfound' error, it gets handled in except, now when u run again, file is now there due to code written in except, so it moves to execute other lines of code, it now executes dictionary code part, there again it sees an exception, then also this except will handle that... Thats the issue.
'''

# so the correct way is
try:
    file = open("random.txt")
    a_dict = {'key': 'value'}
    # print(a_dict['not_present_key'])
    print(a_dict['key'])
except FileNotFoundError:
    file = open("random.txt", 'w')
    file.write("Hi data written in file.")
    print("'FileNotFoundError' exception happened.\n")
except KeyError as error_msg:
    print(f"The key/{error_msg} u r searching for, is not there.\n")
    print("'KeyError' exception happened.\n")

    # We can also get to the exact error message which would normally be printed otherwise.
    # except KeyError as error_msg
else:
    content = file.read()
    print("Entered in else block.")
    print(content)
finally:
    file.close()
    print("Entered in finally.\n")