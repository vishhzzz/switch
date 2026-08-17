# working/iterating through data frame is very similar to working/iterating through dictionary.

import pandas

# iterating over dictionary
student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

for key, value in student_dict.items():
    print(key)
    print(value)

student_df = pandas.DataFrame(student_dict)
print(student_df)
for key, value in student_df.items():
    print(key)
    print(value)

print("------------------------")
# in pandas we have a way of iterating over rows, via iterrows()
for index, row in student_df.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)

    if row.student == 'Angela':
        print("hi angela")