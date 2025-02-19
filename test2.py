# addition 
def add(x, y):
    return x + y

# subtraction
def subtract(x, y):
    return x - y

# multiplication
def multiply(x, y):
    return x * y

# division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# main function 
def main():
    # reads the 2 numbers from the user 
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return


# options for calculation presented  
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

# option for calculation imputed by user
    choice = input("Enter choice (1/2/3/4): ")
# calculation based on the type of operation selected
    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid choice! Please select a valid operation.")


# makes it run
if __name__ == "__main__":
    main()
