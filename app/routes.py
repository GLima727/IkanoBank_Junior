from fastapi import FastAPI
from app.calculations import fibonacci, factorial, loan_repayment
from app.models import FibonacciRequest, FactorialRequest, LoanRepaymentRequest

app = FastAPI(title="Junior Dev Assignment API")


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
