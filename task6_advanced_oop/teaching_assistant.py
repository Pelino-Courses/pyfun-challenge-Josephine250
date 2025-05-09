from student import Student
from instructor import Instructor

class TeachingAssistant(Student,Instructor):
    """this class represent a teaching assistant in the university system who is both a student and an instructor and we have multiple inheritance.
    """
    def __init__(self, name: str, student_id: str, instructor_id: str, department: str):
        """Initialize a TeachingAssistant object with both student and instructor roles.
        """
        Student.__init__(self, name, student_id) # call the parent constructor for Student
        Instructor.__init__(self, name, instructor_id, department) # call the parent constructor for Instructor
        self.student_id = student_id
        self.instructor_id = instructor_id

    def __str__(self):
        """String representation of the TeachingAssistant student and instrucor roles.
        """
        return f"Teaching Assistant : {self.name}, Student ID: {self.student_id}, Instructor ID: {self.instructor_id}, Department: {self.department}"
    
object1 = TeachingAssistant("Bayishimire", "REG22446", "Dr22446", "MINING AND GEOLOGY")
print(object1)