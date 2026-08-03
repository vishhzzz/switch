word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# If u notice here, there is something very fishy going on...
# at line no. 3, we can see that instead of =, we are using == which basically means comparision i.e., instead of assigning we are comparing the 2 values which will result in run-time issues.

# so the fix is to use = instead of ==.
