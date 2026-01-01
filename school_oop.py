import random
class Students:
    def __init__(self):
        self.students = {}
    
    def add_student(self,name,dept,age):
        id = random.randint(1000,9999)
        new_student = Student(id=id,name=name,dept=dept,age=age)
        s_id = new_student.id
        self.students[s_id] = new_student
        return "Student added successfully"
    
    def delete_student(self,id):
        if id not in self.students:
            return "No student with the provided id"
        del self.students[id]
        return "Student deleted successfully"
    
    def edit_student(self,id , new_name):
        if id not in self.students:
            return "No student with the provided id"
        self.students[id].name = new_name
        return "name edited successfully"
        
    
    
    def view_single_student(self,id):
        if id not in self.students:
            return "No student with the provided id"
        s = self.students[id]
        return f"ID: {s.id} | Name: {s.name} | Dept: {s.dept} | Age: {s.age}"
    
    
    def view_all_students(self):
        if not self.students:
            return "No student found"
        result = []
        for s in self.students.values():
            result.append(f"ID: {s.id} | Name: {s.name} | Dept: {s.dept} | Age: {s.age}")
        return "\n".join(result)
    
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
        print("-------- 2.View single Student ----------")
        print("-------- 3.Edit Student ----------")
        print("-------- 4.Delete Student ----------")
        print("-------- 5.View All Student ----------")
        print("-------- 6.Exit ----------\n")
        menu = input("Enter menu: ")
        if menu == "1":
            name = input("Enter the student name: ")
            age = input("Enter the student age: ")
            dept = input("Enter the student dept: ")
            print(students.add_student(name=name,age=age,dept=dept))
        elif menu == "2":
            id = int(input("Enter student id: "))
            print(students.view_single_student(id=id))
        elif menu == "3":
            id = int(input("Enter student id: "))
            new_name = input("Enter new name: ")
            print(students.edit_student(id=id, new_name=new_name))

        elif menu == "4":
            id = int(input("Enter student id: "))
            print(students.delete_student(id=id))
        elif menu == "5":
            print(students.view_all_students())
        elif menu == "6":
            break
        else:
            print("Invalid input")
    
student_db()