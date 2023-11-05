import pytest
import source.my_funcs as my_funcs


def test_add():
    result = my_funcs.add(1, 4)
    assert result == 5


def test_add_strings():
    result = my_funcs.add('one', 'two')
    assert result == "onetwo"

def test_divide():
    result = my_funcs.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        result = my_funcs.divide(10, 0)