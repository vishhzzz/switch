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
lowercase = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

uppercase = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

def encryptDecryptMessage():
    encryptDecrypt = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    if encryptDecrypt.lower() != "encode" and encryptDecrypt.lower() != "decode":
        print("Please choose 'encode' or 'decode'.")
        return
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    if shift < 1:
        print("Please enter correct shift, it should not be 0 or negative.")
        return
    result = ""
    if encryptDecrypt.lower() == "encode":
        for char in message:
            print(ord(char))
            print(shift % 26)
            print(chr(ord(char) - ord('a') + shift % 26))
            if char.islower() == True:
                result += lowercase[(ord(char) - ord('a') + shift) % 26]
            else:
                result += uppercase[(ord(char) - ord('A') + shift) % 26]
            print(result) 
        print(f"Here's the encoded result: {result}")
    else:
        for char in message:
            if char.islower() == True:
                result += lowercase[(ord(char) - ord('a') - shift) % 26]
            else:
                result += uppercase[(ord(char) - ord('A') - shift) % 26]
        print(f"Here's the decoded result: {result}")
        

# Type 'yes' if you want to go again. Otherwise type 'no'.
# calling for 1st time
print(logo)
encryptDecryptMessage()

while 1:
    userChoice = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if userChoice.lower() == "yes":
        encryptDecryptMessage()
    elif userChoice.lower() == "no":
        print("Thank you for playing caesar cipher.")
        break
    else:
        print("Please enter either 'yes' or 'no'.")
        break
        