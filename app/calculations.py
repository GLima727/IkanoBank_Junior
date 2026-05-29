from decimal import Decimal, ROUND_HALF_UP


def fibonacci(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def factorial(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def loan_repayment(principal: float, annual_rate: float, months: int) -> float:
    if not isinstance(months, int) or isinstance(months, bool):
        raise TypeError("months must be an integer")
    if principal <= 0:
        raise ValueError("principal must be greater than zero")
    if annual_rate < 0:
        raise ValueError("annual_rate must be non-negative")
    if months <= 0:
        raise ValueError("months must be greater than zero")

    p = Decimal(str(principal))
    r_annual = Decimal(str(annual_rate))
    n = Decimal(str(months))

    if r_annual == 0:
        monthly = p / n
    else:
        r = r_annual / Decimal("100") / Decimal("12")
        monthly = p * r * (1 + r) ** int(n) / ((1 + r) ** int(n) - 1)

    return float(monthly.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
