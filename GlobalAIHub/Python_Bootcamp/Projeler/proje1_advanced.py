"""
Information about Project
There is 7 teachers: Bengu, Busra, Karamurat, Lutfi, Mert, Ramazan, Ugurcan. (If you want you can change the teachers_list).
You can add different courses. Grade letters: 100-90: A, 89-80: B, 79-70: C, 69-60: D, 59-0: F.
Program takes student name, student surname, school no, course name and exam grade. It keeps the information after entry.
Program shows if student passed or not and prints "Passed" or "Not Passed" the course.
Program can show the grade letter that student took from course's exam.
Program creates a dataframe for passed and not passed students and export to excel.
You can access the dataframe
"""

import pandas as pd


class School_System():
    def __init__(self):
        self.teachers_list = ["Bengu", "Busra", "Karamurat", "Lutfi", "Mert", "Ramazan", "Ugurcan"]
        self.grade_letter_dict = {"A": range(100, 89, -1), "B": range(89, 79, -1), "C": range(79, 69, -1), "D": range(69, 59, -1), "F": range(59, -1, -1)}
        self.students_list = []
    
    def teacher_control(self, teacher_name):
        self.teacher_name = teacher_name
        
    def appending_to_database(self, name, surname, school_id, lesson, exam_grade):
        self.name = name
        self.surname = surname
        self.school_id = school_id
        self.lesson = lesson
        self.exam_grade = exam_grade
        self.students_list.append([self.name, self.surname, self.school_id, self.lesson, self.exam_grade])
        print(f"Student {self.name} {self.surname} is appended by {self.teacher_name} to {self.lesson} course.")
    
    def calculate_grade_letter(self):
        for y in range(len(self.students_list)):
            for i in range(len(list(self.grade_letter_dict.values()))):
                if self.students_list[y][4] in list(self.grade_letter_dict.values())[i]:
                    self.grade_letter = list(self.grade_letter_dict.keys())[i]
                    self.students_list[y].append(self.grade_letter)
                    break
            print(f"Student {self.students_list[y][0]} {self.students_list[y][1]} got {self.grade_letter} from {self.students_list[y][3]} course.")
    
    def passed_not_passed(self):
        for i in self.students_list:
            if i[5] == "F":
                i.append(0)
                print(f"{i[0]} {i[1]} not passed the {i[3]} course.")
            else:
                i.append(1)
                print(f"{i[0]} {i[1]} passed the {i[3]} course.")
                
    def transform_to_dataframe(self):
        columns =["Name", "Surname", "School ID", "Lesson", "Grade", "Exam Letter", "Pass Status"]
        dataframe_dictionary = {}
        for i in range(len(columns)):
            temp_list = [j[i] for j in self.students_list]
            dataframe_dictionary[columns[i]] = temp_list
        self.dataframe = pd.DataFrame(dataframe_dictionary)
        print("Database turned into dataframe.")
        
    def export_excel(self):
        self.dataframe.to_csv("school_database1.csv", sep=",", index=False)
        print("Dataframe exported as csv file.")
    
teachers = School_System()
while True:
    teachers_name = input("Enter your name:").capitalize()
    teachers.teacher_control(teachers_name)
    if teachers.teacher_name in teachers.teachers_list:
        number_of_students = int(input("Enter how many students you append:"))
        for _ in range(number_of_students):
            student_name = input("Enter student's name: ").capitalize()
            student_surname = input("Enter student's surname: ").capitalize()
            student_school_id = int(input("Enter student's school Id: "))
            student_lesson = input("Enter the lesson: ").capitalize()
            student_grade = float(input(f"Enter the student's exam  from {student_lesson} grade: "))
            teachers.appending_to_database(student_name, student_surname, student_school_id, student_lesson, student_grade)

        yes_no = input("Do you want to calculate grade letters? ").capitalize()
        if yes_no == "Yes":
            teachers.calculate_grade_letter()
            yes_no = input("Do you want to see students passed or not passed the courses? ").capitalize()
            if yes_no == "Yes":
                teachers.passed_not_passed()
                yes_no = input("Do you want to transform database to dataframe? ").capitalize()
                if yes_no == "Yes":
                    teachers.transform_to_dataframe()
                    yes_no = input("Do you want to export the dataframe as csv file? ").capitalize()
                    if yes_no == "Yes":
                        teachers.export_excel()
                        break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break
    else:
        print("Wrong teacher name! Please enter right one or contact with IT support.")
