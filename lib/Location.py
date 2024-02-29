class Location:
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def __repr__(self):
        return f"<city ={self.city}, state={self.state}, country={self.country}>"
