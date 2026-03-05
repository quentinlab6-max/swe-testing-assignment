from calculator import Calculator

def test_full_operation_sequence():
    calc = Calculator()

    result = calc.add(5, 3)

    assert result == 8

def test_clear_function():
    calc = Calculator()

    calc.add(5, 3)
    result = calc.clear()

    assert result == 0