def calculator(a, b, operation):
    # Implement basic arithmetic operations here
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '/':
        if b!=0:
            return a/b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Test your function
print(calculator(10, 5, '+'))  # Should output 15
print(calculator(10, 5, '-'))  # Should output 5
print(calculator(10, 5, '*'))  # Should output 50
print(calculator(10, 5, '/'))  # Should output 2.0