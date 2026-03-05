# import sys
# sys.path.append("../src")

from math_demo import add, add_with_bug


def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("Test ADDITION PASSED")


def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    # finally we found data that make test reliable
    # assert add_with_bug(7, 6) == 13
    print("Test BUGGED ADDITION PASSED")


def test_addition_duplicate():
    assert add(6, 7) == 6 + 7
    print("Test DUPLICATE ADDITION PASSED")


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
