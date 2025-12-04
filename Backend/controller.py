from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any, Union

from bisection import *
from false_position import *
from original_newton import *
from modified_newton import *
from fixed_point import *
from secant import *

from time import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BracketingRequest(BaseModel):
    method: str
    func: str
    from_value: float
    to_value: float
    precision: int
    tol: float
    maxIterations: int
    steps: bool

class NewtonRequest(BaseModel):
    method: str
    func: str
    intialGuess: float
    precision: int
    tol: float
    maxIterations: int
    steps: bool

class FixedRequest(BaseModel):
    func: str
    gx: str
    intialGuess: float
    precision: int
    tol: float
    maxIterations: int
    steps: bool

class SecantRequest(BaseModel):
    func: str
    intialGuess: float
    intialGuess2: float
    precision: int
    tol: float
    maxIterations: int
    steps: bool

class Response(BaseModel):
    status: str
    message: str
    result: Union[float, None]
    iterations: int
    rel_err: float
    precision: int
    time: float
    steps: Union[List[Any], None] = List[Any]

@app.post("/bracketing")
def calculate(request: BracketingRequest):

    start = time()
    
    if(request.method == 'bisection'):
        valid, result, iterations, rel_err, precision, steps = do_bisection(request.func,
                                                                            request.from_value, 
                                                                            request.to_value, 
                                                                            request.precision, 
                                                                            request.tol, 
                                                                            request.maxIterations)

    elif(request.method == 'false position'):
        valid, result, iterations, rel_err, precision, steps = do_false_position(request.func,
                                                                                    request.from_value, 
                                                                                    request.to_value, 
                                                                                    request.precision, 
                                                                                    request.tol, 
                                                                                    request.maxIterations)

    else:
        raise HTTPException(status_code=404, detail='choose a valid method')
    
    end = time()

    message = ""

    if(not valid):
        result = None
        message = "Diverge"
        
    if(not request.steps):
        steps = None

    response: Response = Response(
        status='ok',
        message=message,
        result=result,
        iterations=iterations,
        rel_err=rel_err,
        precision=precision,
        time= end - start,
        steps=steps
    ) 
    
    return response

@app.post("/newton")
def calculate(request: NewtonRequest):

    start = time()
    
    if(request.method == 'orginal newton'):
        valid, result, iterations, rel_err, precision, steps = do_original_newton(request.func,
                                                                                    request.intialGuess, 
                                                                                    request.precision, 
                                                                                    request.tol, 
                                                                                    request.maxIterations)

    elif(request.method == 'modified newton'):
        valid, result, iterations, rel_err, precision, steps = do_modified_newton(request.func,
                                                                                    request.intialGuess, 
                                                                                    request.precision, 
                                                                                    request.tol, 
                                                                                    request.maxIterations)

    else:
        raise HTTPException(status_code=404, detail='choose a valid method')
    
    end = time()

    message = ""
    
    if(not valid):
        result = None
        message = "Diverge"
        
    if(not request.steps):
        steps = None

    response: Response = Response(
        status='ok',
        message=message,
        result=result,
        iterations=iterations,
        rel_err=rel_err,
        precision=precision,
        time= end - start,
        steps=steps
    ) 
    
    return response

@app.post("/fixed")
def calculate(request: FixedRequest):

    start = time()

    valid, result, iterations, rel_err, precision, steps = do_fixed_point(request.gx,
                                                                            request.intialGuess, 
                                                                            request.precision, 
                                                                            request.tol, 
                                                                            request.maxIterations)
    
    end = time()

    message = ""

    if(not valid):
        result = None
        message = "Diverge"
        
    if(not request.steps):
        steps = None

    response: Response = Response(
        status='ok',
        message=message,
        result=result,
        iterations=iterations,
        rel_err=rel_err,
        precision=precision,
        time= end - start,
        steps=steps
    ) 
    
    return response


@app.post("/secant")
def calculate(request: SecantRequest):

    start = time()

    valid, result, iterations, rel_err, precision, steps = do_secant(request.func,
                                                                        request.intialGuess,
                                                                        request.intialGuess2, 
                                                                        request.precision, 
                                                                        request.tol, 
                                                                        request.maxIterations)
    
    end = time()

    message = ""
    
    if(not valid):
        result = None
        message = "Diverge"
        
    if(not request.steps):
        steps = None

    response: Response = Response(
        status='ok',
        message=message,
        result=result,
        iterations=iterations,
        rel_err=rel_err,
        precision=precision,
        time= end - start,
        steps=steps
    ) 
    
    return response


