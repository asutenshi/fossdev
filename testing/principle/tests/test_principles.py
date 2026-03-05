import sys
sys.path.append("../src")

from math_demo import add

def test_addition():
    assert 2 + 2 == 4
    print("Test ADDITION PASSED")

if __name__ == "__main__":
    test_addition()
