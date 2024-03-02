#!/usr/bin/env python3

from trip import Trip
from traveler import Traveler
import datetime
import ipdb
from location import Location
from __init__ import CONN, CURSOR

#datetime requires year,month,date: https://www.w3schools.com/python/python_datetime.asp


# create_instance(cls, month, year, stars, traveler_id)
# trip1 = Trip("March", 2023)
# location1 = Location("Johnsonville", "South Carolina", "United States")

#def __init__(self, full_name, id, age):
t1 = Traveler("Rene", 1, 35)
t2 = Traveler("Keya", 2, 25)


ipdb.set_trace()