#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Blaise Konzel, 5/26, created script 
#   Blaise Konzel, 5/26, moved to class-function file structure. 
# ------------------------------------------------------------------------------------------ #
#importing json
import json

# Define the Constants and Variables -------------------
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

#IO class definition -----------------
class IO: 
    
    @staticmethod
    def output_error_messages(message: str, error: Exception):
        '''
        This function outputs error message information for the user if an 
        Exception is thrown. 
        Parameters
        ----------
        message : str
            The error message output to the user.
        error : Exception, optional
            DESCRIPTION. The default is None.
        Returns
        -------
        None.
        '''
        
        print('--', message, '--')
        if error is not None: 
            print('\n---Technical Information---')
            print(error, error.__doc__, type(error), sep='\n')
            print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        '''
        This function prints the menu to screen
        Parameters
        ----------
        menu : str
            string outlining options for user.
        Returns
        -------
        None.
        '''
        print(menu)
        
    @staticmethod
    def input_menu_choice():
        '''
        This function accepts the users input choice and calls the respective 
        function 
        Returns
        -------
        None.
        '''
    
        menu_choice = input('What would you like to do: ')
        if menu_choice == '1': 
            IO.input_student_data(student_data=students)
        # Present the current data
        elif menu_choice == '2':
            IO.output_student_courses(student_data=students)
        elif menu_choice == '3':
            FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        elif menu_choice == "4":
            print('Program Ended.')
            #returns 1 to break function call loop
            return 1
        else:
            print("Please choose options 1, 2, 3, or 4")
    @staticmethod
    def output_student_courses(student_data: list[dict[str,str,str]]):
        '''
        This function takes in the current students lit and prints it to the screen
        Parameters
        ----------
        student_data : list
            list of dictionaries containing student names and courses .
        Returns
        -------
        None.
        '''
        try: 
            print("-" * 50)
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-" * 50)
        except TypeError as e:
            IO.output_error_messages(message= 'JSON empty, No data to Print', error = e)
        
    @staticmethod
    def input_student_data(student_data: list[dict[str,str,str]]):
        '''
        This function allows the user to enter an additional student and course
        to the current list of 'students'
        Parameters
        ----------
        student_data: list[dict[str,str,str]]
            list of dictionaries from json file containing student name and course
        Raises
        ------
        ValueError
            DESCRIPTION.
        Returns
        -------
        student_data : TYPE
            updated list of student names and courses.

        '''
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("\nThe first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            new_student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(new_student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message= 'Unexpected Error', error = e)
        except Exception as e:
            IO.output_error_messages(message= "Error: There was a problem with your entered data.", error = e)
        return student_data 

#FileProcessor Class definition -------------------
class FileProcessor: 
    
    @staticmethod
    def read_data_from_file(student_data: list[dict[str,str,str]], file_name: str):
        '''
        This function reads data from a json file into a list of dictionaries
        Parameters
        ----------
        student_data : list[dict[str,str | float]]
            list of dictionaries json file data is loaded in to.
        file_name : str
            name of file data is taken from. 
        Returns
        -------
        'student_data' as a list of dictionaries 
        '''
        # file: TextIO = None
        try:
            file = open(file_name, "r")
            student_data += json.load(file)
            file.close()
        except Exception as e:
            error_message = "Error: There was a problem with reading the file. \n please check that the file exists and that it is in a json format."
            IO.output_error_messages(message= error_message, error = e)
           
        return(student_data)

    @staticmethod
    def write_data_to_file(student_data: list[dict[str,str,str]], file_name: str):
        '''
        This function writes data a json file. 
        Parameters
        ----------
        file_name : str
            name of file data is written to.
        student_data : list[dict[str,str | float]]
            data written to file. list of dictionaries
        Returns
        -------
        None.

        '''
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
        except UnboundLocalError as e:
            IO.output_error_messages(message= "Error: There was a problem with writing to the file. Please check that the file is not open by another program." , error = e)


#%% running the program 

# populate the 'students' var 
students = FileProcessor.read_data_from_file(student_data=students, file_name=FILE_NAME)

#intialize var to break program loop
loop_breaker = 2
#program containing loop  
while loop_breaker !=1 :
    IO.output_menu(MENU)
    loop_breaker = IO.input_menu_choice()
    











