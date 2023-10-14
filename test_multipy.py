from multiply import multiply

def test_multiply_1():
    result = multiply(1,1)
    assert result == 1


def test_multiply_2():
    result = multiply(2,2)
    assert result == 4

def test_multiply_3():
    result = multiply(3,3)
    assert result == 9

def test_multiply_4():
    result = multiply(4,4)
    assert result == 16

def test_multiply_5():
    result = multiply(23,45)
    assert result == 23*45
    