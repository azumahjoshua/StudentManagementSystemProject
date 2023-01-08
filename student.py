class Student:
    # name = ''
    # student_id= ''
    def __init__(self):
        self.students = []

    def add_student(self):
         # Read two inputs from the user, separated by a space
        studentinfo= input("Enter Student Name and Student_id: ").strip().split(' ')
        # Validate the inputs: make sure that the first input is an integer and the second is a string
        if not studentinfo[1].isdigit() or not isinstance(studentinfo[0], str):
            raise ValueError('Invalid input')
        else :
            name = studentinfo[0]
            student_id = studentinfo[1]
            student = {"name": name, "student_id":   student_id}
            self.students.append(student)



    def view_students(self):
        for student in self.students:
            print(f"Name: {student['name']}, ID: {student['student_id']}")

    # search student by id
    def search_student(self,student_id):
        for student in self.students:
            if student['student_id'] == student_id:
                return student
        return None

    # remove student by id 
    def remove_student(self,student_id):
        try:
             student_id = int(student_id)
        except:print("Student id should be a number: ")
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
        else:
            print("Student not found.")

    # get total number of studnts
    def get_num_students(self):
        return len(self.students)


print("--------------------------Studnt Menu Options -----------------------------------------")
menu_options = {
    1: '(Create Student Register: )Option 1',
    2: '(Add a student: )Option 2',
    3: '(View student Record: )Option 3',
    4: '(Search student: )Option 4',
    5: '(Remove a student from the )',
    6: '(Get number of students)',
    7: 'Exit',
}

# create an object of  a user
# user = Hotelms()

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           students = Student()
        elif option == 2:
            students.add_student()
        elif option == 3:
            students.view_students()
        elif option == 4:
            search_student_id = int(input('Enter id of student to be serached: '))
            student = students.search_student(search_student_id)
            if student:
                print(f"Student with ID {search_student_id} found: {student['name']}")
            else:
             print(f"Student with ID {search_student_id} not found.")
        elif option == 5:
            search_student = int(input('Enter id of student to be removed: '))
            students.remove_student(search_student)
        elif option == 6:
            students.view_students()
        elif option == 7:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

