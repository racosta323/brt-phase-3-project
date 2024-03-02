#!/usr/bin/env python3
from helpers import (
    greeting,
    exit_program 
)

def main():
    while True:
        # greeting()
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


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Where have you been?")
    print("2. Where have your friends been?")

def user_menu():
    print("hello user")
 

def friends_menu():
    print("hello friends")     
             
if __name__ == '__main__':
    main()
