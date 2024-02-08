student_score = {

"Alice": [85, 90, 92],
"bob": [78, 80, 85],
"charlie": [92, 88, 95]

}

student_grades = [student_score["Alice"],
student_score["bob"],
student_score["charlie"]
]

for student, grades in student_score.items():

	print(f'{student}', *grades)
