def add(a, b):
    return a + b
def power(a, b):
    return a ** b

def modulus(a,b):
    return a%b
def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("=== CALCULATOR ===")

a = float(input("Enter first number: "))
operator = input("Enter operation (+, -, *, /, ^, **, %): ")
b = float(input("Enter second number: "))

if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = subtract(a, b)
elif operator == "*":
    result = multiply(a, b)
elif operator == "/":
    result = divide(a, b)
elif operator == "^" or operator == "**":
    result = power(a, b)
elif operator == "%":
    result = modulus(a, b)
else:
    result = "Invalid operation"

print("Result:", result)
