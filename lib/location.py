class Location:
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

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

    def __repr__(self):
        return f"<city ={self.city}, state={self.state}, country={self.country}>"

    def create():
        pass

    def delete():
        pass

    def get_all():
        pass

    def find_by_id():
        pass
