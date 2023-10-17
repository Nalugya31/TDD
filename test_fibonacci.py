from fibonacci import fibonacci
# Test cases using pytest
import pytest

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected

#Uncomment the line below to run the tests
if __name__ == '__main__':
    pytest.main()



#fibonacci(4) = fibonacci(3) + fibonacci(2)
#fibonacci(3) = fibonacci(2) + fibonacci(1)
#fibonacci(2) = fibonacci(1) + fibonacci(0)