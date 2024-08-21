def calculate(operation, x, y):
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if y == 0:
            return "Error: Division by zero."
        else:
            return x / y
    else:
        return "Invalid operation."

# 测试代码
print(calculate('add', 10, 5))       # 输出: 15
print(calculate('subtract', 10, 5))  # 输出: 5
print(calculate('multiply', 10, 5))  # 输出: 50
print(calculate('divide', 10, 5))    # 输出: 2.0
print(calculate('divide', 10, 0))    # 输出: Error: Division by zero.
print(calculate('modulo', 10, 5))    # 输出: Invalid operation.
