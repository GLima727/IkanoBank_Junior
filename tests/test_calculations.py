import pytest
from app.calculations import fibonacci, factorial, loan_repayment

# Run the test suite: pytest tests/ -v

# --- Fibonacci ---


def test_fibonacci_normal():
    assert fibonacci(10) == 55


def test_fibonacci_edge_zero():
    assert fibonacci(0) == 0


def test_fibonacci_edge_one():
    assert fibonacci(1) == 1


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci(-1)


# --- Factorial ---


def test_factorial_normal():
    assert factorial(5) == 120


def test_factorial_edge_zero():
    assert factorial(0) == 1


def test_factorial_large():
    assert factorial(20) == 2432902008176640000


def test_factorial_negative_raises():
    with pytest.raises(ValueError, match="non-negative"):
        factorial(-3)


def test_factorial_exceeds_cap_raises():
    with pytest.raises(ValueError, match="10000"):
        factorial(10_001)


# --- Loan Repayment ---


def test_loan_repayment_normal():
    assert loan_repayment(10000, 5, 24) == 438.71


def test_loan_repayment_zero_interest():
    assert loan_repayment(1200, 0, 12) == 100.00


def test_loan_repayment_negative_principal_raises():
    with pytest.raises(ValueError, match="principal"):
        loan_repayment(-1000, 5, 12)


def test_loan_repayment_negative_rate_raises():
    with pytest.raises(ValueError, match="annual_rate"):
        loan_repayment(1000, -1, 12)


def test_loan_repayment_zero_months_raises():
    with pytest.raises(ValueError, match="months"):
        loan_repayment(1000, 5, 0)
