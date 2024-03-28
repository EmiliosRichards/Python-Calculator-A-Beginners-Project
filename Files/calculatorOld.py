import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

# Print the welcome message and wait for the user to press enter
input("Welcome to your calculator! Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

input("I can perform any basic arithmetic calculation for you! Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

input("Enter 'c' to clear. Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

input("Enter 'q' to quit. Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

# Start an infinite loop for the calculator
while True:
    # Try to get the first number from the user
    try:
        user_input1 = float(input("Enter a number: "))
    except ValueError:
        # If the input is not a valid number, print an error message and clear the terminal
        print("That's not a valid number!")
        time.sleep(2)  # Wait for 2 seconds
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    # Try to get the operator from the user, and handle the quit and clear commands.
    try:
        user_input2 = input(f"Enter an operator: {user_input1} [+, -, *, /] ")
        if user_input2 not in ['+', '-', '*', '/', 'q', 'c']:
            print("That's not a valid operator!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif user_input2 == 'q':
            print("Goodbye!")   
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        elif user_input2 == 'c':
            print("Cleared")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    except ValueError:
        print("That's not a valid operator!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    # Try to get the second number from the user
    try:
        user_input3 = int(input(f"Enter another number: {user_input1} {user_input2} "))
    except ValueError:
        # If the input is not a valid number, print an error message and clear the terminal
        print("That's not a valid number!")
        time.sleep(2)  # Wait for 2 seconds
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    # If the user wants to quit or clear, handle that
    if user_input3 == 'q':
        print("Goodbye!")   
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    elif user_input3 == 'c':
        print("Cleared")
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    # Perform the calculation based on the operator
    try:
        if user_input2 == '+':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{user_input1} + {user_input3} = {user_input1 + user_input3}")
        elif user_input2 == '-':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{user_input1} - {user_input3} = {user_input1 - user_input3}")
        elif user_input2 == '*':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{user_input1} * {user_input3} = {user_input1 * user_input3}")
        elif user_input2 == '/':
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{user_input1} / {user_input3} = {user_input1 / user_input3}")
            except ZeroDivisionError:
                # If the user tries to divide by zero, print an error message and clear the terminal
                print("You can't divide by zero!")
                time.sleep(2)  # Wait for 2 seconds
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            # If the operator is not valid, print an error message and clear the terminal
            print("That's not a valid operator!")
            time.sleep(2)  # Wait for 2 seconds
            os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        # If any other error occurs, print an error message and clear the terminal
        print(f"An error occurred: {e}")
        time.sleep(2)  # Wait for 2 seconds
        os.system('cls' if os.name == 'nt' else 'clear')