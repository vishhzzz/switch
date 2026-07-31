class User:
    pass

# creating objects
user = User()

# creating attributes
user.id = 1
user.user_name = "vishal"

# right now these r just variables but r attached to a single object.

print(user.user_name)


# suppose i had a lot of objects then how can i do this everytime???


# so is there anything which can make this easy for us to pass on this starting info...

# We can do that via "CONSTRUCTOR"
# CONSTRUCTOR    ---    initializing an object
# part of blueprint i.e., class which tells us that what should happen when our object is being constructed.

# In python we does this via a special function called init
#  __init__()  <-- special function
# will be called everytime an object is being created.

# self : actual object which is being created or initialized.

class User:
    # constructor
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        # we can also have an attribute with a default value, we can later modify this at our own use-case.
        self.follower = 0


user_1 = User(1, "vishal") # this will automatically assign 1 to id.

print(user_1.id)
print(user_1.user_name)
print(user_1.follower)

# as we have now the __init__ function then this means is whenever u want to create a new object, u have to have pass id and user name to the class basically constructor.