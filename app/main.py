from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, Optional

app = FastAPI(title="Consolidacao Carteira AP")


class ProcessRequest(BaseModel):
    name: str
    value: float
    metadata: Optional[Dict[str, Any]] = None


class ProcessResponse(BaseModel):
    status: str
    processed_value: float
    message: str


@app.get("/")
def root():
    return {"message": "API is alive"}


@app.post("/process", response_model=ProcessResponse)
def process(data: ProcessRequest):
    processed = data.value * 1.1
    return ProcessResponse(
        status="ok",
        processed_value=processed,
        message=f"Processed {data.name}",
    )
