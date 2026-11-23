class StudentDatabase:
    student_list=[]
    @classmethod
    def add_students(cls,student):
        cls.student_list.append(student)
class Student:
    def __init__(self,student_id,name,department):
        self._student_id = student_id
        self._name= name
        self._department = department
        self._is_enrolled = False

        StudentDatabase.add_students(self)

    def get_student_id(self):
        return self._student_id

    def enroll_student(self):
        if self._is_enrolled:
            print("Error: Student is already enrolled.")
        else:
            self._is_enrolled = True
            print("Student enrolled successfully!")

    def drop_student(self):
        if not self._is_enrolled:
            print("Error: Student is not enrolled.")
        else:
            self._is_enrolled = False
            print("Student dropped successfully!")

    def view_student_info(self):
        print("\n----- Student Information -----")
        print("Student ID:", self._student_id)
        print("Name:", self._name)
        print("Department:", self._department)

        if self._is_enrolled:
            print("Status: Enrolled")
        else:
            print("Status: Not Enrolled")

Student1 = Student("101","Ridoy","CSE")
Student2 = Student("102","kawsar","CV")
Student3 = Student("103","Shovom","THEM")

while True:
    print("\n===== Student Database Management System =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your Choice: ")

    if(choice =="1"):
        if len(StudentDatabase.student_list)==0:
            print("No students found.")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif choice == "2":
        student_id = input("Enter Student ID: ")
        found = False

        for student in  StudentDatabase.student_list:
            if student.get_student_id() == student_id:
                student.enroll_student()
                found =  True
                break
        if not found:
            print("Error: Invalid Student ID.")

    elif choice == "3":
        student_id = input("Enter Student ID: ")
        found = False

        for student in StudentDatabase.student_list:
            if student.get_student_id()==student_id:
                student.drop_student()
                found = True
                break
        if not found:
            print("Error: Invalid Student ID.")

    elif choice == "4":
        print("Thank you for using Student Database!")
        break

    else:
        print("Invalid choice! Please try again.")

