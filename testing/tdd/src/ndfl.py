def calculate_ndfl(income):
    result = 0
    if income < 2_400_000:
        result = income * 0.13
    elif income < 5_000_000:
        result = (2_400_000 * 0.13 +  \
                (income - 2_400_000) * 0.15)
    elif income < 20_000_000:
        result = (2_400_000 * 0.13 + \
                2_600_000 * 0.15 + \
                (income - 5_000_000) * 0.18)
    elif income < 50_000_000:
        result = (2_400_000 * 0.13 + \
                2_600_000 * 0.15 + \
                15_000_000 * 0.18 + \
                (income - 20_000_000) * 0.20)
    elif income > 50_000_000:
        result = (2_400_000 * 0.13 + \
                2_600_000 * 0.15 + \
                15_000_000 * 0.18 + \
                30_000_000 * 0.20 + \
                (income - 50_000_000) * 0.22)
    
    return result