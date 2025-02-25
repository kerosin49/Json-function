# import json

# def get_student_by_id(filename, student_id):
#     with open(filename, 'r') as f:
#         students = json.load(f)
#         for student in students:
#             if student.get('student_id') == student_id:
#                 return student
#     return None

# student = get_student_by_id('data.json', 3)

# if student:
#     print(student)
# else:
#     print("Студент не найден")
import json
f = open('data.json', 'r')
data = json.load(f)
f.close()
print(data)
