from __init__ import CONN, CURSOR


class Location:

    #using faux data for now; later switch to empty dict
    all = {}

    def __init__(self, city, state, country, id = None):
        self.city = city
        self.state = state
        self.country = country
        self.id = id

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


    def __init__(self, city, state, country, id = None):
        self.city = city
        self.state = state
        self.country = country
        self.id = id
        #added temporarily
        Location.all[self.id] = self

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        if isinstance (new_city, str):
           self._city = new_city
        else:
            raise TypeError("City must be a string")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        if isinstance (new_state, str):
           self._state = new_state
        else:
            raise TypeError("State must be a string")

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_country):
        if isinstance (new_country, str):
           self._country = new_country
        else:
            raise TypeError("Country must be a string")


    def __repr__(self):
        return f"<Location_id {self.id}: city ={self.city}, state={self.state}, country={self.country}>"

    def create():
        pass

    def delete():
        pass

    def get_all():
        pass

    def find_by_id():
        pass


