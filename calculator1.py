#This is a simple Calculator, coded in Python
#You can add, subtract, multiply, and divide
#An operation can only be performed between TWO numbers

print("Welcome to the Calculator!")
print("Programmed by @ibrahim")

def add():
    user_input1 = float(input("Please enter the first number: "))
    user_input2 = float(input("Please enter the second number: "))
    total = user_input1 + user_input2
    return total


def subtract():
    user_input1 = float(input("Please enter the first number: "))
    user_input2 = float(input("Please enter the second number: "))
    total = user_input1 - user_input2
    return total


def multiply():
    user_input1 = float(input("Please enter the first number: "))
    user_input2 = float(input("Please enter the second number: "))
    total = user_input1 * user_input2
    return total


def divide():
    user_input1 = float(input("Please enter the first number: "))
    user_input2 = float(input("Please enter the second number: "))
    if user_input2 == 0:
        return "Error: Cannot divide by zero."
    total = user_input1 / user_input2
    return total

operations_list = ['1. Add', 
                   '2. Subtract',
                   '3. Multiply',
                   '4. Divide']

print("Available operations:")
for operation in operations_list:
    print(operation)

user_input = input("Please select an operation from the given list: ").strip().lower()

if user_input == '1' or user_input == 'add':
    print(add())
elif user_input == '2' or user_input == 'subtract':
    print(subtract())
elif user_input == '3' or user_input == 'multiply':
    print(multiply())
elif user_input == '4' or user_input == 'divide':
    print(divide())
else:
    print("Invalid operation. Please choose Add, Subtract, Multiply, Divide, or their corresponding number.")
