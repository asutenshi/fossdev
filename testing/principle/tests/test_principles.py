# import sys
# sys.path.append("../src")

from math_demo import add, add_with_bug, calculate_tax_bugged, calculate_tax


def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("Test ADDITION PASSED")


def test_addition_with_bug():
    # Тесты показывают наличие ошибок, а не их остутствие
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    # finally we found data that make test reliable
    # assert add_with_bug(7, 6) == 13
    print("Test BUGGED ADDITION PASSED")


def test_addition_duplicate():
    # Тесты не предсказывают работу проверяемой функции
    assert add(6, 7) == 6 + 7
    print("Test DUPLICATE ADDITION PASSED")


def test_addition_overkill():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == i + j  # violation of duplication
            assert add(-i, j) == -i + j
            assert add(-i, -j) == -i + -j
            assert add(i, -j) == i + -j


def test_addition_clussters():
    assert add(7, 6) == 13
    assert add(0, 6) == 6
    assert add(7, 0) == 7
    assert add(10, -11) == -1
    assert add(-10, -11) == -21
    assert add(0, -5) == -5
    assert add(-10, 0) == -10
    print("Test CLUSSTERS ADDITION PASSED")


def test_addition_commutative():
    assert add(9, 5) == 14
    assert add(5, 9) == 14
    print("Test COMMUTATIVE PASSED")
    
    
def test_tax_calculator_pesticide():
    assert calculate_tax_bugged(1000) == 150
    assert calculate_tax_bugged(100) == 15
    assert calculate_tax_bugged(10) == 1.5
    assert calculate_tax_bugged(1) == 0.15
    assert calculate_tax_bugged(234) == 35.1
    # only integers don't cover some tests
    # assert calculate_tax_bugged(2.34) == 0.35 # 0.351
    print("Test TAX BAGGED CALCULATOR PASSED")
    
    
def test_tax_calculator():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(234) == 35.1
    # float may give us more test cases
    assert calculate_tax(2.34) == 0.35 # 0.351
    print("Test TAX UNBUGGED CALCULATOR PASSED")


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    # test_addition_overkill()
    test_addition_clussters()
    test_addition_commutative()
    test_tax_calculator_pesticide()
    test_tax_calculator()