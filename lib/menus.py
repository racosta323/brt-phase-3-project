from helpers import (
    create_trip,
    exit_program,
    my_travels,
    trips_by_country,
    trips_by_stars,
    trips_by_state,
    update_month,
    update_year,
    update_stars,
    update_all,
    remove,
    all_friends_visits,
    older_friends,
    younger_friends,
    sort_by_year,
    sort_by_name,
    sort_by_state,
    sort_by_country,
    update_name,
    reset_all
)

def menu():
    print("Please select an option:")
    print("1. Where have you been? (Your travels)")
    print("2. Where have your friends been? (Friends' travels)")
    print("3. Show all travels (you and friends)")
    print("4. Update your name and age.")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        user_menu()
    elif choice == "2":
        friends_menu()
    elif choice == "3":
        show_all_loc_menu()
    elif choice == "4":
        update_name()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def user_menu():
    print("1. Enter a record of a location you've been to")
    print("2. Show locations you've been to by sorting options")
    print("3. Show all locations (both your friends' and yours).")
    print("4. Go back to prior menu")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "1":
        create_trip()
    elif choice == "2":
        show_locations_menu()
    elif choice == "3":
        show_all_loc_menu()
    elif choice == "4":
        menu()    
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def show_locations_menu():
    print("1. Show ALL locations you've been to.")
    print("2. Show locations you've been to BY COUNTRY.")
    print("3. Show locations you've been to BY STATE")
    print("4. Show locations you've been to with X NUMBER OF STARS")
    print("5. Update a location you've been to BY TRIP ID")
    print("6. Remove a location you've been to.")
    print("7. Go back to prior menu")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "1":
        my_travels()
    elif choice == "2":
        try:
            trips_by_country()
        except:
            print("\n No trips by country entered \n")
    elif choice == "3":
        try:
            trips_by_state()
        except:
            print("\n No trips by state entered \n")
    elif choice == "4":
        try:
            trips_by_stars()
        except:
            print("\n No trips by stars entered \n")
    elif choice == "5":
        user_trip_update()
    elif choice == "6":
        remove()
    elif choice == "7":
        user_menu()    
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def show_all_loc_menu():
    print("1. Show ALL places, sorted by visit month (asc)")
    print("2. Show ALL places, sorted by visit year (asc)")
    print("3. Show ALL places, sorted alphabetically by name")
    print("4. Show ALL places,sorted alphabetically by state.")
    print("5. Show ALL places, sorted alphabetically by country.")
    print("6. Go back to prior menu")
    print("7. Reset all tables (removes information)")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "1":
        try:
            from trip import Trip
            Trip.get_all_by_visit()
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "2":
        try:
            sort_by_year()
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "3":
        try:
            sort_by_name()
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "4":
        try:
            sort_by_state()
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "5":
        try:
            sort_by_country
        except:
            print("\n No trips. \n Enter a trip through the 'Where have you been?' menu to create table. \n")
    elif choice == "6":
        user_menu()
    elif choice == "7":
        print("\n Resetting will remove all data. There is NO turning back. \n Are you sure you want to remove data? \n")
        confirmation = input("Y/N:> ")
        if confirmation == "Y":
            reset_all()
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to menu item")

def friends_menu():
    print("1. Where have your friends been? THIS WILL GIVE ALL (minus you).")
    print("2. Where have friends older than you been?")
    print("3. Where have friends younger than you been?")
    print("4. Go back to prior menu")
    print("0. Exit the program")
    choice = input("> ")
    if choice == "1":
        try:
            all_friends_visits()
        except:
            print("\n Friends do not have any visits. Have them add some! \n")
    elif choice == "2":
        try:
            older_friends()
        except:
            print("\n Friends do not have any visits. Have them add some! \n")
    elif choice == "3":
        try:
            younger_friends()
        except:
            print("\n Friends do not have any visits. Have them add some! \n")
    elif choice == "4":
        menu()
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice -- enter number corresponding to the menu item")

def user_trip_update():
    print("1. Update month")
    print("2. Update year")
    print("3. Update stars")
    print("4. Update all")
    print("5. Go back to prior menu")
    print("0. Exit the program")
    choice = input("> ")
    if choice == 1:
        update_month()
    elif choice == 2:
        update_year()
    elif choice == 3:
        update_stars()
    elif choice == 4:
        update_all()
    elif choice == 5:
        show_locations_menu()    
    elif choice == 0:
        exit_program()
    elif choice == 4:
        pass
        print("Invalid choice -- enter number corresponding to menu item")
