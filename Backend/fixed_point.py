from essential_functions import getValue, getEPS, round_to_significant_digits, count_all_digits, calculate_significant_digits

def do_fixed_point(gx, intial, precision, epsilon=0.00001, maxIterations = 50):
    maxVal = 1e12
    minVal = -1e12

    x_old = round_to_significant_digits(intial, precision)
    try :
        x_new = round_to_significant_digits(getValue(gx, x_old), precision)
    except Exception as e:
        return False, x_old, 0, -1, 0, None

    solution_steps = []
    # solution_steps = [{
    #     "x_i": x_old,
    #     "x_i+1": x_new,
    #     "eps": -1
    # }]

    if(x_new == x_old):
        return True, x_new, 0, -1, count_all_digits(x_new), solution_steps

    relative_error = 120

    for i in range(maxIterations):
        
        x_old = x_new

        x_new = round_to_significant_digits(getValue(gx, x_old), precision)

        # Check for overflow/underflow
        if(x_new > maxVal or x_new < minVal):
            return False, x_new, i+1, relative_error, 0, solution_steps
        

        relative_error = getEPS(x_new, x_old)

        solution_steps.append({
            "x_i": x_old,
            "x_i+1": x_new,
            "eps": relative_error
        })


        # Detect 2-cycle oscillation
        if (i > 1):
            x_prev2 = solution_steps[i-1]["x_i"]
            print(x_prev2, x_new)
            if x_new == x_prev2:
                return False, None, i+1, -1, 0, None

        # Check for convergence
        if(x_new == x_old or relative_error <= epsilon):
            if (relative_error == 0): # exact root
                return True, x_new, i+1, relative_error, count_all_digits(x_new), solution_steps
            return True, x_new, i+1, relative_error, calculate_significant_digits(relative_error), solution_steps

    # Return false if the maximum number of iterations is reached
    return False, x_new, i+1, relative_error, calculate_significant_digits(relative_error), solution_steps


if __name__ == '__main__':
    success, root, iterations, relative_error, precision, steps = do_fixed_point("9/x", 1, 17, 0.0001, 100)
    print("Success:", success)
    print("Root:", root)
    print("Iterations:", iterations)
    print("Relative Error:", relative_error)
    print("Precision:", precision)
    # print("Steps:", steps)
    # for step in steps:
    #     print(step)