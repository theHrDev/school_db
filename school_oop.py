import random
class Students:
    def __init__(self):
        self.students = {}
    
    def add_student(self,name,dept,age):
        id = random.randint(10**3,10**3+1)
        new_student = Student(id=id,name=name,dept=dept,age=age)
        s_id = new_student.id
        self.students[s_id] = {'id':new_student.id, 'name':new_student.name,'dept':new_student.dept,'age':new_student.age}
        return "Student added successfully"
    
    def delete_student(self,id):
        if id not in self.students:
            return "No student with the provided id"
        del self.students[id]
        return "Student deleted successfully"
    
    def edit_student(self):
        pass
    
    
    def view_single_student(self):
        pass
    
    
    def view_all_students(self):
        if not self.students:
            return "No student found"
        return self.students
    
class Student:
    def __init__(self,name,dept,age,id):
        self.name = name
        self.dept = dept
        self.age = age
        self.id = id
        
        
def student_db():
    students = Students()
    print("Welcome to student data")
    while True:
        print("-------- 1.Add Student ----------")
        print("-------- 2.View All Student ----------")
        print("-------- 3.Exit ----------\n")
        menu = input("Enter menu: ")
        if menu == "1":
            name = input("Enter the student name: ")
            age = input("Enter the student age: ")
            dept = input("Enter the student dept: ")
            print(students.add_student(name=name,age=age,dept=dept))
        elif menu == "2":
            print(students.view_all_students())
        elif menu == "3":
            break
        else:
            print("Invalid input")
    
student_db()