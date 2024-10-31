#!/usr/bin/env python3
import sys

def is_valid_name(name):
    return name.isalpha() and name[0].isupper()  

def greet_names(names):
    errors = []
    greetings = []

    for name in names:
        if is_valid_name(name):
            greetings.append(f"Hello, {name}!")
        else:
            
            errors.append(name)   

    return greetings, errors

def write_errors_to_file(errors, filename):
    with open(filename, 'w') as file:
        for error in errors:
            
            file.write(f"Error: invalid name '{error}'.\n")

def greet_user():
    while True:
        try:
            name = input("Enter your name: ").strip()
            if is_valid_name(name):
                print(f"Hello, {name}!")
            else:
                print(f"Error: invalid name '{name}'.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit()

def main():
    if len(sys.argv) > 1:  
        with open(sys.argv[1], 'r') as file:
            names = file.read().strip().splitlines()
        
        greetings, errors = greet_names(names)

        for greeting in greetings:
            print(greeting)

        if errors:
            # Записываем ошибки в файл
            write_errors_to_file(errors, 'errors.txt')
    else:
        greet_user()

if __name__ == "__main__":  
    main()




