from pydantic import BaseModel
from math import *

class PolynomialTerm(BaseModel):
    coefficient: float
    exponent: float

def calc_rel_err(current, previous):
    return abs((current - previous) / current) * 100

def get_value(polynomial, x_value):
    y_value = 0
    for term in polynomial:
        y_value += term.coefficient * (x_value ** term.exponent)

    return y_value

def do_bisection(func, from_val, to_val, tolerance, errorType):

    interval_length = abs(to_val - from_val)
    number_of_iterations = ceil(log2(interval_length / tolerance)) if (errorType == 'abs') else 1

    epsilon = tolerance + 100

    x_l = from_val
    y_l = get_value(func, x_l)
    x_u = to_val
    y_u = get_value(func, x_u)
    x_r = 0
    y_r = 0
    prev = 0

    isFirstIteration = True

    while((errorType == 'abs' and number_of_iterations) or (errorType == 'rel' and epsilon > tolerance)):
        prev = x_r
        x_r = x_l + (x_u - x_l) / 2
        y_r = get_value(func, x_r)

        if(y_l * y_r < 0):
            x_u = x_r
            y_u = y_r
        
        elif(y_u * y_r < 0):
            x_l = x_r
            y_l = y_r

        elif(y_r == 0):
            break

        if(not isFirstIteration):
           epsilon = calc_rel_err(x_r, prev)
           isFirstIteration = False

        if(errorType == 'abs'):
            number_of_iterations -= 1

    return x_r


def do_false_position(func, from_val, to_val, tolerance, errorType):

    interval_length = abs(to_val - from_val)
    number_of_iterations = ceil(log2(interval_length / tolerance)) if (errorType == 'abs') else 1

    epsilon = tolerance + 100

    x_l = from_val
    y_l = get_value(func, x_l)
    x_u = to_val
    y_u = get_value(func, x_u)
    x_r = 0
    y_r = 0
    prev = 0

    isFirstIteration = True

    while((errorType == 'abs' and number_of_iterations) or (errorType == 'rel' and epsilon > tolerance)):
        prev = x_r
        x_r = ((x_l * y_u) - (x_u * y_l)) / (y_u - y_l)
        y_r = get_value(func, x_r)

        if(y_l * y_r < 0):
            x_u = x_r
            y_u = y_r
        
        elif(y_u * y_r < 0):
            x_l = x_r
            y_l = y_r

        elif(y_r == 0):
            break
        
        if(not isFirstIteration):
           epsilon = calc_rel_err(x_r, prev)
           isFirstIteration = False

        if(errorType == 'abs'):
            number_of_iterations -= 1

    return x_r





    
