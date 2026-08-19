# **kwargs : many key worded args.

# kwargs is a dictionary it holds keyword args, keyword as key and args as value.
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))

    # looping through
    for key, value in kwargs.items():
        print(key, value)

    # or names
    print(kwargs['add'])
    # also via get method
    # benefit: if key is not there, it will return none and not the error.
    print(kwargs.get('add'))
    print(kwargs['mul'])

    n += kwargs['add']
    n *= kwargs['mul']
    print(n)

calculate(4, add=5, mul=6)


# here we have a default args, along with keyword args., keyword args wins...
def trial(num = 2, **kwargs):
    print(num)

trial(num=67)