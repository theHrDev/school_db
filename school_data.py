
students = []
std = {}
def add_student(name,dept):
    std["name"] = name
    std["dept"] = dept
    
    students.append(std)
    return "student info added successfully"
    
def edit_student(index,key,newValue):
    if index not in range(len(students)):
        return f"Student with the index {index} does not exist"
    elif key not in students[index].keys():
        return f"Key {key} does not exist"
    
    students[index][key] = newValue
    return f"student with index {index}'s {key} has been changed to {newValue}"

def delete_student(index):
    if index not in range(len(students)):
        return f"Student with the index {index} does not exist"

    del students[index]
    return f"Student info deleted successfully"
    
def view_students():
    return f"The available students are \n {students}"
    

def data_management(menu):
    print(" Welcome to Oasis College.")
    if menu == "1":
        name = input("Enter the student name: ")
        dept = input("Enter the student dept: ")
        print(add_student(name=name,dept=dept))
    elif menu == "2":
        index = int(input("Enter the index for the student to be edited: "))
        key = input("Enter the key to be edited: ")
        newValue = input(f"Enter the new value for {key}: ")
        print(edit_student(index,key,newValue))
    elif menu == "3":
        index = int(input("Enter the index for the student to be deleted: "))
        print(delete_student(index))
    elif menu == "4":
        print(view_students())
    else:
        print("Unknown Menu")
    
    repeat = input("Do you want to perform another action\n1.yes\n2.no: ")
    if repeat == "1":
        menu = input("Enter a menu tot get started\n1. To add student\n2.To edit student details\n3.To delete student\n4.To view all students details: ")

        data_management(menu)
    else:
        print("Thanks for using our services")

menu = input("Enter a menu tot get started\n1. To add student\n2.To edit student details\n3.To delete student\n4.To view all students details: ")

data_management(menu)