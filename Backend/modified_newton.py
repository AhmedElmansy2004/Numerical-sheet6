from essential_functions import getValue, getDerivative, getSecondDerivative,getEPS, round_to_significant_digits, calculate_significant_digits, count_all_digits

# to do: fix if derivaitive = 0


def do_modified_newton(func, intial, precision, epsilon=0.00001, maxIterations = 50):

    maxVal = 1e12
    minVal = -1e12

    x_old = round_to_significant_digits(intial, precision)

    # first guess was true
    if(getValue(func, x_old) == 0):
        return True, x_old, 0, -1, count_all_digits(x_old), None

    res1 = getValue(func, x_old) * getDerivative(func, x_old)
    res2 = (getDerivative(func, x_old) ** 2) - (getValue(func, x_old) * getSecondDerivative(func, x_old))
    

    # diverge at first step
    if(res2 == 0):
        print("1-division by zero")
        return False, x_old, 0, -1, 0, None

    res = res1 / res2
    x_new = round_to_significant_digits(x_old - res, precision)



    solution_steps = [{
        "x_i": x_old,
        "x_i+1": x_new,
        "eps": -1
    }]

    # second guess was true
    if(getValue(func, x_old) == 0):
        return True, x_new, 0, -1, count_all_digits(x_new), solution_steps

    relative_error = 120

    for i in range(maxIterations):
        
        x_old = x_new

        res1 = getValue(func, x_old) * getDerivative(func, x_old)
        res2 = (getDerivative(func, x_old) ** 2) - (getValue(func, x_old) * getSecondDerivative(func, x_old))

        # diverge at step i
        if(res2 == 0):
            print("2- division by zero")
            return False, x_old, 0, -1, 0, None

        res = res1 / res2
        x_new = round_to_significant_digits(x_old - res, precision)

        # Check for overflow/underflow
        if(x_new > maxVal or x_new < minVal):
            return False, x_new, i+1, relative_error, 0, solution_steps

        relative_error = getEPS(x_new, x_old)

        solution_steps.append({
            "x_i": x_old,
            "x_i+1": x_new,
            "eps": relative_error
        })

        # converged
        if(getValue(func, x_new) == 0 or relative_error <= epsilon):
            if (relative_error == 0): # exact root
                return True, x_new, i+1, relative_error, count_all_digits(x_new), solution_steps
            return True, x_new, i+1, relative_error, calculate_significant_digits(relative_error), solution_steps

    # max iterations reached
    return False, x_new, i+1, relative_error, calculate_significant_digits(relative_error), solution_steps