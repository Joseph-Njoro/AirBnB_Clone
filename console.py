#!/usr/bin/python3
"""
This is a sample Python script to demonstrate pycodestyle compliance.
"""

def greet_user(username):
    """
    This function greets the user by their username.
    """
    print(f"Hello, {username}!")

def add_numbers(num1, num2):
    """
    This function adds two numbers and returns the result.
    """
    return num1 + num2

def main():
    """
    Main function to demonstrate usage.
    """
    greet_user("Alice")
    result = add_numbers(5, 3)
    print("The result of adding 5 and 3 is:", result)

if __name__ == "__main__":
    main()