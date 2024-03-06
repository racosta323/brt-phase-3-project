#!/usr/bin/env python3
from helpers import (
    greeting,
    exit_program,
)
from menus import (
    menu
)

def main():
    greeting()
    while True:
        menu()
    
if __name__ == '__main__':
    main()


