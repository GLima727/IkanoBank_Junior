from fastapi.testclient import TestClient
from app.routes import app

client = TestClient(app)

# --- Fibonacci ---


def test_fibonacci_normal():
    response = client.post("/fibonacci", json={"n": 10})
    assert response.status_code == 200
    assert response.json() == {"n": 10, "result": 55}


def test_fibonacci_edge_zero():
    response = client.post("/fibonacci", json={"n": 0})
    assert response.status_code == 200
    assert response.json()["result"] == 0


def test_fibonacci_negative_raises():
    response = client.post("/fibonacci", json={"n": -1})
    assert response.status_code == 422


def test_fibonacci_non_integer_raises():
    response = client.post("/fibonacci", json={"n": 3.5})
    assert response.status_code == 422


# --- Factorial ---


def test_factorial_normal():
    response = client.post("/factorial", json={"n": 5})
    assert response.status_code == 200
    assert response.json() == {"n": 5, "result": 120}


def test_factorial_edge_zero():
    response = client.post("/factorial", json={"n": 0})
    assert response.status_code == 200
    assert response.json()["result"] == 1


def test_factorial_negative_raises():
    response = client.post("/factorial", json={"n": -3})
    assert response.status_code == 422


def test_factorial_exceeds_cap_raises():
    response = client.post("/factorial", json={"n": 10_001})
    assert response.status_code == 422


# --- Loan Repayment ---


def test_loan_repayment_normal():
    response = client.post(
        "/loan-repayment",
        json={"principal": 10000, "annual_rate": 5, "months": 24},
    )
    assert response.status_code == 200
    assert response.json()["monthly_payment"] == 438.71


def test_loan_repayment_zero_interest():
    response = client.post(
        "/loan-repayment",
        json={"principal": 1200, "annual_rate": 0, "months": 12},
    )
    assert response.status_code == 200
    assert response.json()["monthly_payment"] == 100.00


def test_loan_repayment_negative_principal_raises():
    response = client.post(
        "/loan-repayment",
        json={"principal": -1000, "annual_rate": 5, "months": 12},
    )
    assert response.status_code == 422


def test_loan_repayment_negative_rate_raises():
    response = client.post(
        "/loan-repayment",
        json={"principal": 1000, "annual_rate": -1, "months": 12},
    )
    assert response.status_code == 422


def test_loan_repayment_zero_months_raises():
    response = client.post(
        "/loan-repayment",
        json={"principal": 1000, "annual_rate": 5, "months": 0},
    )
    assert response.status_code == 422
