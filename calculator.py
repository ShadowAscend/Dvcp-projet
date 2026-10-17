number1 = int(input("Enter a number : "))
number2 = int(input("Enter a number : "))

operation = input("Choose an operation (+, -, *, /): ").strip()

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number1 == 0 or number2 == 0:
        print("Your answer is equals to zero.")
    else:
        result = number1 / number2
else:
    print("Invalid operation. Please choose +, -, *, or /.")
    
if operation in ("+", "-", "*", "/") and not (operation == "/" and number2 == 0):
    print(f"Result: {result}")

