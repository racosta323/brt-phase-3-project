import ipdb

class Trip:

    MONTHS = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}

    
    def __init__(self, place, month, year, id = None):
        self.place = place
        self.month = month
        self.year = year
        self.id = id
    
    @property
    def month(self):
        return self._month
    
    @month.setter
    def month(self, new_month):
        if isinstance(new_month,str):
            if new_month in Trip.MONTHS:
                self._month = new_month
            else:
                raise ValueError("String must be a month of the year")
        else:
            raise TypeError("Month must be a string")
        
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        if isinstance(new_year, int):
            self._year = new_year    
        else:
            raise TypeError("Year must be an integer")

    def __repr__(self):
        return f'<Trip {self.id}: place={self.place}, date={self.date}>'