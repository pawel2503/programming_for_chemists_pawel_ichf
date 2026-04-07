import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    return a / b

def square(a):
    return a ** 2

def root(a):
    if a < 0:
        print("Error: Cannot take square root of negative number!")
        return None
    return math.sqrt(a)

def pi():
    return math.pi

def clear():
    return 0

def display(value):
    print(f"Result: {value}")
    return value