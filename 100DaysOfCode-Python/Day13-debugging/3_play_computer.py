year = int(input("What's your year of birth.?"))

if year > 1980 and year < 1994:
    print("You r millenial.")
elif year > 1994:
    print("You r GenZ.")
else: #1994
    print("this is the fix.....")

# The problem here is there will be nothing for case year == 1994. Becoz we r either dealing with > 1994 or <1994.
