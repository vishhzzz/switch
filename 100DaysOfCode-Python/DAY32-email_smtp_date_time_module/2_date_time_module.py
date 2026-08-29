import datetime as dt

# will work with datetime class in datetime module
# now() will give current date-time from computer
now = dt.datetime.now()
print(now)
print(type(now)) #now is a datetime object.

# working directly with now is quite difficult as its a very long string and to do distinction is difficult
year = now.year
print(year)

# we can even get to know which weekday it is.
# it starts with 0.
weekday = now.weekday()
print(type(weekday), weekday)

# creating any date time object.
birthday = dt.datetime(year=2002, month=2, day=5)
print(birthday)