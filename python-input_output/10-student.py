class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes with those names
        are retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list): List of attribute names to retrieve (default None).
        
        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
