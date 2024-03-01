#!/usr/bin/env python3

from Traveler import Traveler
import ipdb

# Create a Traveler instance for testing
test_traveler = Traveler(full_name="John Doe", traveler_id="12345", age=30)

# Print the representation of the Traveler instance
print("Representation of the Traveler instance:")
print(repr(test_traveler))

# Set a breakpoint using ipdb
ipdb.set_trace()

# Access individual attributes
print("\nAccessing individual attributes:")
print(f"Full Name: {test_traveler.full_name}")
print(f"Traveler ID: {test_traveler.traveler_id}")
print(f"Age: {test_traveler.age}")

# Modify attributes
print("\nModifying attributes:")
test_traveler.full_name = "Updated Name"
test_traveler.age = 35
print(repr(test_traveler))

# Additional testing or debugging code can be added as needed
