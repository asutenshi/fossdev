from ndfl import calculate_ndfl

# TODO make test to obey principles

def test_ndfl_tier_1_basic():
    assert calculate_ndfl(2_000_000) == 260_000
    
    
def test_ndfl_tier_2_basic():
    # 4_000_000 -> 2_400_000 * 0.13 + 1_600_000 * 0.15
    assert calculate_ndfl(4_000_000) == 552_000


def test_ndfl_tier_3_basic():
    # 10_000_000 -> 2_400_000 * 0.13 + 2_600_000 * 0.15 + 
    # + 5_000_000 * 0.18
    assert calculate_ndfl(10_000_000) == 1_602_000


def test_ndfl_tier_4_basic():
    # 30_000_000 -> 2_400_000 * 0.13 + 2_600_000 * 0.15 + 
    # + 15_000_000 * 0.18 + 10_000_000 * 0.20
    assert calculate_ndfl(30_000_000) == 5_402_000


def test_ndfl_tier_5_basic():
    # 30_000_000 -> 2_400_000 * 0.13 + 2_600_000 * 0.15 + 
    # + 15_000_000 * 0.18 + 30_000_000 * 0.20 + 10_000_000 * 0.22
    assert calculate_ndfl(60_000_000) == 11_602_000