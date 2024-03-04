# traveler.py
import ipdb

from __init__ import CONN, CURSOR

class Traveler:
    all = {}

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS travelers (
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            traveler_id INTEGER,
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
    def create_instance(cls, full_name, traveler_id, age):
        instance = cls(full_name=full_name, traveler_id=traveler_id, age=age)
        instance.save_to_db()
        return instance

    @classmethod
    def find_by_id(cls, traveler_id):
        sql = """
            SELECT * FROM travelers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (traveler_id,)).fetchone()
        return cls.instance_from_db(row) if row else LookupError("Record not found: ID not in database")

    @classmethod
    def instance_from_db(cls, row):
        traveler = cls.all.get(row[0])
        if traveler:
            traveler.full_name = row[1]
            traveler.traveler_id = row[2]
            traveler.age = row[3]
            traveler.id = row[0]
            return traveler
        else:
            new_traveler = cls(row[1], row[2], row[3], row[0])
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

    def save_to_db(self):
        sql = """
            INSERT INTO travelers (full_name, traveler_id, age)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.full_name, self.traveler_id, self.age))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update_in_db(self):
        sql = """
            UPDATE travelers
            SET full_name = ?, traveler_id = ?, age = ?
            WHERE id = ?
        """        
        CURSOR.execute(sql, (self.full_name, self.traveler_id, self.age, self.id))
        CONN.commit()

    def delete_from_db(self):
        sql = """
            DELETE FROM travelers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # also delete from dict
        del type(self).all[self.id]
        self.id = None

    def __init__(self, name, traveler_id, age, id=None):
        self.name = name
        self.age = age
        self.id = id

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
    
    ##adding temporarily
    def get_all_travels_by_name(self):
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
            WHERE travelers.name = ?;
        """
        row = CURSOR.execute(sql,(self.name,)).fetchall()
        print(row)
        # return row

