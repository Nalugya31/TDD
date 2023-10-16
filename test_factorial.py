from factorial import calculate_factorial
import pytest


def test_calculate_factorial_0f_zero():
    assert calculate_factorial(0) == 1


def test_calculate_factorial_of_positive_value():
    assert calculate_factorial(5) == 120


def test_calculate_factorial_of_negative_value():
    with pytest.raises(ValueError):
        calculate_factorial(-5)


# My pair is Nakaweesi Juliet.
