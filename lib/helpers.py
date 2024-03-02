def greeting():
    name = input("What is your name? ")
    age = input("How old are you? ")
    while name and age:
        print(f'Hello, {name}! Nice to meet you.')
        name = False
        

def exit_program():
    print("Until next time, Traveler!")
    exit()

