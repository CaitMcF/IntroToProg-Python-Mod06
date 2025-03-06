# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Caitlyn M, 3/5/25, Created and Edited Script
# ------------------------------------------------------------------------------------------ #

# Import json converts to json string format
import json
from typing import IO

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the variables
# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
#csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# Processing with Classes
class FileProcessor:
    """
    A collection of processing layer functions that work with json files
        ChangeLog:
        Caitlyn M, 05 Mar 2025, Created class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads data from a file and converts it into json format
        ChangeLog:
        Caitlyn M, 05 Mar 2025, Created class
        :param file_name: File that program is reading from
        :param student_data: A list of dictionary rows
        :return: A list of dictionaries
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        # Error handling below
        except FileNotFoundError as e:
            IO.output_error_message(message = "Text file not found")
        except Exception as e:
            IO.output_error_messages("There was a non-specific error", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # Removed global file and student variables
        """
        This function writes data to a json file. Data is in a list of dictionary rows
        ChangeLog:
        Caitlyn M, 05 Mar 2025, Created class
        :param file_name: JSON file created that data is written to
        :param student_data: list of dictionary rows
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following students have been registered: ")
            IO.output_student_courses(student_data)
        except TypeError as e:
            IO.output_error_messages("Please check that the data is in valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error", e)
        finally:
            if not file.closed:
                file.close()


class IO:
    """
    A collection of functions that groups input and output functions in the script
    ChangeLog:
    Caitlyn M, 05 Mar 2025, Created class
    """

    @staticmethod
    def output_error_messages(message :str, exception: Exception = None):
        """
        This function displays an error message to the user
        ChangeLog:
        Caitlyn M, 05 Mar 2025, Created class
        """
        print(message)
        if exception is not None:
            print("-- Technical Error Message -- ")
            print(exception, exception.__doc__, type(exception), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu
        ChangeLog:
        Caitlyn M, 05 Mar 2025, Created class
        """
        print() # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """
        This function displays the menu choices
        ChangeLog:
        Caitlyn M, 05 Mar 2025, Created class
        :return: String with the users choice
        """
        try:
            menu_choice = input("What would you like to do: ")
            if menu_choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return menu_choice


    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays the students first and last name
        and the course name.
        ChangeLog:
        Caitlyn M, 05 Mar 2025, Created class
        :param student_data: List of dictionary rows to be displayed
        :return: List
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                f'{student["LastName"]} is enrolled in {student["Course"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function allows for user input.
        ChangeLog:
        Caitlyn M, 05 Mar 2025, Created class
        :param student_data: List of dictionary rows from input data
        :return: List
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "Course": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="Invalid Data Type")
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.")
        return student_data


# End of Class Definitions


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:
    # Present the menu of choices
    IO.output_menu(menu = MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")