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
            stars INTEGER,
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
    def create_instance(cls, month, year, stars, location_id, traveler_id):
        instance = cls(month, year, stars, location_id, traveler_id)
        cls.add_to_db(instance)
        return instance
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM trips
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        ipdb.set_trace()
        return cls.instance_from_db(row) if row else LookupError("Record not found: ID not in database")
    
    #find by name when I link to traveler; needs work
    # @classmethod
    # def find_by_name(cls, name):
    #     sql = """
    #         SELECT * FROM trips
    #         WHERE name = ?
    #     """
    #     row = CURSOR.execute(sql, (name,)).fetchone()
    #     return cls.instance_from_db(row) if row else LookupError("Record not found: Name not in database")

    @classmethod
    def instance_from_db(cls, row):
        trip = cls.all.get(row[0])
        if trip:
            trip.month = row[1]
            trip.year = row[2]
            trip.stars = row[3]
            trip.location_id = row[4]
            trip.traveler_id = row[5]
            trip.id = row[0]
            return trip
        else:
            new_trip = cls(row[1], row[2], row[3], row[4], row[5], row[0])
            cls.all[new_trip.id] = new_trip
            return new_trip
    
    @classmethod
    def get_all_from_db(cls):
        sql = """
            SELECT * FROM trips
        """
        rows = CURSOR.execute(sql).fetchall()
        list_of_rows = [cls.instance_from_db(row) for row in rows]
        if list_of_rows:
            return list_of_rows
        else:
            raise ValueError("Table does not have any data")  
    
    @classmethod
    def get_all_by_visit(cls):
        all = cls.get_all_from_db()

    # @classmethod
    # def get_all_by_visit(cls):
    #     sql = """
    #         SELECT travelers.name,
    #         locations.city,
    #         locations.state,
    #         locations.country,
    #         trips.month,
    #         trips.year,
    #         trips.stars 
    #         FROM trips
    #         JOIN travelers
    #         ON trips.traveler_id = travelers.id
    #         JOIN locations
    #         ON trips.location_id = locations.id
    #         ORDER BY year, month
    #     """
    #     rows = CURSOR.execute(sql).fetchall()
    #     if rows:
    #         print(rows)
    #     else:
    #         raise ValueError("Table does not have any data")

    #this method probably shouldn't be in this class, but instead in the Traveler class
    #leaving temporarily to complete other methods, but may consider removing later
    @classmethod
    def find_name_by_id(cls, trav_id):
        from traveler import Traveler
        if trav_id in Traveler.all:
            return Traveler.all[trav_id].name
        else:
            ipdb.set_trace()
            raise Exception
         

    def add_to_db(self):
        Trip.create_table()
        sql = """
            INSERT INTO trips (month, year, stars, location_id, traveler_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.month, self.year, self.stars, self.location_id, self.traveler_id,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    
    def update_row(self):
        sql = """
            UPDATE trips
            SET month = ?, year = ?, stars = ?, location_id = ?, traveler_id = ?
            WHERE id = ?
        """        
        CURSOR.execute(sql, (self.month, self.year, self.stars, self.location_id, self.traveler_id, self.id))
        CONN.commit()

    def destroy(self):
        sql = """
            DELETE FROM trips
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        #also delete from dict
        del type(self).all[self.id]
        self.id = None

    def __init__(self, month, year, stars, location_id, traveler_id, id = None):
        self.month = month
        self.year = year
        self.stars = stars
        self.location_id = location_id
        self.id = id
        self.traveler_id = traveler_id

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
        
    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, new_stars):
        if isinstance(new_stars, int):
            if 0 <= new_stars <= 5:
                self._stars = new_stars
            else:
                raise ValueError("Stars must be an integer between 0 and 5")    
        else:
            raise ValueError("Stars must be an integer")
           
    @property
    def traveler_id(self):
        return self._traveler_id
    
    @traveler_id.setter
    def traveler_id(self, new_id):
        from traveler import Traveler
        if new_id in Traveler.all:
            self._traveler_id = new_id
        else:
            raise TypeError("ID must be associated with ID in traveler class")
        

    @property
    def location_id(self):
        return self._location_id

    @location_id.setter
    def location_id(self, new_id):
        from location import Location
        if new_id in Location.all:
            self._location_id = new_id
        else:
            raise TypeError("ID must be associated with ID in location class")        
        
    def __repr__(self):
        return f'<Trip ID: {self.id}: month={self.month}, year={self.year}, stars={self.stars} traveler_id = {self.traveler_id}>'
    
    ## for testing
    @classmethod
    def reset(cls):
        cls.all = {}
        cls.drop_table()
        cls.create_table()