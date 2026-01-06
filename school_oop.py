import random
class Student:
    def __init__(self,name,dept,age,id):
        self.name = name
        self.dept = dept
        self.age = age
        self.id = id
        self.enrolled_courses = []
        
class Course:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.enrolled_students = []
        
# STUDENTS CLASS
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
    
# COURSES CLASS
class Courses:
    def __init__(self):
        self.courses = {}
        
    def generate_course_id():
        id = random.randint(10*5, 10*6-1)
        formated_id = f'course{id}'
        return formated_id
    
    def create_course(self,name):
        course_id = self.generate_course_id()
        new_course = Course(id=course_id,name=name)
        self.courses[course_id] = new_course
        return "course added successfully"
    
    def view_single_course(self,course_id):
        if course_id not in self.courses:
            return "no course found"
        course = self.courses[course_id]
        return f"ID: {course.id} name : {course.name} enrolled_student: {course.enrolled_students}"
    
    def edit_course(self,course_id,title):
        if course_id not in self.courses:
            return "no course found"
        self.courses[course_id].name = title
        return "course title edited successfully"
    
    def delete_course(self,course_id):
        if course_id not in self.courses:
            return "no course found"
        del self.courses[course_id]
        return "course deleted successfully"
    
    def view_all_courses(self):
        if not self.courses:
            return "no courses found"
        results = []
        for course in self.courses.values():
            results.append(f"course_id: {course.id} title: {course.name} enrolled_students : {course.enrolled_students}")
            return "\n".join(results)


# ENROLLMENT CONTROLLER
class EnrollmentController:
    def __init__(self,students,courses):
            self.students = students
            self.courses = courses
            
    def enroll_student(self,student_id,course_id):
        if student_id not in self.students.students:
            return "Please enter valid student id"
        if course_id not in self.courses.courses:
            return "Please enter valid course id"

        course = self.courses.courses[course_id]
        student = self.students.students[student_id]
        
        if course in student.enrolled_courses:
            return "Student already enrolled in this course"
        
        student.enrolled_courses.append(course)
        course.enrolled_students.append(student)
        return f"enrollment successful"
    def drop_student(self,student_id,course_id):
        if student_id not in self.students.students:
            return "Please enter valid student id"
        if course_id not in self.courses.courses:
            return "Please enter valid course id"
        course = self.courses.courses[course_id]
        student = self.students.students[student_id]
        
        if student not in course.enrolled_students:
            return "registration not found"
        course.enrolled_students.remove(student)
        student.enrolled_courses.remove(course)
        
        return "student dropped from course"
    def list_student_courses(self,student_id):
        if student_id not in self.students.students:
            return "Please enter valid student id"
        student = self.students.student[student_id]
        if not student.enrolled_courses:
            return "No courses enrolled"
        return "\n".join(f"{c.id} : {c.name}" for c in student.enrolled_courses)
    def list_course_students(self,course_id):
        if course_id not in self.courses.courses:
            return "Invalid course id"
        
        course = self.courses.courses[course_id]
        if not course.enrolled_students:
            return "No students enrolled"
        
        return "\n".join(f"{s.id} : {s.name}" for s in course.enrolled_students)
        
def student_menu(students):
    while True:
        print("\n--- Student Menu ---")
        print("1. Add Student")
        print("2. View Student")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. View All Students")
        print("6. Back")

        choice = input("Select option: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            dept = input("Department: ")
            print(students.add_student(name, dept, age))

        elif choice == "2":
            sid = int(input("Student ID: "))
            print(students.view_single_student(sid))

        elif choice == "3":
            sid = int(input("Student ID: "))
            new_name = input("New name: ")
            print(students.edit_student(sid, new_name))

        elif choice == "4":
            sid = int(input("Student ID: "))
            print(students.delete_student(sid))

        elif choice == "5":
            print(students.view_all_students())

        elif choice == "6":
            break
def course_menu(courses):
    while True:
        print("\n--- Course Menu ---")
        print("1. Create Course")
        print("2. View Course")
        print("3. Edit Course")
        print("4. Delete Course")
        print("5. View All Courses")
        print("6. Back")

        choice = input("Select option: ")

        if choice == "1":
            name = input("Course name: ")
            print(courses.create_course(name))

        elif choice == "2":
            cid = input("Course ID: ")
            print(courses.view_single_course(cid))

        elif choice == "3":
            cid = input("Course ID: ")
            title = input("New title: ")
            print(courses.edit_course(cid, title))

        elif choice == "4":
            cid = input("Course ID: ")
            print(courses.delete_course(cid))

        elif choice == "5":
            print(courses.view_all_courses())

        elif choice == "6":
            break
def enrollment_menu(enrollment):
    while True:
        print("\n--- Enrollment Menu ---")
        print("1. Enroll Student in Course")
        print("2. Drop Student from Course")
        print("3. View Student's Courses")
        print("4. View Course's Students")
        print("5. Back")

        choice = input("Select option: ")

        if choice == "1":
            sid = int(input("Student ID: "))
            cid = input("Course ID: ")
            print(enrollment.enroll_student(sid, cid))

        elif choice == "2":
            sid = int(input("Student ID: "))
            cid = input("Course ID: ")
            print(enrollment.drop_student(sid, cid))

        elif choice == "3":
            sid = int(input("Student ID: "))
            print(enrollment.list_student_courses(sid))

        elif choice == "4":
            cid = input("Course ID: ")
            print(enrollment.list_course_students(cid))

        elif choice == "5":
            break

def main():
    students = Students()
    courses = Courses()
    enrollment = EnrollmentController(students, courses)

    while True:
        print("\n====== UNIVERSITY MANAGEMENT SYSTEM ======")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Enrollment Management")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            student_menu(students)
        elif choice == "2":
            course_menu(courses)
        elif choice == "3":
            enrollment_menu(enrollment)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


main()