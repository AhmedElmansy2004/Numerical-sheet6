from bisection import do_bisection
from false_position import do_false_position

def find_root(method , func, from_val, to_val, precision, epsilon=0.00001, maxIterations = 50):
    result = 0
    if(method == "bisection"):
            result = do_bisection(func, from_val, to_val, precision, epsilon, maxIterations)

    elif(method == "false position"):
          result = do_false_position(func, from_val, to_val, precision, epsilon, maxIterations)

    elif(method == "rest"):
          pass

    return result

if __name__ == "__main__":

    methods = ["bisection", "false position"]

    # Test case 1
    func = "x**2 - 4"
    from_val = 0
    to_val = 5
    precision = 6

    for method in methods:
        print(find_root(method, func, from_val, to_val, precision))

    print()

    # Test case 2
    func = "sin(x)"
    from_val = -1
    to_val = 2

    for method in methods:
        print(find_root(method, func, from_val, to_val, precision))

    print()

    # Test case 3
    func = "exp(x) - 2"
    from_val = 0
    to_val = 2

    for method in methods:
        print(find_root(method, func, from_val, to_val, precision))

    print()

    # Test case 4
    func = "x**3 - 6*x**2 + 11*x - 6"
    from_val = 0
    to_val = 2.5

    for method in methods:
        print(find_root(method, func, from_val, to_val, precision))

    print()

    # Test case 5
    func = "x**5"
    from_val = -1
    to_val = 1

    for method in methods:
        print(find_root(method, func, from_val, to_val, precision))

    print()

    # Test case 6
    func = "x**2 - 9"
    from_val = -5
    to_val = 0

    for method in methods:
        print(find_root(method, func, from_val, to_val, precision))

    print()

    # Test case 7
    func = "x**3 - x - 2"
    from_val = 1
    to_val = 2

    for method in methods:
        print(find_root(method, func, from_val, to_val, precision))