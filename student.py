
class Student:
    def __init__(self,students=[]):
        self.students = students

    def add_student(self):
        # Read two inputs from the user, separated by a space
        student_name = input("Enter Student Name: ")
        student_id = input("Enter Student Id: ")
        # Validate the inputs: make sure that the first input is a string and the second is an integer
        if not isinstance(student_name, str) or not student_id.isdigit():
            raise ValueError('Invalid input')
        else:
            name = student_name
            student_id = student_id
            student = {"name": name, "student_id": student_id}
            self.students.append(student)

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

    # remove student by id
    def delete_student(self, student_id):
        """"
        In the delete_student method, the enumerate() function is used in combination with a for 
        loop to iterate through the list of students. The enumerate() function adds a counter 
        to an iterable and returns it in a form of enumerate object, which is an iterator containing pairs 
        (index, element). This allows you to both access the elements of the list, as well as 
        keep track of their index within the list.
        When you iterate over the students list using the for loop, the enumerate()
        function adds a counter variable to each iteration. In this case, 
        i is the counter variable and it holds the current index of the student in the students list.
        This is useful in this case because it allows to find the index of the student object that is 
        to be deleted using the student_id passed to the function. Once we know the index, 
        we can then remove that student object from the list using the del statement and the index of the element.
        """
        # Check if student_id is an integer
        try:
            for student in self.students:
                if student["student_id"] == student_id:
                    self.students.remove(student)
                    print("Student has been removed.")
                    return
            raise ValueError(f"Student with ID {student_id} not found")
        except ValueError as e:
            print(e)

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
            print("-------------------View Searchecd Student-----------------")
            search_student_id = input('Enter id of student to be searched: ')
            student = students.search_student(search_student_id)
            if student:
                print("-------------------View Searchecd Student-----------------")
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
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


# class TestStudentMethods(unittest.TestCase):
# 
    # def setUp(self):
        # self.students = Student()
# 
    # def test_add_student(self):
        # self.students.add_student()
        # self.assertEqual(len(self.students.students), 1)
        # self.students.add_student()
        # self.assertEqual(len(self.students.students), 2)
# 
    # def test_search_student(self):
        # self.students.add_student()
        # self.assertIsNotNone(self.students.search_student("1"))
        # self.assertIsNone(self.students.search_student("2"))
# 
    # def test_remove_student(self):
        # self.students.add_student()
        # self.assertEqual(len(self.students.students), 1)
        # self.students.remove_student("1")
        # self.assertEqual(len(self.students.students), 0)
# 
    # def test_get_num_students(self):
        # self.students.add_student()
        # self.assertEqual(self.students.get_num_students(), 1)
        # self.students.add_student()
        # self.assertEqual(self.students.get_num_students(), 2)
# 
# 
# if __name__ == '__main__':
    # unittest.main()
