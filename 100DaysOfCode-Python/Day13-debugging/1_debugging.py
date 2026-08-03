def funct():
    for i in range(1, 20):
        if i == 20:
            print("HI")

funct()

# why HI is not being printed.? --> ISSUE : need to debug this
# range(a, b) : a starting point, b ending point but not included.
# a, a+1, a+2, ., ., ........., b-1 : this is the list of elements which falls under range(a, b)