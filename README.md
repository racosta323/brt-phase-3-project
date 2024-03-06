# Travel CLI + ORM Application

## Overview

*The Travel CLI + ORM application is a command-line interface tool with an integrated Object-Relational Mapping (ORM) system designed to help users organize and compare travel information effortlessly. Users can input details about their trips and those of their friends, allowing for easy management and comparison of travel plans.*


---

## Features

- User-friendly CLI Interface: Enjoy a simple and intuitive command-line interface that guides users through the process of entering travel information.
- ORM Integration: Leverage the power of the Object-Relational Mapping system to efficiently store and retrieve travel data from the database.
- Trip Entry and Comparison: Easily input details about your trips and those of your friends, and compare the travel plans side by side for better coordination.

---

## CLI

- **Main Menu: The main menu offers the following options:**
  - *See all travels:* Display a list of all the trips created by the user.
  - *Entering data:* Provides options to add, update, or delete trip records.
  - *Show all user locations:* Display the user's saved locations.
  - *See all friends travels:* Display the travel plans of the user's friends.

- **User Details:** Users are prompted to enter their name and age upon starting the application.
- **Nested Menus:** Users can navigate through nested menus to access various functionalites.
- **Data Persistence:** Users will always find themselves in menus unless they decide to exit the application on their own, ensuring data persistence throughout their session.
- **Exit the Application:** Users can exit the application by typing '0' in any menu prompt.

To set up the application, follow these steps:

1. Install the required packages using Pipenv: `pipenv install`
2. Enter the virtual environment using Pipenv shell: `pipenv shell`
3. Run the CLI by executing: `python lib/cli.py`

==Remember to encourage users to reset all tables before beginning: `print("5. Reset all tables (removes information)")`This will ensure a clean slate for users to start entering their travel information.==
---


## Trip

The trip.py file contains the code for the Trip class, which represents a single travel event with attributes such as month, year, stars, location_id, and traveler_id. The class uses SQLite as the underlying database, storing information in a table named 'trips'.

- **The Trip class has the following features and methods:**
   - *Find Methods:* This class provides 'find_by_id' method to search for records based on the trip's unique ID
   - *Join Queries:* This class provides methods to retrieve trip data joined with traveler and location data, such as 'get_all_by_visit', 'older_friends', and 'younger_friends'.
   - *CRUD Operations:* This class supports Create, Read, Update, and Delete (CRUD) operations for managing records in the 'trips' table.
   - *Data Validation:* This class validates input data to ensure that month, year, stars, location_id and traveler_id attributes are valid.
   - *Database Management:* This class manages a local SQLite database with 'trips' table, storing and retrieving records as needed.
   - *Data Persistence:* This class maintains a dictionary 'all' of all Trip instances, allowing for easy access to data throughout the application's lifetime.
---


## Location

The location.py file contains the code for the Location class. The 'Location' class is designed to represent geographical locations with attributes such as city, state, and country. It uses SQLite as the underlying database, storing information in a table named 'locations'.

- **The Location class has the following features and methods:**
    - *Find Methods:* This class provides 'find_by_id' and 'find_by_city' methods to search for records based on the location's unique ID or city name.
    - *Database Management:* This class manages a local SQLite database with a 'locations' table, storing and retrieving records as needed.
    - *Data Validaton:* This class validates input data to ensure that city, state, and country attributes are strings.
    - *CRUD Operations:* The class supports Create, Read, Update, and Delete (CRUD) operations for managing records in the 'locations'table.
    - *Data Persistence:* The class maintains a dictionary 'all' of all Locations instances, allowing for easy access to data throughout the application's lifetime.

---

## Traveler

The traveler.py file contains the code for the Traveler class, which represents a traveler with attributes such as name and age. The class uses SQLite as the underlying database, storing information in a table named 'travelers'.

- **The Traveler class has the following features and methods:**
    - *Find Methods:* This class provides 'find_by_id' and 'find_by_name' methods to search for records based on the traveler's unique ID or name.
    - *Database Management:* This class manages a local SQLite database with a 'travelers' table, storing and retrieving records as needed.
    - *Data Validaton:* This class validates input data to ensure that name and age attributes are valid.
    - *CRUD Operations:* The class supports Create, Read, Update, and Delete (CRUD) operations for managing records in the 'travelers'table.
    - *Data Persistence:* The class maintains a dictionary 'all' of all Locations instances, allowing for easy access to data throughout the application's lifetime.
    - *Join Queries:* This class provides a method to retrieve travel data joined with trip and location data, such as 'get_all_travels_by_name'.
---

## Contributors

Rene Acosta
Batsheva Parshan
TaKeya McFadden

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Enterprised DNA Blog](https://blog.enterprisedna.co/how-to-sort-a-list-alphabetically/)
- [Tutorials Teacher](https://www.tutorialsteacher.com/python/classmethod-decorator#google_vignette)
