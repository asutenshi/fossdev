from script import devide, sum


def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a, b) == result


def test_devide():
    a = 2
    b = 4
    result = 0.5
    assert devide(a, b) == result


def test_devide_zero():
    a = 2
    b = 0
    try:
        devide(a, b)
        assert False
    except ValueError as e:
        print("Test (zero-devision) passed")


def test_devision_prohibited():
  try:
    devide("A", "B")
    print("Test string-devision fails")
    assert False
  except ValueError as e:
    print("Test string-devision passed")


if __name__ == "__main__":
    test_sum()
    test_devide()
    test_devide_zero()
    test_devision_prohibited()
