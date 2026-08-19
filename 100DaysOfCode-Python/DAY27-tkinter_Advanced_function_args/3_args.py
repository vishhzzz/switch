# *args: many positional arguements   Unlimited Positional Args.

# functions that can take 'n' no. of args.

# adding nos.
def add(n1, n2):
    return n1+n2

add(2, 3)

# but this is limited to 2 nos only, but what if we have to add multiple nos.???
# we can do this via this:
def add(*args): #args is by-default name for arguement, i.e., we can name it anything. args: arguements

    # instead of looping, we can also access it via indexes.
    print(args[0])
    print(args[3])
    sum = 0
    print(args)
    print(type(args))
    for n in args: #args is in form of tuples.
        # print(n)
        sum += n
    return sum
value = add(2, 3, 4, 5, 6, 7, 8)
print(value)
# *args ---> means it can understand n no. of args.
# * collects all the arg into a tuple.