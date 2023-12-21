# This is a basic Python Project, A calculator to perform Add, Subtract, Divide and Multiply

# Define functions to perform functions
def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


def modulo(number1, number2):
    return number1 % number2


# Function to get a valid operand from the user
def get_operand():
    while True:
        operand = int(input("Enter Operand 1 - 5: "))
        if 1 <= operand <= 5:
            return operand
        else:
            print("Invalid input. Please enter a number between 1 and 5.")


# Display options to the user
print("Enter the operation you want to perform:\n" +
      "1. Addition\n" +
      "2. Subtraction\n" +
      "3. Multiplication\n" +
      "4. Division \n" +
      "5. Modulo: ")

# Get a valid operand from the user
operand = get_operand()

# Ask the user for input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))


# Function to call which operation function when needed
def calculate():
    if operand == 1:
        return addition(number1, number2)
    elif operand == 2:
        return subtraction(number1, number2)
    elif operand == 3:
        return multiplication(number1, number2)
    elif operand == 4:
        return division(number1, number2)
    elif operand == 5:
        return modulo(number1, number2)


# Display results back to the user
result = calculate()
if result is not None:
    print(f"The result is: {result}")
