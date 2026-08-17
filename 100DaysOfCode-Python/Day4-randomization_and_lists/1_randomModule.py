# Computers are deterministic machines, which means that they will always produce the same output for a given input.
# However, sometimes we want to generate random numbers or make random choices in our programs.
# This is where the random module comes in handy.

# Any Programming language does random number generation using a pseudo-random number generator (PRNG) algorithm.
# A PRNG is an algorithm that generates a sequence of numbers that approximates the properties of random numbers.
# The sequence is determined by an initial value called the seed.
# If you use the same seed, you will get the same sequence of random numbers.
# The random module in python uses the Mersenne Twister algorithm, which is a widely used PRNG algorithm.

# random is a module in python which contains functions for generating random numbers and making random choices.
# inbuilt library in python, so we need to import it before using it.
import random
# randint(a, b) means both a and b are inclusive.
randomNum = random.randint(1, 10) # this will generate a random integer between 1 and 10 (inclusive).
print(randomNum)

# What exactly is modules in python?
# modules are a way to organize code in python.
# Each module serves a specific purpose and can be imported and used in other parts of the code.
# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
# A module can define functions, classes, and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized and prevents name clashes between different parts of the code.


# inorder to use contents of a module, we first import it using import statement. We can import the entire module or specific functions, classes, or variables from the module.
import my_module
print(f"My fav number is: {my_module.my_fav_num}") # this will print the value of my_fav_num which is defined in my_module.py file.

# random for float
randomFloat = random.random() # this will generate a random float between 0.0 and 1.0 (inclusive of 0.0 but not 1.0).
print(randomFloat)
print(f"{randomFloat:.2f}") # this will print the random float with 2 decimal places.

# we can increase the range of random float by multiplying it with a number.
randomFloat = random.random() * 5 # this will generate a random float between 0.0 and 5.0 (inclusive of 0.0 but not 5.0).
print(randomFloat)

# its alternative is uniform(a, b) which will generate a random float between a and b (inclusive of a but not b).
randomFloat = random.uniform(1, 10) # this will generate a random float between 1.0 and 10.0 (inclusive of 1.0 but not 10.0).
print(randomFloat)

# diff between random() and uniform() is that random() generates a random float between 0.0 and 1.0, while uniform(a, b) generates a random float between a and b.


# Heads or Tails 
coin = random.randint(0, 1) # this will generate a random integer between 0 and 1 (inclusive).
if coin == 0:
    print("Heads")
else:
    print("Tails") 