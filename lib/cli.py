#!/usr/bin/env python3
from helpers import (
    greeting,
    exit_program,
    menu,
    user_menu,
    friends_menu
)

def main():
    # greeting()
    # while True:
    menu()
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        user_menu()
    elif choice == "2":
        friends_menu()
    else:
        print("Invalid choice -- enter number corresponding to menu item")


    
             
if __name__ == '__main__':
    main()
