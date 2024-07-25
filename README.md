# Python Calculator: A Beginners Project

Hello and welcome! This document will contain everything you will need to know about the conception, design, and creation of the snazziest calculator out there, the infamous Python Calculator!

## The Why?

It all begins with a humble programming enthusiast, a hunger for knowledge, and a thirst for technical experience & expertise. With little prior experience working through the entirety of a project and keeping relevant, well-documented step-by-step procedures, the simple challenge of developing The Python Calculator proved to be the perfect first step in my journey through the realm of data projects.

## What to Expect From This Document

The contents of this document contain the following:

- **Design Phase**: This takes place before the build of our program. We will talk a little about the expectations I have going into the project, the desired requirements for functionality, and a general overview of the program architecture.
- **How to Use Python Calculator**: This will contain everything you need to know if you want to run Python Calculator on your own computer!
- **Challenges**: This section will discuss some challenges I faced, what I did to overcome them.
- **Technical Insights**: For all you nerds out there! This section will talk about technical considerations.
- **The Final Version**: During this section, we will discuss the end product, some expectations that did not turn out as planned, and all the lessons I learned on the way.
- **Conclusion**: Here you will find a summary of the project, how you can contribute, as well as new things I will work on in the future.

## Significance

The reasons I chose this to be my first project are as follows:

- **Simplicity**: Start small, iterate, and accumulate. As the ancient Chinese proverb says, “Walk slowly and you will walk far!”
- **Documentation**: As it is the first time documenting my work, this will stand as an outline for further projects to come. It will be a great blueprint to expand and build upon.
- **Practice**: Keeping the objective clear leaves focus and attention on the process of project work, opposed to getting caught in a web of technical pondering.

## Design Phase - Pre Build

### Project Overview

**Project Statement and Scope**: The goal of this project is to develop a simple program able to perform the basic functions of an arithmetic calculator. This process will require the implementation of several fundamental python programming techniques such as: Handling user input, use of variables and conditional statements, and error checking, such as dividing by zero.

**Objective**: The objective of this project is to apply the python concepts mentioned above to perform calculations and in turn display the results.

### Tools

Seeing as this is a Python Calculator, the only tool needed for this project is Python!

### Functional Requirements

The Python Calculator must be able to:

- Perform simple arithmetic
- Handle User Input
- Handle Input Errors

### Non-Functional Requirements

The Python Calculator should:

- Have a clean and easy to read aesthetic
- Should act as a standalone application that can be used repeatedly without rerunning code
- Have intuitive commands such as resets and exiting
- Uncluttered code built with the potential of expansion and modification in mind.

### Design and Architecture

**Basic Flow**: Ask for a number, ask for an operator, ask for another number, produce a result. Be able to reset to the beginning or exit at any point.

**Code**: Import any required libraries, followed by defining any functions such as clearing terminal/reset function, and lastly the main logic of the program.

**User Input**: Create a loop which continuously asks for user input after every output, only exiting upon instruction. (`while True` / `break`)

**Error Handling**: A solution for error handling will be to use `try` / `except` and if functions.


This covers the design phase of the project. Next, we will cover how to use the finished product, how I arrived at the completion of said product, and what I learned during the process of creating it.


## How to Use Python Calculator

**Prerequisites**: Python needs to be downloaded on your computer.

**Installation**: Download `calculator.py` (Found in the Files repository)

Now using the Command Prompt on Windows or Terminal on macOS and Linux navigate your way to the directory (File) containing your downloaded `calculator.py`. From here you can type in the following command:

```bash
python calculator.py
```

You should now see a welcome message and instructions on how to use Python Calculator: 

```bash
Welcome to your calculator! Press Enter to continue....                                         
```

### Congratulations! 

You were able to download, locate and run Python Calculator! 

### How to use Python Calculator
- **Introduction** : The calculator is very simple and will guide you through its reset and exit commands, just press enter to cycle through the introduction.
- **c to reset and q to quit** : c will reset the current calculation, q will quit the program. 
- **Invalid Inputs** : Python Calculator will not except any characters that are non-numbers or are not apart of the specified operators [+, -, *, /]

