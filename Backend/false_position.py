from essential_functions import getValue, getEPS, round_to_significant_digits, count_all_digits, calculate_significant_digits

solution_steps = []


def do_false_position(
    func, from_val, to_val, precision, epsilon=0.00001, maxIterations=50
):
    global solution_steps
    solution_steps = []

    x_l = round_to_significant_digits(from_val, precision)
    y_l = round_to_significant_digits(getValue(func, x_l), precision)
    x_u = round_to_significant_digits(to_val, precision)
    y_u = round_to_significant_digits(getValue(func, x_u), precision)
    x_r = 0
    y_r = 0
    prev = 0

    # invalid interval -> root is none because the function has same signs at both ends
    if (y_l * y_u > 0):
        return False, None, 0, -1, 0, None

    # check if any of the bounds is the root
    elif (y_l == 0):
        return True, x_l, 0, 0, count_all_digits(y_l), None
    
    elif (y_u == 0):
        return True, x_u, 0, 0, count_all_digits(y_u), None

    # solution_steps = [
    #     {
    #         "x_l": x_l,
    #         "x_u": x_u,
    #         "x_r": x_r,
    #         "y_l": y_l,
    #         "y_u": y_u,
    #         "y_r": y_r,
    #         "eps": -1,
    #     }
    # ]

    relative_error = 120 ###############

    for i in range(maxIterations):
        prev = x_r
        x_r = round_to_significant_digits(((x_l * y_u) - (x_u * y_l)) / (y_u - y_l), precision)
        y_r = round_to_significant_digits(getValue(func, x_r), precision)

        # calculate relative error
        relative_error = relative_error if (i > 0) else -1
        # if not first iteration, calculate relative error
        if i > 0:
            relative_error = getEPS(x_r, prev)

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
            return True, x_r, i + 1, relative_error, count_all_digits(x_r), solution_steps


        if relative_error <= epsilon and i > 0:
            if (relative_error == 0): # exact root
                return True, x_r, i+1, relative_error, count_all_digits(x_r), solution_steps
            return True, x_r, i+1, relative_error, calculate_significant_digits(relative_error), solution_steps

    return False, x_r, i + 1, relative_error, calculate_significant_digits(relative_error), None

if __name__ == "__main__":
    success, root, iterations, relative_error, precision, steps = do_false_position("sin(x)", 2, 4, 17, 0.0001, 100)
    # success, root, iterations, relative_error, precision, steps = do_false_position("x**2 - 9", 0, 4, 17, 0.0001, 100)
    print("Success:", success)
    print("Root:", root)
    print("Iterations:", iterations)
    print("Relative Error:", relative_error)
    print("Precision:", precision)
    # print("Steps:", steps)
    for step in steps:
        print(step)