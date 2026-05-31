from pydantic import BaseModel, field_validator
from app.calculations import MAX_FACTORIAL_N


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
        if v > MAX_FACTORIAL_N:
            raise ValueError(f"n must be <= {MAX_FACTORIAL_N} to avoid excessive computation")
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