### Here’s an example:
**Inputs** :
```bash
Enter a number: 50
Enter an operator: 50 [+, -, *, /] +
Enter another number: 100
```
**Results in** :
```bash
50 + 100 = 150
Enter a number: 
```

In the example we sum up the values 50 and 100. Once the calculator produces the result of 150, it awaits input for its next calculation! Neat right?


## Challenges - Post Build

We will now discuss some of the challenges I faced when building the Python Calculator. I will explain the iterations Python Calculator went through, some of the problems I faced, and what adjustments I made to overcome them, as well as the decision process behind the format and code itself.

Before we begin, I thought it worth mentioning, whether you’re a technical wizard or somebody who doesn’t code at all, I will try my best to explain everything as simply as possible. However, if you would prefer to skip to the conclusion click [here](#the-final-version).

### Breakdown

Here's what this section will cover:

- **Initial Design**: Overview of the first rendition of Python Calculator
- **Welcome Message**: An issue I faced with the welcome message and a workaround.
- **Further Refinements / Functions**: We next go over some refinements we made by adding functions!
- **Handling Errors / Validating Inputs**: We next go over how Python Calculator deals with errors and invalid inputs.
- **Resetting the Loop**: Here we will discuss the biggest challenge I faced when making Python Calculator.

### Initial Design

Glance over the code. Notice we ask the user for a number (Enter a number:), an operator (Enter an operator:), another number (Enter another number:), then depending on the operator performs a certain calculation and prints the result back to the user. For instance if the operator is a + than it would run : {if user_input2 == '+': print(f"{user_input1} + {user_input3} = {user_input1 + user_input3}") }

```python
print("Welcome to your calculator! \nI can perform any basic arithmetic calculation for you! \nEnter 'c' to clear \nEnter 'q' to quit")

while True:
    user_input1 = input("Enter a number: ")
    if user_input1.lower() == 'q':
        print("Goodbye!")
        exit()
    elif user_input1.lower() == 'c':
        continue
    user_input2 = input(f"Enter an operator: {user_input1} [+, -, *, /]")
    if user_input2.lower() == 'q':
        print("Goodbye!")
        exit()
    elif user_input2.lower() == 'c':
        continue

    user_input3 = input(f"Enter another number: {user_input1} {user_input2} ")
    if user_input3.lower() == 'q':
        print("Goodbye!")
        exit()
    elif user_input3.lower() == 'c':
        continue

    try:
        user_input1 = int(user_input1)
        user_input3 = int(user_input3)
    except ValueError:
        print("That's not a valid number!")
        continue

    if user_input2 == '+':
        print(f"{user_input1} + {user_input3} = {user_input1 + user_input3}")
    elif user_input2 == '-':
        print(f"{user_input1} - {user_input3} = {user_input1 - user_input3}")
    elif user_input2 == '*':
        print(f"{user_input1} * {user_input3} = {user_input1 * user_input3}")
    elif user_input2 == '/':
        try:
            print(f"{user_input1} / {user_input3} = {user_input1 / user_input3}")
        except ZeroDivisionError:
            print("You can't divide by zero!")
    else:
        print("That's not a valid operator!")
```
Notice the except ZeroDivisionError: Code.  
This checks for an error related to dividing by zero. < 

So, what do you think of our first attempt at creating a python calculator! Nice colours am I right?


### Problem 1 - Welcome Message

The initial design performs the basic functionality we were aiming for. However, when we run the program, we encounter a few problems: it's clunky and lacks a clean and intuitive user experience. 

### Issue Description

Upon starting the program, users are greeted with a welcome message. This message, although functional, did not meet our standards for clarity and user engagement. The text was not only visually unappealing but also failed to guide the user effectively through the initial interaction process.

### Initial Welcome Message

Here's what the initial welcome message looked like:
```bash
Welcome to your calculator!
I can perform any basic arithmetic calculation for you!
Enter 'c' to clear
Enter 'q' to quit
```
Eww yuck!

With just a few adjustments to our code, we are able to clean up the welcome messages! Now they look like this:
```bash
Welcome to your calculator! Press Enter to continue...
```
Ooh nice!

### Result
The code now allows for a set of interactive welcome messages and instructions to the calculator, only requiring the user to hit enter to clear the previous code and move on to the next message.

If you’re interested in the code, or you’re a nerd like me, here it is:
```python
input("Welcome to your calculator! Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')


input("I can perform any basic arithmetic calculation for you! Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')


input("Enter 'c' to clear. Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')


input("Enter 'q' to quit. Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')
```

### Further Refinements - Defining Functions 
The last adjustment was definitely an improvement but the code could be cleaned up a little, it seemed appropriate to define functions for any repetitive lines of code.


### Clearing Terminal 
We define a function called **clear_terminal** which now will run the following code anytime is is called:
```python
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
```

**Result**
Look at how much easier our code is to understand : 
```python
input("Welcome to your calculator! Press Enter to continue...")
clear_terminal()

input("I can perform any basic arithmetic calculation for you! Press Enter to continue...")
clear_terminal()


input("Enter 'c' to clear. Press Enter to continue...")
clear_terminal()


input("Enter 'q' to quit. Press Enter to continue...")
clear_terminal()
```


### Handling Errors:
Remember how we addressed division by zero errors with the use of a try / except statement. There were still other input errors I needed to account for so to keep things quick and simple I defined a function that could be applied to any error that came up.
```python
def print_error(message):
    print(message)
    time.sleep(2)
    clear_terminal()
```
Notice the  time.sleep(2) . Without it the terminal would clear before the message can be read.

### Handling Commands c and q:
In order to create clean get_input functions, we needed to separate the command handling logic into its own function. We will talk more about this in the Resetting the Loop Section.
```python
def handle_commands(user_input):
    if user_input.lower() == 'q':
        print("Goodbye!")
        exit()
    elif user_input.lower() == 'c':
        clear_terminal()
        return True
    return False
```

### Validating Inputs:
Aside from our ‘clear’ and ‘quit’ commands, the types of inputs Python Calculator should receive are numbers and operators. I defined functions to generalise these two types of inputs. Notice 
that it uses the handle_commands function to check for c or q. <
```python
def get_input1(prompt):
    while True:
        user_input = input(prompt)
        if handle_commands(user_input):            <
            return None
        try:
            return int(user_input)
        except ValueError:
            print_error("That's not a valid number!")
def get_input2(prompt):
    while True:
        user_input = input(prompt)
        if handle_commands(user_input):            <
            return None
        if user_input not in ['+', '-', '*', '/']:
            print_error("That's not a valid operator!")
            continue
        return user_input
```


### Resetting the Loop

We have now reached the final and most challenging hurdle of creating Python Calculator. It's fitting that one of the most seemingly simple functions of the calculator evidently turned out to be the tallest mountain we would have to climb. That’s right people, our beloved “Enter c to Clear” Command, was Python Calculator’s everest.

Without forcing you to read through every iteration of code and every feeble attempt to fix this problem I will explain to you the issue I was facing and the solution I found that taught me a lot about loops in Python. 

### The Issue 
For some reason no matter how I spun it, there would always be some sort of output or functionality problem with resetting the calculator on the third input. I will show you two examples. 

Notice where the user inputs c : 
It would not let the user enter c because ‘c’ is not a valid number
```bash
Enter a number: 40
Enter an operator: 40.0 [+, -, *, /] +
Enter another number: 40.0 + c      
That’s not a valid number!
```



It would clear the lines but would not reset the calculator to the first input. 
```bash
Enter a number: 40
Enter an operator: 40.0 [+, -, *, /] +
Enter another number: 40.0 + c      
Cleared!
```

Would result in:
```bash
Enter another number: 40.0 +
```


### How did I solve this?
I knew I had to find a way to loop to the top of the program however the Python language does not provide a way to hop to a designated location in code. There is a way to mimic this behaviour though.

### Function main() 
I was trying to use if / elif / else commands, when really I should have been using a function. For all you non code folk out there, it was as if I was trying to scale mount everest without a map. By creating a function, I now had somewhere to point to every time the user typed ‘c’. 

By inputting ‘c’, the main() function is called and functionally this restarts the calculator. Essentially main () is a loop that resets every time the user hits ‘c’. 

Check out Python Calculator’s Map:
```python
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
```
Wow, so cool!

## The Final Version

Adhering to all our Design Requirements, the final version of the Python Calculator works as follows:

- **Main Logic**: The main logic of the program is handled by the `main()` function.
- **User Interaction**: It allows the user to input two numbers and an operator, calculates the result by applying the operator to the numbers, then prints the result.
- **Error Handling**: It also accounts for errors by handling user input and checking for `ZeroDivisionErrors`.
- **Command Handling**: We utilize the `handle_commands` function to allow the user to restart the calculation or quit at any time.

### Key Decisions + Learning Points

A few lessons and key turning points I encountered during this project are as follows:

- **Using Functions**: It didn’t take long for the code to look cluttered. Although, at the outset it seemed that this program would only require easy `if` / `else` logic, defining even simple functions kept the code readable and easy to manage.
- **Refactoring with `main()`**: The readability of the code as well as the command functions were hinged by the use of our `main()` function. Seeing as this was not a part of the initial plan, it proved to be a huge learning point with regards to the application of loops and resetting functionality.

## Future Work

In order to enhance the utility of the Python Calculator, I’ve considered adding these advanced mathematical capabilities:

- **Scientific Calculations**: Incorporating functions like sine, exponential, and logarithmic calculations.
- **Statistical Calculation**: In order to cater to the data science crowd, adding calculations like mean, medium, standard deviation, and variance would allow for statistical analysis.

**Adding a Graphical User Interface (GUI)**: 
To make the calculator more accessible and user-friendly, I aim to integrate a GUI. This will enable users to interact with the calculator through buttons and text fields, improving user experience.

## Contributions

Contributions are welcome! There are many ways you can contribute to this project:

- **Reporting Bugs**: If you find a bug, please open an issue in the GitHub repository, providing a detailed description of the bug and, if possible, steps to reproduce it.
- **Suggesting Enhancements**: Have ideas on how to improve the calculator? Open an issue to suggest new features or enhancements.
- **Submitting Pull Requests**: Feel free to fork the repository and submit pull requests with bug fixes or feature additions.

Please adhere to the following steps for your contributions to be considered:
- Fork the repository and create your branch from `main`.
- If you've added code, ensure it is well documented and tested.
- Ensure your commit messages clearly describe the changes.
- Open a pull request with a clear title and description.

For more information on how to contribute, please read the [CONTRIBUTING.md](https://github.com/EmiliosRichards/Beginner-Project-Python-Calculator/blob/main/CONTRIBUTING.md) guide in our repository.

### Licence

This project is licensed under the MIT License - see the [LICENSE]([LICENSE_FILE_LINK](https://github.com/EmiliosRichards/Beginner-Project-Python-Calculator/blob/main/LICENSE)) file for details.

### Contact Information

If you have any questions or comments about the project, or if you're interested in contributing, feel free to reach out:

- **Project Maintainer**: Emilios Richards
- **Email**: emiliosmrichards@gmail.com
- **GitHub Profile**: [EmiliosRichards](https://github.com/EmiliosRichards)

### References

- **Python Official Documentation**: The Python documentation (https://docs.python.org/3/) was invaluable for understanding the standard libraries and functions.
- **Stack Overflow**: Various threads and discussions on Stack Overflow (https://stackoverflow.com/) provided solutions and insights for specific programming challenges encountered during the development of the project.
- **GitHub Docs**: The GitHub documentation (https://docs.github.com/en) was a guide for using Git and GitHub for version control and project management, ensuring best practices in code sharing and collaboration.
