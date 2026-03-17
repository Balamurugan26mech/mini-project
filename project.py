student={}
def add_student(name, marks):
    student[name]=marks
    print("Student added successfully.")
def display_student():
   for name, marks in student.items():
       print(name, ":", marks)
add_student("Alice", 85)
add_student("Bob", 90)
display_student()