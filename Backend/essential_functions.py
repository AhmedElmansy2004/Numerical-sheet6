from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

import re

def convert(expression):

    # remove spaces
    expression = re.sub(r"\s+", "", expression)

    # exponentiation
    expression = expression.replace("^", "**")

    # exponential function e^x => exp(x)
    expression = re.sub(r"\be\*\*([A-Za-z0-9]+)", r"exp(\1)", expression)
    expression = re.sub(r"\be\*\*\(([A-Za-z0-9]+)\)", r"exp(\1)", expression)

    

    # algebraic multiplication
    expression = re.sub(r"(\d)([A-Za-z(])", r"\1*\2", expression)
    expression = re.sub(r"\)([A-Za-z]+)", r"\)*\1", expression)

    # trig and sqrt functions
    functions = ["sin", "cos", "tan", "sec", "csc", "cot", "sqrt"]

    expression = re.sub(rf"([A-Za-z0-9])({'|'.join(functions)})", r"\1*\2", expression)

    for f in functions:
        expression = re.sub(rf"{f}([A-Za-z0-9]+)", rf"{f}(\1)", expression)

    # ln function
    expression = re.sub(r"\bln([A-Za-z0-9]+)", r"log(\1)", expression)

    # log (default base of 10)
    expression = re.sub(r"\blog([A-Za-z0-9]+)", r"log(\1, 10)", expression)

    return expression

def getValue(func, x_val):
    x = symbols('x')
    func = convert(func)
    expr = parse_expr(func)
    return float(expr.subs(x, x_val).evalf())

def getDerivative(func, x_val):
    x = symbols('x')
    func = convert(func)
    expr = parse_expr(func)
    diff_x = expr.diff(x)
    return float(diff_x.subs(x, x_val).evalf())
    

def getSecondDerivative(func, x_val):
    x = symbols('x')
    func = convert(func)
    expr = parse_expr(func)
    diff_x = expr.diff(x, 2)
    return float(diff_x.subs(x, x_val).evalf())
    

def getEPS(current, previous):
    if previous == current:
        print("zerooooo")
    return abs((current - previous) / current) * 100


if "__main__" == __name__:
    print(type(getValue('x', 1)))
    print(getValue('x', 1))



def round_to_significant_digits(x, n):
    if x == 0:
        return 0

    sign = 1
    if x < 0:
        sign = -1
        x = -x

    # Compute magnitude: k = floor(log10(x))
    k = math.floor(math.log10(x))

    # Scale x to have n significant digits:
    factor = 10**(n - 1 - k)
    rounded = round(x * factor) / factor

    return sign * rounded

def calculate_significant_digits(epsilon):
    # epsilon value = ( 0.5 * 10**(2-n) ) %
    return math.floor(2 - math.log10(epsilon * 2))

def count_all_digits(x):
    return sum(ch.isdigit() for ch in str(abs(x if not x.is_integer() else round(x))))
