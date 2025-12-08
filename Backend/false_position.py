from essential_functions import getValue, getEPS

solution_steps = []


def do_false_position(
    func, from_val, to_val, precision, epsilon=0.00001, maxIterations=50
):
    global solution_steps

    x_l = round(from_val, precision)
    y_l = round(getValue(func, x_l), precision)
    x_u = round(to_val, precision)
    y_u = round(getValue(func, x_u), precision)
    x_r = 0
    y_r = 0
    prev = 0

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

    isFirstIteration = True

    relative_error = 120

    for i in range(maxIterations):
        prev = x_r
        x_r = round(((x_l * y_u) - (x_u * y_l)) / (y_u - y_l), precision)
        y_r = round(getValue(func, x_r), precision)

        if y_l * y_r < 0:
            x_u = x_r
            y_u = y_r

        elif y_u * y_r < 0:
            x_l = x_r
            y_l = y_r

        elif y_r == 0:
            relative_error = getEPS(x_r, prev) if not isFirstIteration else -1
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
            break

        if isFirstIteration:
            isFirstIteration = False
        else:
            relative_error = getEPS(x_r, prev)

        if relative_error <= epsilon:
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
            break

    if y_r == 0 or relative_error <= epsilon:
        return True, x_r, i + 1, relative_error, precision, solution_steps
    else:
        return False, x_r, i + 1, relative_error, precision, solution_steps
