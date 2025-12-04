from essential_functions import getValue, getEPS

def do_secant(func, intial1, intial2, precision, epsilon, maxIterations):
    x_old1 = round(intial1, precision)
    x_old2 = round(intial2, precision)

    y_old1 = round(getValue(func, x_old1), precision)
    y_old2 = round(getValue(func, x_old2), precision)

    # first guesses were true
    if(getValue(func, x_old1) == 0): return True, x_old1, 0, -1, precision, None
    if(getValue(func, x_old2) == 0): return True, x_old2, 0, -1, precision, None

    res1 = y_old2 * (x_old2 - x_old1)
    res2 = y_old2 - y_old1

    # diverge
    if(res == 0): return False, x_old2, 0, -1, precision, None

    res = res1 / res2
    x_new = round(x_old2 - res, precision)

    solution_steps = [{
        "x_i-1": x_old1,
        "x_i": x_old2,
        "x_i+1": x_new,
        "eps": -1
    }]

    relative_error = 120

    for i in range(maxIterations):
        
        x_old1 = x_old2
        x_old2 = x_new

        res1 = y_old2 * (x_old2 - x_old1)
        res2 = y_old2 - y_old1

        # diverge
        if(res == 0): return False, x_old2, 0, -1, precision, None

        res = res1 / res2
        x_new = round(x_old2 - res, precision)

        relative_error = getEPS(x_new, x_old2)

        solution_steps = [{
            "x_i-1": x_old1,
            "x_i": x_old2,
            "x_i+1": x_new,
            "eps": relative_error
        }]

        if(getValue(func, x_new) == 0 or relative_error <= epsilon):
            break

    if(getValue(func, x_new) == 0 or relative_error <= epsilon):
        return True, x_new, i+1, relative_error, precision, solution_steps 
    else:
        return False, x_new, i+1, relative_error, precision, solution_steps