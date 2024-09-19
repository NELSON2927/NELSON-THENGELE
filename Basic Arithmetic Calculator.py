def calculator():
    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
      
        operator = input("Enter an operator (+, -, *, /): ")
        
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            
            result = num1 / num2
        else:
            print("Invalid operator! Please use one of the following: +, -, *, /")
            return
        
        
        print(f"The result is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    