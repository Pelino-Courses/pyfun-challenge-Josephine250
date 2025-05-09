from student import Student
from course import Course
from instructor import Instructor
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant
from typing import List
from person import Person

def demo():
    """this function demonstrates the functionality of the university system.
    """
    # Create an instructor
    instructor1 = Instructor("Erneste", "prof2025", "Computer Engineering")
    print(f"Instructor: {instructor1.name}, ID: {instructor1.id_number}, Department: {instructor1.department}")

    # Create a course
    course1 = Course.create_course("PY001", "Python Programming", 3, instructor1)
    course2 = Course.create_course("WEB001", "Web Development", 4, instructor1)
    print(f"Course information: \n Code: {course1.course_code}, Name: {course1.course_name}, Credits: {course1.credits}, Instructor: {course1.instructor.name}")
    print(f"Course information: \n Code: {course2.course_code}, Name: {course2.course_name}, Credits: {course2.credits}, Instructor: {course2.instructor.name}")  
     # Create students
    student1 = Student("josephine", "REG22456")
    student2 = Student("peter", "REG22457")
    print(f"Student: {student1.name}, ID: {student1.id_number}\n")
    print(f"Student: {student2.name}, ID: {student2.id_number}\n")

    # Create enrollment system
    enrollment_system = Enrollment()

    # Enroll students in courses
    enrollment_system.enroll(student1, course1)
    enrollment_system.enroll(student1, course2)
    enrollment_system.enroll(student2, course1)

    # Print enrollement summary
    print("Enrollment Summary:")
    for student, courses in enrollment_system.student_courses.items():
        print(f"{student.name}: {', '.join(course.course_code for course in courses)}")

    #create a teaching assistant
    ta1 = TeachingAssistant("Proof josephine", "REG no 22111", "LCT22111", "PYTHON")
    print(f"Teaching Assistant: {ta1.name}, Student ID: {ta1.student_id}, Instructor ID: {ta1.instructor_id}, Department: {ta1.department}")

demo()