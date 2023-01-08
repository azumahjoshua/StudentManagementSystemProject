from student import Student

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
        print(key, '--', menu_options[key])


if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            students = Student()
        elif option == 2:
            students.add_student()
        elif option == 3:
            students.view_students()
        elif option == 4:
            search_student_id = int(
                input('Enter id of student to be serached: '))
            student = students.search_student(search_student_id)
            if student:
                print(
                    f"Student with ID {search_student_id} found: {student['name']}")
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
