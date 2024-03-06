#!/usr/bin/env python3
from helpers import (
    greeting,
    exit_program,
)
from menus import (
    menu
)

def main():
    while True:
        greeting()
        menu()
    

             
if __name__ == '__main__':
    main()


