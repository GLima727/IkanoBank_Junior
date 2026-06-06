def fibonacci(n: int) -> int:

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


MAX_FACTORIAL_N = 10_000


def factorial(n: int) -> int:

    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n > MAX_FACTORIAL_N:
        raise ValueError(
            f"n must be <= {MAX_FACTORIAL_N} to avoid excessive computation"
        )

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def loan_repayment(principal: float, annual_rate: float, months: int) -> float:

    if principal <= 0:
        raise ValueError("principal must be greater than zero")
    if annual_rate < 0:
        raise ValueError("annual_rate must be non-negative")
    if months <= 0:
        raise ValueError("months must be greater than zero")

    if annual_rate == 0:
        return round(principal / months, 2)

    r = (annual_rate / 100) / 12
    monthly = principal * r * (1 + r) ** months / ((1 + r) ** months - 1)
    return round(monthly, 2)
