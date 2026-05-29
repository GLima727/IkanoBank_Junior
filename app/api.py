from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from app.calculations import fibonacci, factorial, loan_repayment

app = FastAPI(title="Junior Dev Assignment API")


class FibonacciRequest(BaseModel):
    n: int

    @field_validator("n")
    @classmethod
    def n_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError("n must be a non-negative integer")
        return v


class FactorialRequest(BaseModel):
    n: int

    @field_validator("n")
    @classmethod
    def n_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError("n must be a non-negative integer")
        return v


class LoanRepaymentRequest(BaseModel):
    principal: float
    annual_rate: float
    months: int

    @field_validator("principal")
    @classmethod
    def principal_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("principal must be greater than zero")
        return v

    @field_validator("annual_rate")
    @classmethod
    def rate_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError("annual_rate must be non-negative")
        return v

    @field_validator("months")
    @classmethod
    def months_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("months must be greater than zero")
        return v


@app.post("/fibonacci")
def compute_fibonacci(request: FibonacciRequest):
    result = fibonacci(request.n)
    return {"n": request.n, "result": result}


@app.post("/factorial")
def compute_factorial(request: FactorialRequest):
    result = factorial(request.n)
    return {"n": request.n, "result": result}


@app.post("/loan-repayment")
def compute_loan_repayment(request: LoanRepaymentRequest):
    result = loan_repayment(request.principal, request.annual_rate, request.months)
    return {
        "principal": request.principal,
        "annual_rate": request.annual_rate,
        "months": request.months,
        "monthly_payment": result,
    }
