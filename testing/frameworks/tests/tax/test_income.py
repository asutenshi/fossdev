from tax.income import calculate_tax

def test_income():
    assert calculate_tax(100) == 15
    print("Test tax passed")

if __name__ == "__main__":
    test_income()