from t32 import square
# library to test the code - unit testing 
# import pytest

def test_square():
    assert square(2) == 4
    assert square(5)== 25
    assert square(-2) == 4
    assert square(-5) == 5
    assert square(0) == 0




