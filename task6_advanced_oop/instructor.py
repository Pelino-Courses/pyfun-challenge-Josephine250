from person import Person # import the Person class from person which is base class

class Instructor(Person): 
    """this class represent an instructor in the university system.
    """
    def __init__(self, name: str, id_number: str, department: str):
        """Initialize an Instructor object with name, id_number and department."""
        super().__init__(name, id_number) # call the parent constructor
        self.department = department

    def get_role(self) -> str:
        """ This method is required by the abstract base class Person to identify the role of the person."""
        return "Instructor"
    def addDepartment(self, department: str) :
        """ this method is used to add a department to the instructor. 
        """
        self.department = department
    def __str__(self) -> str:
        """String representation of the Instructor object.
        """
        return f"{self.get_role()} : {self.name}, ID: {self.id_number}, Department: {self.department}"
    
object1 = Instructor("kagabo", "UR2025", "Information Technology")
print(object1)
object1.addDepartment("Mathematics")
print("New department :", object1.department)