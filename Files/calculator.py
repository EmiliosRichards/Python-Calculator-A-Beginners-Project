import os
import time
import operator

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

# Print the welcome message and wait for the user to press enter
input("Welcome to your calculator! Press Enter to continue...")
clear_terminal()

input("I can perform any basic arithmetic calculation for you! Press Enter to continue...")
clear_terminal()

input("Enter 'c' to clear. Press Enter to continue...")
clear_terminal()

input("Enter 'q' to quit. Press Enter to continue...")
clear_terminal()


def print_error(message):
    print(message)
    time.sleep(2)
    clear_terminal()

def handle_commands(user_input):
    if user_input.lower() == 'q': 
        print("Goodbye!")
        exit()
    elif user_input.lower() == 'c': 
        clear_terminal()
        return True
    return False

def get_input1(prompt):
    while True:
        user_input = input(prompt)
        if handle_commands(user_input):
            return None
        try:
            return int(user_input)
        except ValueError:
            print_error("That's not a valid number!")

def get_input2(prompt):
    while True:
        user_input = input(prompt)
        if handle_commands(user_input):
            return None
        if user_input not in ['+', '-', '*', '/']:
            print_error("That's not a valid operator!")
            continue
        return user_input

def main():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    while True:
        num1 = get_input1("Enter a number: ")
        if num1 is None:
            continue
        op = get_input2("Enter an operator: [+, -, *, /] ")
        if op is None:
            continue
        num2 = get_input1("Enter another number: ")
        if num2 is None:
            continue
        try:
            result = operators[op](num1, num2)
            clear_terminal()
            print(f"{num1} {op} {num2} = {result}")
        except ZeroDivisionError:
            print_error("You can't divide by zero!")
        except Exception as e:
            print_error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()