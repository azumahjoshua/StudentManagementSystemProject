class Student:
    def __init__(self,students=[]):
        self.students = students

    def add_student(self):
       
        # Validate the inputs: make sure that the first input is a string and the second is an integer
        while True:
             # Read two inputs from the user, separated by a space
            student_name = input("Enter Student Name: ")
            student_id = input("Enter Student Id: ")
            if not isinstance(student_name, str) or not student_id.isdigit():
               print('Invalid input try again.')
               continue
            else:
                name = student_name
                student_id = student_id
                student = {"name": name, "student_id": student_id}
                self.students.append(student)
                break

    def view_students(self):
        print("-------------------View Student-----------------")
        for student in self.students:
            print(f"Name: {student['name']}, ID: {student['student_id']}")
        print("\n")

    # search student by id
    def search_student(self, student_id):
        for student in self.students:
            if student['student_id'] == student_id:
                return student
        return None

 # search student by name
    def search_student_by_name(self, name):
        for student in self.students:
            if student['name'] == name:
                return student
        return None

    # remove student by id
    def delete_student(self, student_id):

        # Check if student_id is an integer
        try:
            for student in self.students:
                if student["student_id"] == student_id:
                    self.students.remove(student)
                    print("Student has been removed.")
                    return
            raise ValueError(f"Student with ID {student_id} not found")
        except ValueError:
            print("input data is wrong")

    # get total number of students
    def get_num_students(self):
        return len(self.students)


print("--------------------------Student Menu Options -----------------------------------------")

menu_options = {
    1: 'Add a student (Option 1)',
    2: 'View student Record (Option 2)',
    3: 'Search student (Option 3)',
    4: 'Remove a student (Option 4)',
    5: 'Get number of students (Option 5)',
    6: 'Exit (Option 6)',
}

students = Student() #create an object of a student
def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


if __name__ == '__main__':
    while (True):
        print_menu()
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Wrong input. Please enter a number ...')
            continue
        # Check what choice was entered and act accordingly
        if option == 1:
            students.add_student()
            print("Student has successfully been added\n")
        elif option == 2:
            students.view_students()
        elif option == 3:
            print("-------------------View Searched Student-----------------")
            search_student_id = input('Enter id of student to be searched: ')
            student = students.search_student(search_student_id)
            if student:
                print("-------------------View Searched Student-----------------")
                print(f"Student with ID {search_student_id} found: {student['name']}")
            else:
                print("Student was not found")
            print("\n")
        elif option == 4:
            search_student = (input('Enter id of student to be removed: '))
            students.delete_student(search_student)
        elif option == 5:
            print(f"Number students: {students.get_num_students()}")
        elif option == 6:
            print('goodbye!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')


