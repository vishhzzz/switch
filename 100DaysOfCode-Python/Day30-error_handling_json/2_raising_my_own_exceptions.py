'''
raise is for raising manual exceptions
We can catch the raised exceptions by wrapping it inside try/except.
'''

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
else:
    content = file.read()
    print("Entered in else block.")
    print(content)
finally:
    file.close()
    print("Entered in finally.\n")

    # raising my own error
    # raise KeyboardInterrupt : general error with normal error msg.
    raise TypeError("Hi, this is my own error which i raised.\n")
