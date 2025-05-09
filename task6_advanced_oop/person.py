from abc import ABC, abstractmethod
"""" this is a module for defining a Person class and its subclasses.
"""

class NameDescriptor:
    """A descriptor to manage and validate name attributes."""
    def __set_name__(self, owner, name): # set the internal name of the attribute
        self.private_name = f"_{name}"
    def __get__(self, instance, owner):
        return getattr(instance, self.private_name) # return the stored name.
    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip(): # check if the value is a string and not empty.
            raise ValueError(f"{self.name} must be a string and not empty.")
        setattr(instance, self.private_name, value.strip().title()) # set the name to title case.

class Person(ABC):
    """Abstract base class for people in university like students, instructors,...
    Attributes:
        name (str): full name of the person.
        id_number (str): unique identifier for the person.
        
    
    """
    name = NameDescriptor() # use the descriptor for name validation
    
    def __init__(self, name: str, id_number: str):
        self.name = name
        self.id_number = id_number

    @abstractmethod
    def get_role(self) -> str:
        """Abstract method to get the role of the person and must be implemented by subclasses."""
        pass
    def __str__(self) -> str:
        """String representation of the Person object."""
        return f"{self.get_role()} : {self.name}, ID: {self.id_number}"
    
