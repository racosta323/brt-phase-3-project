# traveler.py

class Traveler:

    #using faux data for now; later switch to empty dict
    all = {}

    def __init__(self, name, id, age):
        self._name = None  
        self.name = name
        self._id = id
        self._age = None  
        self.age = age
        #added temporarily
        Traveler.all[self.id] = self  
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Full name must be a string.")
        min_length = 2
        max_length = 50
        if not (min_length <= len(value) <= max_length):
            raise ValueError(f"Full name must be between {min_length} and {max_length} characters.")
        self._name = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value is not None:
            if not isinstance(value, (int, float)):
                raise ValueError("Age must be a number.")
            if value < 0:
                raise ValueError("Age cannot be negative.")
        self._age = value

    def __repr__(self):
        return f"<name={self.name}, id={self.id}, age={self.age}>"
