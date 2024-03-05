from __init__ import CONN, CURSOR

class Location:

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
            CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            city TEXT,
            state TEXT,
            country TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS locations;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_instance(cls, city, state, country):
        instance = cls(city, state, country)
        cls.add_to_db(instance)    
        return instance
    
    @classmethod
    def instance_from_db(cls, row):
        location = cls.all.get(row[0])
        if location:
            location.city = row[1]
            location.state = row[2]
            location.country = row[3]
            location.id = row[0]
            return location
        else:
            new_location = cls(row[1], row[2], row[3], row[0])
            cls.all[new_location.id] = new_location
            return new_location
        
    @classmethod
    def get_all_from_db(cls):
        sql = """
            SELECT * FROM locations;
        """  
        rows = CURSOR.execute(sql).fetchall()
        row_list = [cls.instance_from_db(row) for row in rows]
        if row_list:
            return row_list
        else:
            raise ValueError("Table does not have any data")

    ## sql/attr methods

    def add_to_db(self):
        Location.create_table()
        sql = """
            INSERT INTO locations (city, state, country)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.city, self.state, self.country))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update_row(self):
        sql = """
            UPDATE locations
            SET city = ?, state = ?, country = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.city, self.state, self.country))
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

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM locations
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else LookupError("Record not found: ID not in database")    

   ## attr methods     

    def __init__(self, city, state, country, id = None):
        self.city = city
        self.state = state
        self.country = country
        self.id = id
        
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        if isinstance(new_city, str):
            self._city = new_city
        else:
            raise TypeError("City must be a string")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        if isinstance(new_state, str):
            self._state = new_state
        else:
            raise TypeError("State must be a string")

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_country):
        if isinstance(new_country, str):
            self._country = new_country
        else:
            raise TypeError("Country must be a string")

    def __repr__(self):
        return f"<Location_id {self.id}: city ={self.city}, state={self.state}, country={self.country}>"