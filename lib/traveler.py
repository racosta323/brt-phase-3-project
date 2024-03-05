import ipdb

from __init__ import CONN, CURSOR

#copy class to rename

class Traveler:
    
    all = {}

    ## for testing
    @classmethod
    def reset(cls):
        cls.all = {}
        cls.drop_table()
        cls.create_table()
    ##

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS travelers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS travelers;
        """      
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_instance(cls, name, age):
        instance = cls(name, age)
        instance.add_to_db()
        return instance

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM travelers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else LookupError("Record not found: ID not in database")

    @classmethod
    def instance_from_db(cls, row):
        traveler = cls.all.get(row[0])
        if traveler:
            traveler.name = row[1]
            traveler.age = row[2]
            traveler.id = row[0]
            return traveler
        else:
            new_traveler = cls(row[1], row[2], row[0])
            cls.all[new_traveler.id] = new_traveler
            return new_traveler

    @classmethod
    def get_all_from_db(cls):
        sql = """
            SELECT * FROM travelers
        """
        rows = CURSOR.execute(sql).fetchall()
        list_of_rows = [cls.instance_from_db(row) for row in rows]
        if list_of_rows:
            return list_of_rows
        else:
            raise ValueError("Table does not have any data")  

    def add_to_db(self):
        Traveler.create_table()
        sql = """
            INSERT INTO travelers (name, age)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.age,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM travelers
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else LookupError("Record not found: Name not in database")


    def update_in_db(self):
        sql = """
            UPDATE travelers
            SET name = ?, age = ?
            WHERE id = ?
        """        
        CURSOR.execute(sql, (self.name, self.age, self.id,))
        CONN.commit()

    def delete_from_db(self):
        sql = """
            DELETE FROM travelers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    def __init__(self, name, age, id=None):
        self.name = name
        self.age = age
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string.")
        if not (2 <= len(new_name) <= 50):
            raise ValueError("Name must be between 2 and 50 characters.")
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age is not None:
            if not isinstance(new_age, (int, float)):
                raise TypeError("Age must be a number.")
            if new_age < 0:
                raise ValueError("Age cannot be negative.")
            self._age = new_age
        else:
            raise ValueError("Age must be a non-zero number")

    def __repr__(self):
        return f"<name={self.name}, id={self.id}, age={self.age}>"
    
    ##adding temporarily
    def get_all_travels_by_name(self):
        sql = """
            SELECT trips.id, 
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
            WHERE travelers.name = ?;
        """
        row = CURSOR.execute(sql,(self.name,)).fetchall()
        print(row)
        return row

    def trips_by_stars(self, stars):
        all_trips = self.get_all_travels_by_name()
        print([trip for trip in all_trips if str(trip[6]) >= str(stars)])

    def trips_by_country(self, country):
        all_trips = self.get_all_travels_by_name()
        for trip in all_trips:
            if country == trip[3]:
                print(trip)
                return trip
            else:
                LookupError("No travels by this country")

    def trips_by_state(self, state):
        all_trips = self.get_all_travels_by_name()
        for trip in all_trips:
            if state == trip[2]:
                print(trip)
                return trip
            else:
                LookupError("No travels by this state")

    
        

                
                                

