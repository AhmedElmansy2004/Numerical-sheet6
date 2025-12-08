from essential_functions import getValue, getEPS

solution_steps = []

# Bisection Method Implementation
# return (success: bool, root: float, iterations: int, relative_error: float, precision: int, steps: list)
def do_bisection(func, from_val, to_val, precision, epsilon=0.00001, maxIterations=50):
    global solution_steps

    # print the input first
    print("Bisection Method")
    print("Function: " + func)
    print("Interval: [" + str(from_val) + ", " + str(to_val) + "]")
    print("Precision: " + str(precision))
    print("Tolerance: " + str(epsilon))
    print("Max Iterations: " + str(maxIterations))

    x_l = round(from_val, precision)
    y_l = round(getValue(func, x_l), precision)
    x_u = round(to_val, precision)
    y_u = round(getValue(func, x_u), precision)
    x_r = 0
    y_r = 0
    prev = 0

    # invalid interval -> root is none because the function has same signs at both ends
    if (y_l * y_u > 0):
        return False, None, 0, -1, precision, None

    # check if any of the bounds is the root
    elif (y_l == 0):
        return True, x_l, 0, 0, precision, None
    
    elif (y_u == 0):
        return True, x_u, 0, 0, precision, None

    solution_steps = [
        {
            "x_l": x_l,
            "x_u": x_u,
            "x_r": x_r,
            "y_l": y_l,
            "y_u": y_u,
            "y_r": y_r,
            "eps": -1,
        }
    ]

    relative_error = 120

    for i in range(maxIterations):
        # get the midpoint
        prev = x_r
        x_r = round(x_l + (x_u - x_l) / 2, precision)
        y_r = round(getValue(func, x_r), precision)

        # calculate relative error
        relative_error = relative_error if (i > 0) else -1

        solution_steps.append(
            {
                "x_l": x_l,
                "x_u": x_u,
                "x_r": x_r,
                "y_l": y_l,
                "y_u": y_u,
                "y_r": y_r,
                "eps": relative_error,
            }
        )

        # if the root is in left subinterval
        if y_l * y_r < 0:
            x_u = x_r
            y_u = y_r

        # if the root is in right subinterval
        elif y_u * y_r < 0:
            x_l = x_r
            y_l = y_r

        # got the root -> Successful termination
        elif y_r == 0:
            print("Found exact root")
            return True, x_r, i + 1, relative_error, precision, solution_steps

        # if not first iteration, calculate relative error
        if i > 0:
            relative_error = getEPS(x_r, prev)

        # Successful termination
        if relative_error <= epsilon and i > 0:
            print("Converged to desired precision")
            return True, x_r, i + 1, relative_error, precision, solution_steps

    
    # if max iterations reached -> but then also return the best estimate
    return False, x_r, i + 1, relative_error, precision, solution_steps


if "__main__" == __name__:
    print(do_bisection("sin(x)", 2, 4, 17, 0.0001, 100))
