def calculator():
    print("Welcome to the Ankit's simple calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    sign = input("Choose a operation +, -, *, / : ")
    
    if sign == '+':
        result = num1 + num2
    elif sign == '-':
        result = num1 - num2
    elif sign == '*':
        result = num1 * num2
    elif sign == '/':
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    else:
        result = "Invalid operation!"

    print("The result is:", result)

calculator()
