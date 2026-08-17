print(len("1234")) #will print 4

# print(len(1234)) #error type error as int object has no len function.

# Type Check: type()
print(type("1234")) #string : class <str>
print(type(1234)) #integer : class <int>
print(type(12.34)) #floating point no : class <float>
print(type(True)) #boolean : class <bool>

print("*******************************************")
# Type Conversion
# We can convert one data type to another data type using these functions
# str : str()
print(type(str(1234)))

# int : int()
print(type(int("1234")))

# float : float()
print(type(float("12.34")))

# bool : bool()
print(type(bool(1))) # True