#!/usr/bin/env python3

from trip import Trip
from traveler import Traveler
import datetime
import ipdb
from location import Location
from __init__ import CONN, CURSOR

#datetime requires year,month,date: https://www.w3schools.com/python/python_datetime.asp

# from traveler: def __init__(self, full_name, id, age):
tr1 = Traveler("Rene", 1, 35)
tr2 = Traveler("Keya", 2, 25)

l1 = Location("Johnsonville", "South Carolina", "United States", 2)
l2 = Location("Austin", "TX", "US", 1)

Traveler.get_all_from_db()
trip1 = Trip.create_instance("March", 2020, 2, 1, 1)
# trip2 = Trip.create_instance("April", 2019, 2, 2, 1)

# Trip.get_all_by_name("Rene")
ipdb.set_trace()