num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result= "invalid operation"
    
print(f"Result:{result}")