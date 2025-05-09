from typing import List, Iterator
from person import Person # import the Person class from person
from course import Course # import the Course class from course even it will be in next codes


class Student(Person):
    """this class represent a student in the university system.
    """

    def __init__(self, name: str, id_number: str):
        """Initialize a Student object with name and id_number."""
        Person.__init__(self,name, id_number) # call the parent constructor
        self.courses : list[Course] = [] # initialize an empty list of courses

    def enroll(self, course: Course) -> None:
        """Enroll the student in a course.
        raises:
            ValueError: if the course is already in the student's course list.
        """
        if course in self.courses:
            raise ValueError(f"{self.name} is already enrolled in {course.course_code}.")
        
        else:
            self.courses.append(course) # add the course to the list of courses

    def remove(self, course: Course) -> None:
        """ remove the student from a course.
        raises:
            ValueError: if the course is not in the student's course list.
        """

        if course not in self.courses:
            raise ValueError(f"{self.name} is not enrolled in {course.course_code}.") # check if the course is not in the list of courses
        
        else:
            self.courses.remove(course) # remove the course from the list of courses
    def __iter__(self) -> Iterator[Course]:
        """ an iterator to iterate over the courses of the student.
        """
        return iter(self.courses)
    def get_role(self) -> str:
        """ This method is required by the abstract base class Person to identify the role of the person."""
        
        return "Student"
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """ this a factory method to create a Student object from a dictionary.
        for instance like  data = {'name': 'Kagabo', 'id_number': 'REG22446'}
        """
        return cls(name = data.get('name'), id_number = data.get('id_number'))
    
object1 = Student("Kagabo", "REG22446")
print(object1)   