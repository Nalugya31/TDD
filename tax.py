"""
calculating tax
"""


def calculate_tax(earning):
    if earning < 12000:
        return 0.0
    elif earning >= 12000 and earning <= 36000:
        rate1 = 0.2
        tax1 = rate1 * earning
        return tax1
    else:
        rate2 = 0.4
        tax2 = rate2 * earning
        return tax2


result = calculate_tax(26000)
print("The total tax is", result)