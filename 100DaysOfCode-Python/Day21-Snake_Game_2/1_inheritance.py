# The process of inheriting behaviour and appearance from existing class is aka 'INHERITANCE'.

# Suppose u r working on a restro project, there u have a chef  but now u want a pastry chef then its not ideal to build it from scratch but make it inherit from chef i.e., all the things chef knows should be known to pastry chef and then something extra.

# We can inherit both apperance - attributes 
                    #   behaviour - methods

# normal class way
class Fish():
    def __init__(self):
        pass


# inheritance
# class Fish(Animal):         #inheriting from animal class 
#     def __int__(self):
#         super.__init__()    # super here referes to super class which is Animal here.
        # it initialize everything superclass-animal do in fish class.



class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Exhale - Inhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("swimming in water.")

    # for changing or modifying parent's function
    def breathe(self):
        # hold of parent function
        super().breathe() # everything breathe does + extra 
        print("Breathing in water")

fish = Fish()
print(fish.num_eyes)
fish.breathe()
fish.swim()
