# Define the basic calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "cannot divide by zero"
    
# To get valid numerical inputs
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
# Present possible operations to the user then receive input
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")
  
    # Enter variables to be calculated 
    num1 = get_numeric_input("Enter first number: ")
    num2 = get_numeric_input("Enter second number: ")

    # Perform calculations
    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid choice.")

# Call the calculator function
calculator()
