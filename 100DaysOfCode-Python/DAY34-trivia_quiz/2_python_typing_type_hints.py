'''
There is 1 more wonder in Python
We can specify the data type against a variable and later assign that value accordingly, if not then editors show warning

It is like announcing i am creating a variable named age and it should be int

but later if u assign string or float, python itself will not stop u becoz python is Dynamic Typed.

This is called 'TYPE HINT'

this also works for passing parameters in Python functions.
'''
age: int
height: float
name: str




# age = 12
age = "Vishal"

# -> bool tells that it is suppose to return bool value.
def dummy_function(dummy_param: int) -> bool:
    pass