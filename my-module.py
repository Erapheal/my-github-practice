def calculate(num1, operator, num2):
#conditional statement for the calculator
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operator."


def run_calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        result = calculate(num1, operator, num2)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ =="__main__":
    run_calculator()
