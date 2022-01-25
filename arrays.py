import numpy as np
import pandas as pd
import math
# Marks obtained by students in Python class
data = [50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82, 62, 37, 15, 70, 27, 36, 35, 48, 52, 63, 64]
grades = np.array(data)
# Study hours by students in Math class
study_hours = [10.0, 11.5, 9.0, 16.0, 9.25, 1.0, 11.5, 9.0, 8.5, 14.5, 15.5,
               13.75, 9.0, 8.0, 15.5, 8.0, 9.0, 6.0, 10.0, 12.0, 12.5, 12.0]
# A 2D array of study hours and grades
student_data = np.array([study_hours, grades])
print(student_data)
# Mean value of each sub array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))

df_students = pd.DataFrame({'Name': ['Henry', 'Prince', 'Solomon', 'Kelly', 'Matthew', 'Arthur', 'Jochebed', 'Ceci',
                                     'Rhonda', 'Emmanuel', 'Francesca', 'Bamfo', 'Christoph', 'Thelma', 'Vanessa',
                                     'Michael', 'Roseline', 'Nick', 'Priscilla', 'Davis', 'Benedicta', 'Sabrina'],
                            'StudyHours': student_data[0],
                            'Grade': student_data[1]})
print(df_students)
print(df_students.loc[df_students['Name'] == 'Kelly'])
print(df_students.query('Name == "Solomon"'))

# Loading a DataFrame from a file
