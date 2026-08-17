# I am devloping a Caesar Cipher program which mimics the functionality of a Caesar Cipher. It will take a string and a shift number as input and will return the encrypted string by shifting each letter by the shift number. For example, if the input string is "hello" and the shift number is 3, then the output will be "khoor".

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

options = ['encode', 'decode']

def ciphingMessage(shift, message):
    # result = "" this is also fine but if we look conceptually then string are immutable in python so everytime anything added here creates a new string, using memory.
    result = []
    for char in message:
        if char.islower():
            result.append(chr((ord(char) - ord('a') + shift ) % 26 + ord('a'))) #lets say char is z whose ascii is 122, 122 - 97 + 3 + 97 = 125 which is } but it should be c -> (122 - 97 + 3) % 26 + 97
        elif char.isupper():
            result.append(chr((ord(char) - ord('A') + shift ) % 26 + ord('A')))
        else: #for any other char which can be whitespace or special char or so.
            result.append(char)
    result = "".join(result) #basically right now result is -> ['a', 'b', 'c']. "".join will join them without any space or extrachar -> "abc"
    return result

def encryptDecryptMessage():

    encryptDecrypt = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    # we can make a list and then search inside it rather than this seperate checks
    # if encryptDecrypt != "encode" and encryptDecrypt != "decode":
    if encryptDecrypt not in options:
        print("Please choose 'encode' or 'decode'.")
        return

    message = input("Type your message: ")

    # if user enters string or anything which is not a number then valueerror would be raised.
    try :
        shift = int(input("Type the shift number: "))
    except ValueError:
        print("Shift must be a number")
        return
    if shift < 1:
        print("Please enter correct shift, it should not be 0 or negative.")
        return
    #limiting shift value within 26.
    # Note: we dont explicitly need this wrap around code becoz later we r doing this only. it just improve readability and showcase intent.
    shift %= 26

    #we can do like this but here we r violating code rule: DRY = Dont Repeat Yourself.
    # if encryptDecrypt.lower() == "encode":
    #     for char in message:
    #         if char.islower():
    #             # we can ommit using an external list by proper usage of ascii.
    #             result += chr(ord(char) - ord('a') + shift + ord('a')) 
    #         elif char.isupper():
    #             result += ord(char) - ord('A') + shift + ord('A')
    #         else: #for any other char which can be whitespace or special char or so.
    #             result += char
    #     print(f"Here's the encoded result: {result}")
    # else:
        # for char in message:
        #     if char.islower():
        #         result += chr(ord(char) - ord('a') - shift + ord('a'))
        #     elif char.isupper():
        #         result += chr(ord(char) - ord('A') - shift + ord('A'))
        #     else: #for any other char which can be whitespace or special char or so.
        #         result += char
        # print(f"Here's the decoded result: {result}")
    
    # Whats changing in both if-else
    # shift 
    
    if encryptDecrypt == "decode": #decode
        shift *= -1
    result = ciphingMessage(shift, message)
    if encryptDecrypt == "encode": #encode
        print(f"Here's the encoded result: {result}")
    else: #decode
        print(f"Here's the decoded result: {result}")


# calling for 1st time
print(logo)
encryptDecryptMessage()

while True:
    userChoice = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if userChoice.lower() == "yes":
        encryptDecryptMessage()
    elif userChoice.lower() == "no":
        print("Thank you for playing caesar cipher.")
        break
    else:
        print("Please enter either 'yes' or 'no'.")
        break

# I can use set or tuple for storing mode/options - decode encode but that for later when i learn that.