from essential_functions import getValue, getEPS

def do_fixed_point(gx, intial, precision, epsilon=0.00001, maxIterations = 50):

    x_old = round(intial, precision)
    x_new = round(getValue(gx, x_old), precision)

    solution_steps = [{
        "x_i": x_old,
        "x_i+1": x_new,
        "eps": -1
    }]

    if(x_new == x_old):
        return True, x_new, 0, relative_error, precision, solution_steps

    relative_error = 120

    for i in range(maxIterations):
        
        x_old = x_new

        x_new = round(getValue(gx, x_old), precision)

        relative_error = getEPS(x_new, x_old)

        solution_steps.append({
            "x_i": x_old,
            "x_i+1": x_new,
            "eps": relative_error
        })

        if(x_new == x_old or relative_error <= epsilon):
            break

    if(x_new == x_old or relative_error <= epsilon):
        return True, x_new, i+1, relative_error, precision, solution_steps 
    else:
        return False, x_new, i+1, relative_error, precision, solution_steps