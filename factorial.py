# factorial.py
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)
