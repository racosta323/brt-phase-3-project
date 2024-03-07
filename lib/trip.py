from __init__ import CONN, CURSOR

class Trip:

    MONTHS = {
        "january", 
        "february", 
        "march", 
        "april", 
        "may", 
        "june", 
        "july", 
        "august", 
        "september", 
        "october", 
        "november", 
        "december",
        "n/A"
    }

    all = {}

    @classmethod
    def reset(cls):
        cls.all = {}
        cls.drop_table()
        cls.create_table()

   ## sql class methods     
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
        return cls.instance_from_db(row) if row else LookupError("Record not found: ID not in database")
    
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
        sql = """
            SELECT travelers.name,
            locations.city,
            locations.state,
            locations.country,
            trips.month,
            trips.year,
            trips.stars 
            FROM trips
            JOIN travelers
            ON trips.traveler_id = travelers.id
            JOIN locations
            ON trips.location_id = locations.id
            ORDER BY year, month
        """
        rows = CURSOR.execute(sql).fetchall()
        if rows:
            results = [f"(NAME: {result[0]}, CITY: {result[1]}, STATE: {result[2]}, COUNTRY: {result[3]}, MONTH: {result[4]}, YEAR: {result[5]}, STARS GIVEN: {result[6]})" for result in rows]
            return rows
        else:
            raise ValueError("Table does not have any data")

    @classmethod
    def older_friends(cls, age):
        sql = """
            SELECT travelers.name,
            locations.city,
            locations.state,
            locations.country,
            trips.month,
            trips.year,
            trips.stars 
            FROM trips
            JOIN travelers
            ON trips.traveler_id = travelers.id
            JOIN locations
            ON trips.location_id = locations.id
            WHERE travelers.age > ?
            ORDER BY year, month
        """
        rows = CURSOR.execute(sql, (int(age),)).fetchall()
        if rows:
            return rows
        else:
            raise LookupError("Did not return any data; friends older than you have not recorded trips")      

    @classmethod
    def younger_friends(cls, age):
        sql = """
            SELECT travelers.name,
            locations.city,
            locations.state,
            locations.country,
            trips.month,
            trips.year,
            trips.stars 
            FROM trips
            JOIN travelers
            ON trips.traveler_id = travelers.id
            JOIN locations
            ON trips.location_id = locations.id
            WHERE travelers.age < ?
            ORDER BY year, month
        """
        rows = CURSOR.execute(sql, (age,)).fetchall()
        if rows:
            return rows
        else:
            raise LookupError("Did not return any data; friends younger than you have not recorded trips") 
    
    @classmethod
    def find_name_by_id(cls, trav_id):
        from traveler import Traveler
        if trav_id in Traveler.all:
            return Traveler.all[trav_id].name
        else:
            raise Exception

    ## sql attr methods
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
        del type(self).all[self.id]
        self.id = None

    ## attr methods   
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
        if new_month == "N/A":
            self._month = new_month
        elif isinstance(new_month,str):
            if new_month.lower() in Trip.MONTHS:
                self._month = new_month.capitalize()
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
            if new_year == 0:
                self._year = "N/A"
            else:
                self._year = new_year    
        else:
            raise TypeError("Year must be an integer")
        
    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, new_stars):
        if isinstance(new_stars, int):
            if new_stars == 0:
                self._stars = "N/A"
            elif 0 <= new_stars <= 5:
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
        Traveler.get_all_from_db()
        if new_id in Traveler.all:
            self._traveler_id = new_id
        else:
            raise TypeError("Traveler ID must be associated with ID in traveler class")
        
    @property
    def location_id(self):
        return self._location_id

    @location_id.setter
    def location_id(self, new_id):
        from location import Location
        Location.get_all_from_db()
        if new_id in Location.all:
            self._location_id = new_id
        else:
            raise TypeError("Location ID must be associated with ID in location class")        
        
    def __repr__(self):
        return f'<Trip ID: {self.id}: month={self.month}, year={self.year}, stars={self.stars} traveler_id = {self.traveler_id}>'