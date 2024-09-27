from myClass import my_name

# my_name: str = "BIlal"
my_age: int = 12
is_active: bool = True

student_01: str = "Bilal"
# print("Students: ", student_01[-1:-6:-2])


students: list[str | int] = ["bilal", "Hamza", "Hammad", "CHris", "John", "bilal", "Henry"]
# print("Students: ", students[-1:-6:-2])

# For comment we use "#"

# "Hamza", "Hammad", "CHris", "John", "Henry"
# "Hamza","CHris","Henry"
# print("Students: ", students[-1:-6:])


# students[0]
# print("Before changed", students)

# students[0] = "Bilal"

# print("After changed: ", students)

# Tuples:
online_students = ("bilal", "Faraz", "Ahsan")
# print("Online student name: ", online_students[0])

# Set:

print("Before", online_students)

# online_students[0] = "Bilal" Error because of immutable

print("After", online_students)

user = {
    "username": "Bilal",
    "age": 12,
    "isActive": True,
    "Password": "123"
}

# unique_students: set = {students}

# print(f"Unique students: {unique_students}")

# students = {
#     "studentNames": ["bilal", "eduction"],
#     "age": [12, 13],
#     "isActive": True,
#     "Password": "123"
# }

# # Nested Dictionary
# student: dict = {
#     "name": "Bilal",
#     "courses": {
#         "languages": {
#             "German": 70
#         },
#         "coding": {
#             "python": [100, 90, 80],
#             "javascript": {
#                 "Beginning": 50,
#                 "Intermediate": 70,
#                 "Advanced": 90
#             }
#         },
#         "english": []
#     },
# }

# print(student["courses"]["coding"]["javascript"]["Intermediate"])


# Type Casting
str(10)
int("10") # -> it wil convert into integer
print(float(10)) # 10.0


# String:

# Simple string:
name = "bilal"

# F-String:
math_marks = 90
computer_marks = 70

total: int = math_marks + computer_marks

# Single quote string
student_prop = ''
# Double quote string
message = "Your total marks is" + str(total)

# Single Triple quote string
student_prop = '''
My name is bilal I work 
I work as a developer
'''

# Double Triple quote string
student_prop = """
My name is bilal I work 
I work as a developer
"""


# Double Triple quote with F-String
message = f"""
===============================================
Your total marks is {total}. 
===============================================
Computer marks: {computer_marks}
Math Marks: {math_marks}
===============================================
"""

# Jinja Style
admin_data = f"""
===============================
Name: %d
Phone Number: %d
Card Number: %d
CVC: %d
===============================
""" % (1, 31243434, 4242424, 123)

print(type(admin_data))
print("True is: ", True == 1)
print("False is: ", False == 1)

ADMIN = "bilal"


