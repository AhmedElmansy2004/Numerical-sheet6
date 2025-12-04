from essential_functions import getValue, getDerivative, getSecondDerivative,getEPS

# to do: fix if derivaitive = 0


def do_modified_newton(func, intial, precision, epsilon=0.00001, maxIterations = 50):

    x_old = round(intial, precision)

    # first guess was true
    if(getValue(func, x_old) == 0): return True, x_old, 0, -1, precision, None

    res1 = getValue(func, x_old) * getDerivative(func, x_old)
    res2 = (getDerivative(func, x_old) ** 2) - (getValue(func, x_old) * getSecondDerivative(func, x_old))

    # diverge
    if(res2 == 0): return False, x_old, 0, -1, precision, None

    res = res1 / res2
    x_new = round(x_old - res, precision)

    

    solution_steps = [{
        "x_i": x_old,
        "x_i+1": x_new,
        "eps": -1
    }]

    if(getValue(func, x_old) == 0):
        return True, x_new, 0, -1, precision, solution_steps

    relative_error = 120

    for i in range(maxIterations):
        
        x_old = x_new

        res1 = getValue(func, x_old) * getDerivative(func, x_old)
        res2 = (getDerivative(func, x_old) ** 2) - (getValue(func, x_old) * getSecondDerivative(func, x_old))

        # diverge
        if(res2 == 0): return False, x_old, 0, -1, precision, None

        res = res1 / res2
        x_new = round(x_old - res, precision)

        relative_error = getEPS(x_new, x_old)

        solution_steps.append({
            "x_i": x_old,
            "x_i+1": x_new,
            "eps": relative_error
        })

        if(getValue(func, x_new) == 0 or relative_error <= epsilon):
            break

    if(getValue(func, x_new) == 0 or relative_error <= epsilon):
        return True, x_new, i+1, relative_error, precision, solution_steps 
    else:
        return False, x_new, i+1, relative_error, precision, solution_steps