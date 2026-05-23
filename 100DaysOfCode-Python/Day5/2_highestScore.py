# Python is very very number friendly language. It has a lot of built-in functions and libraries to work with numbers. In this file, we will see how to find the highest score from a list of scores.

student_scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
# sum of all the elements of list.
# sum needs any iterable (like list, tuple, set, etc.) as an argument and returns the sum of all the elements in the iterable.
print(f"Total Score of students: {sum(student_scores)}")
# maximum score from list.
# max needs any iterable (like list, tuple, set, etc.) as an argument and returns the maximum element in the iterable.
print(f"Highest Score of students: {max(student_scores)}")


# manual implementation of sum()
total_score = 0
for score in student_scores:
    total_score += score
print(f"Total Score of students: {total_score}")

# manual implementation of max()
max_score = 0 #we can either do this or
# we can do this [this is slightly better because it will work even if all the scores are negative]
max_score = student_scores[0]
# for score in student_scores: #if we do initialize variable with 0th element, then we need slight imprvement in for statement to start from index 1 instead of 0 because we have already assigned max_score to student_scores[0].
for score in student_scores[1:]: # this will start the loop from index 1 and will ignore the first element of the list.
    if score > max_score:
        max_score = score
print(f"Highest Score of students: {max_score}")