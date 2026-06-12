"""
Mini API for the QA Automation demo.

Run:
    uvicorn app.main:app --reload

Open:
    http://127.0.0.1:8000/docs
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.calculator import calculate

app = FastAPI(title="QA Automation Demo API")


class CalculationRequest(BaseModel):
    operation: str
    a: float
    b: float


class CalculationResponse(BaseModel):
    result: float


@app.get("/")
def health_check() -> dict[str, str]:
    return {"status": "ok", "message": "QA Automation Demo API is running"}


@app.post("/calculate", response_model=CalculationResponse)
def calculate_endpoint(payload: CalculationRequest) -> CalculationResponse:
    try:
        result = calculate(payload.operation, payload.a, payload.b)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return CalculationResponse(result=result)
