# attribute : what object has
# method : what object does

# METHOD ---> function when attached to an object is called method.
# Unlike function, method is something which must have a arguement i.e., self so that it can know/access the object who called it.

class User:
    # constructor
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.following = 0
        self.followers = 0
    # user_id, user_name, following, followers <--- attributes

    # method
    def follow(self, user): #self: to know the object which called the function, user: the other user whom we want to follow.
        self.following += 1
        user.followers += 1
    

user_1 = User(1, "Vishal")
user_2 = User(2, "Kumar")
print(user_1.following)
print(user_2.followers)
user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)
