from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from bracketing import *


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculationRequest(BaseModel):
    terms: List[PolynomialTerm]
    tolerance: float
    from_value: float
    to_value: float
    method: str
    errorType: str

@app.post("/calculate")
def calculate(request: CalculationRequest):

    if(not (request.errorType == 'abs' or request.errorType == 'rel')):
        raise HTTPException(status_code=404, detail='choose a valid error type')
    
    elif(request.method == 'bt'):
        result = do_bisection(request.terms, request.from_value, request.to_value, request.tolerance, request.errorType)

    elif(request.method == 'fp'):
        result = do_false_position(request.terms, request.from_value, request.to_value, request.tolerance, request.errorType)

    else:
        raise HTTPException(status_code=404, detail='choose a valid method')
    
    return {
        "status": "ok",
        "root": result
    }
