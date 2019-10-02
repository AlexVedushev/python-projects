import pytest
import sys



def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5


class TestB:
    def test_c(self):
        with pytest.raises(ZeroDivisionError):
            1/0