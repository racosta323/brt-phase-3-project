#!/usr/bin/env python3

from trip import Trip
from traveler import Traveler
import datetime
import ipdb
from location import Location
from __init__ import CONN, CURSOR

#datetime requires year,month,date: https://www.w3schools.com/python/python_datetime.asp


# create_instance(cls, month, year, stars, traveler_id)
# location1 = Location("Johnsonville", "South Carolina", "United States")

# from traveler: def __init__(self, full_name, id, age):
tr1 = Traveler("Rene", 1, 35)
tr2 = Traveler("Keya", 2, 25)

trip1 = Trip.create_instance("March", 2020, 2, 2)
trip2 = Trip.create_instance("April", 2019, 2, 1)

tr1.get_all_by_name()

# Trip.get_all_by_name("Rene")
# ipdb.set_trace()