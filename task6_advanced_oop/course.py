from typing import List
from person import Person # import the Person class from person
from instructor import Instructor # import the Instructor class from instructor

class Credit:
    """this is a descriptor class to validate the credits of a course and credits must be postive.
    """

    def __set_name__(self, owner, name): # set the internal name of the attribute
        self.private_name = f"_{name}"

    def __get__(self, instance, owner): # return the stored credits
        return getattr(instance, self.private_name)
    def __set__(self, instance, value): # set the credits and validate it.
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{self.private_name} must be greater than 0.")
        setattr(instance, self.private_name, value) # set the credits to the value.

class Course:
    """this class represent a course in the university system.
        """
    def __init__(self, course_code: str, course_name: str, credits: int, instructor: Person):
        self.course_code = course_code # this is the course code and is unique for each course.
        self.course_name = course_name # this is the name of the course.
        self.credits = credits
        self.instructor = instructor
        self.enrolled_students: List[Person] = [] # this is a list of students enrolled in the course
        self.students: List[Person] = [] # this is used to store the list of students enrolled in the course.

    def add_student(self, student: Person) -> None:
        """this method adds a student in the course if not already enrolled.
        """
        if student not in self.enrolled_students:
            self.enrolled_students.append(student) 
        else:
            raise ValueError(f"{student.name} is already enrolled in {self.course_code}.")
        
    def remove_student(self, student: Person) -> None:
        """this method removes a student from the course if already enrolled.
        """
        if student in self.enrolled_students:
            self.enrolled_students.remove(student) 
        else:
            raise ValueError(f"{student.name} is not enrolled in {self.course_code}.")
        
    def get_enrolled_students(self) -> List[Person]:
        """this method returns the list of enrolled students in the course.
        """
        return self.enrolled_students
    
    def __iter__(self):
        """this method iterate over the enrolled students in the course.
        """
        return iter(self.enrolled_students)
    def __str__(self):
        """String representation of the Course object.
        """
        return f"Code: {self.course_code}, Name: {self.course_name}, Credits: {self.credits}, Instructor: {self.instructor.name}"
        
    @classmethod
    def create_course(cls, course_code: str, course_name: str, credits: int, instructor: Person) -> 'Course':
        """this is a factory method to create a Course object from a dictionary.
        """
        return cls(course_code, course_name, credits, instructor)


Lecture = Instructor("kagabo", "UR2025", "Python ") 
course = Course("PYHON101", "Python Programming", 3, Lecture) # create a course object
print(course) 

newcourse = Course.create_course("WEB101", "Web Development", 4, Lecture)
print("New course information:\n", newcourse)