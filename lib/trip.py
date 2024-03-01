import ipdb
from __init__ import CONN, CURSOR

class Trip:

    MONTHS = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}
    all = {}

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS trips (
            id INTEGER PRIMARY KEY,
            month TEXT,
            year INTEGER,
            location_id INTEGER,
            traveler_id INTEGER,
            FOREIGN KEY (location_id) REFERENCES locations(id),
            FOREIGN KEY (traveler_id) REFERENCES travelers(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS trips;
        """      
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_instance(cls, month, year):
        instance = cls(month, year)
        cls.save_to_table(instance)
        return instance
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM trips
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else LookupError("Record not found: ID not in database")
    
    @classmethod
    def instance_from_db(cls, row):
        trip = cls.all.get(row[0])
        if trip:
            trip.month = row[1]
            trip.year = row[2]
        else:
            new_trip = cls(row[1], row[2])
            cls.all[new_trip.id] = new_trip
        return trip

    def save_to_table(self):
        sql = """
            INSERT INTO trips (month, year, id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.month, self.year, self.id,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update_row(self):
        sql = """
            UPDATE trips
            SET month = ?, year = ?
            WHERE id = ?
        """        
        CURSOR.execute(sql, (self.month, self.year, self.id,))
        CONN.commit()

    def destory(self):
        sql = """
            DELETE FROM trips
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def __init__(self, month, year, id = None):
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
        return f'<Trip {self.id}: month={self.month} year={self.year}>'