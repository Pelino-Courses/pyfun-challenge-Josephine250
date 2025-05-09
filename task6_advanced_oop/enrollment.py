from typing import List
from student import Student # import the Student class from student
from course import Course # import the Course class from course
from instructor import Instructor # import the Instructor class from instructor

class Enrollment:
    """this class represent the enrollment relationship between students and courses.
    it allows to enroll students in courses and view the enrolled students in a course.
    """
    def __init__(self):
        self.student_courses: dict[Student, List[Course]] = {} # this is a dictionary to store the courses of each student

    def enroll(self, student: Student, course: Course):
        """Enroll a student in a course.
        raises:
            ValueError: if the student is already enrolled in the course.
        """
        if student not in self.student_courses: # check if the student is not in the dictionary
            self.student_courses[student] = [] # add the student to the dictionary with an empty list of courses
        if course in self.student_courses[student]:
            raise ValueError(f"{student.name} is already enrolled in {course.course_code}.")
        else:
            self.student_courses[student].append(course)
            course.add_student(student) 

    def get_courses(self, student: Student) -> List[Course]:
        """this method returns the list of courses the student is enrolled in.
        """
        return self.student_courses.get(student, []) # return the list of courses for the student or an empty list if not found
    def get_students(self, course: Course) -> List[Student]:
        """this method returns the list of students enrolled in the course.
        """
        return list(course.enrolled_students) # return the list of students enrolled in the course
    def __str__(self):
        """this method returns a string summary of all enrollments.
     """
        summary = []
        for student, courses in self.student_courses.items():
            course_list = ', '.join(course.course_code for course in courses) # create a list of course codes for the student
            summary.append(f"{student.name}: {course_list}")
        return "\n".join(summary)
    
s1 = Student("Yvette","REG22446")
s2 = Student("Fiette","REG22447")
lecture = Instructor("Duhawumugisha", 13,"D001")

course1 = Course("PYHON2025", "Python Programming", 3, lecture)
course2 = Course("MATH2025", "Mathematics for Engineer", 4, lecture)

enrollment = Enrollment()
enrollment.enroll(s1, course1)
enrollment.enroll(s1, course2)
enrollment.enroll(s2, course1)
print("Enrollment Summary:\n", enrollment) 