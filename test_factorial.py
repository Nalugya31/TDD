from factorial import calculate_factorial
import pytest


# def test_calculate_factorial_0f_zero():
#     assert calculate_factorial(0) == 1


# def test_calculate_factorial_of_positive_value():
#     assert calculate_factorial(5) == 120


# def test_calculate_factorial_of_negative_value():
#     with pytest.raises(ValueError):
#         calculate_factorial(-5)




#Using a loop

# Test case 1: Test the factorial of 0
def test_factorial_zero():
    assert calculate_factorial(0) == 1

# Test case 2: Test the factorial of a positive number using a loop
def test_factorial_positive():
    for n in range(1, 11):  # Testing numbers from 1 to 10
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        assert calculate_factorial(n) == fact

# Test case 3: Test the factorial of a negative number
def test_factorial_negative():
    with pytest.raises(ValueError):
        calculate_factorial(-5)










# My pair is Nakaweesi Juliet.
