from essential_functions import getValue, getEPS, round_to_significant_digits, calculate_significant_digits, count_all_digits

def do_secant(func, intial1, intial2, precision, epsilon, maxIterations):

    maxVal = 1e12
    minVal = -1e12

    x_old1 = round_to_significant_digits(intial1, precision)
    x_old2 = round_to_significant_digits(intial2, precision)

    y_old1 = round_to_significant_digits(getValue(func, x_old1), precision)
    y_old2 = round_to_significant_digits(getValue(func, x_old2), precision)

    # first guesses were true
    if(getValue(func, x_old1) == 0):
        return True, x_old1, 0, -1, count_all_digits(x_old1), None
    if(getValue(func, x_old2) == 0):
        return True, x_old2, 0, -1, count_all_digits(x_old2), None

    res1 = y_old2 * (x_old2 - x_old1)
    res2 = y_old2 - y_old1

    # diverge
    if(res2 == 0): return False, x_old2, 0, -1, precision, None

    res = res1 / res2
    
    x_new = round_to_significant_digits(x_old2 - res, precision)

    solution_steps = [{
        "x_i-1": x_old1,
        "x_i": x_old2,
        "x_i+1": x_new,
        "eps": -1
    }]

    relative_error = 120

    for i in range(maxIterations):
        
        x_old1, x_old2 = x_old2, x_new

        # recalculate y for this iteration
        y_old1 = round_to_significant_digits(getValue(func, x_old1), precision)
        y_old2 = round_to_significant_digits(getValue(func, x_old2), precision)

        res1 = y_old2 * (x_old2 - x_old1)
        res2 = y_old2 - y_old1

        # diverge at this step
        if(res2 == 0):
            return False, x_old2, i+1, -1, calculate_significant_digits(relative_error), None

        res = res1 / res2
        
        x_new = round_to_significant_digits(x_old2 - res, precision)

        # Check for overflow/underflow
        if(x_new > maxVal or x_new < minVal):
            return False, None, i+1, -1, 0, None

        relative_error = getEPS(x_new, x_old2)

        solution_steps.append({
            "x_i-1": x_old1,
            "x_i": x_old2,
            "x_i+1": x_new,
            "eps": relative_error
        })

        # convergence check
        if(getValue(func, x_new) == 0 or relative_error <= epsilon):
            if (relative_error == 0): # exact root
                return True, x_new, i+1, relative_error, count_all_digits(x_new), solution_steps
            return True, x_new, i+1, relative_error, calculate_significant_digits(relative_error), solution_steps

    # max iterations reached
    return False, None, i+1, relative_error, 0, None