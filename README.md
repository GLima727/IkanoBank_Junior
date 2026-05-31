# Junior Developer Assignment

A small FastAPI service that exposes three calculation endpoints: Fibonacci, Factorial, and Loan Repayment.

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── calculations.py   # Pure business logic
│   ├── models.py         # Pydantic request models & validation
│   └── routes.py         # FastAPI app & endpoints
├── tests/
│   ├── __init__.py
│   └── test_calculations.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup & Run (plain Python)

**Requirements:** Python 3.10+

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.routes:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs (Swagger UI) are at `http://localhost:8000/docs`.

## Setup & Run (Docker)

```bash
# Build the image
docker build -t junior-assignment .

# Run the container
docker run -p 8000:8000 junior-assignment
```

The API will be available at `http://localhost:8000`.

## Running Tests

```bash
# With the virtual environment active
pytest tests/ -v
```

## API Endpoints

All endpoints accept JSON via `POST`.

### `POST /fibonacci`

```json
{ "n": 10 }
```

Returns the nth Fibonacci number.

### `POST /factorial`

```json
{ "n": 5 }
```

Returns n!

### `POST /loan-repayment`

```json
{ "principal": 10000, "annual_rate": 5, "months": 24 }
```

Returns the fixed monthly payment rounded to 2 decimal places.  
`annual_rate` is a percentage (e.g. `5` means 5%).

## Assumptions & Limitations

- **Fibonacci / Factorial inputs** must be non-negative integers. Floats, booleans, and negative numbers are rejected with a `422` response.
- **Factorial cap** — inputs are limited to `n <= 10,000` to avoid excessive computation time. Larger values are rejected with a `422` response.
- **Loan repayment** uses Python's `Decimal` type internally to avoid floating-point rounding errors. Results are rounded to 2 decimal places using ROUND_HALF_UP.
- **Zero-interest loans** (`annual_rate = 0`) are handled as equal principal-only instalments: `monthly = principal / months`.
- **No persistence** — all calculations are stateless; nothing is stored between requests.
- **No authentication** — the API is open; add an auth layer before exposing it publicly.
