def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes introducir un número entero.")

def addition():
    num1 = pedir_entero("Enter the first number: ")
    num2 = pedir_entero("Enter the second number: ")
    print(f"The sum of {num1} and {num2} is:", num1 + num2)

def subtraction():
    num1 = pedir_entero("Enter the first number: ")
    num2 = pedir_entero("Enter the second number: ")
    print(f"The difference of {num1} and {num2} is:", num1 - num2)
    
def multiplication():
    num1 = pedir_entero("Enter the first number: ")
    num2 = pedir_entero("Enter the second number: ")
    print(f"The product of {num1} and {num2} is:", num1 * num2)

def division():
    num1 = pedir_entero("Enter the first number: ")
    num2 = pedir_entero("Enter the second number: ")

    try:
        result = num1 / num2
        print(f"The quotient of {num1} and {num2} is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Division operation completed.")

def factorial():
    num = pedir_entero("Enter a number to find its factorial: ")
    print("The factorial of " + str(num) + " is:", str(factorial_helper(num)))

def factorial_helper(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_helper(n - 1)

def exponentiation():
    base = pedir_entero("Enter the base number: ")
    exponent = pedir_entero("Enter the exponent: ")
    print(f"{base} raised to the power of {exponent} is:", exponentiation_helper(base, exponent))

def exponentiation_helper(base, exponent):
    if exponent <= 0:
        return 1
    else:
        return base * exponentiation_helper(base, exponent - 1)
    
def calculator():
    fin = False
    while not fin:
        
        opc = pedir_entero("Opcion: ")
        
        if opc == 1:
            addition()
        elif opc == 2:
            subtraction()
        elif opc == 3:
            multiplication()
        elif opc == 4:
            division()
        elif opc == 5:
            factorial()
        elif opc == 6:
            exponentiation()
        elif opc == 7:
            print("Exiting the calculator. Goodbye!")
            fin = True
        else:
            print("Invalid option. Please try again.")

    
if __name__ == "__main__":
    try:
        print("Welcome to the calculator!") 
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Factorial")
        print("6. Exponentiation")
        print("7. Exit")
        calculator()
    except KeyboardInterrupt:
        print("\nExiting the calculator. Goodbye!")
        

