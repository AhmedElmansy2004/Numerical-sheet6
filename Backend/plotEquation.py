import matplotlib.pyplot as plt
import numpy as np

def plot_equation(equation, equation2=None):
    x = np.linspace(-10, 10, 2000)
    y = eval(equation)

    plt.plot(x, y, label='f(x)')

    intersection_x = []
    intersection_y = []

    if equation2:
        y2 = eval(equation2)
        plt.plot(x, y2, label='g(x)')

        # Find intersections: where f(x) - g(x) ≈ 0
        diff = y - y2
        sign_change_indices = np.where(np.diff(np.sign(diff)))[0]

        for i in sign_change_indices:
            # Linear interpolation for better accuracy => Raphson method step
            x_inter = x[i] - diff[i] * (x[i+1] - x[i]) / (diff[i+1] - diff[i])
            y_inter = eval(equation.replace("x", f"({x_inter})"))

            intersection_x.append(x_inter)
            intersection_y.append(y_inter)

        # Plot intersection points + vertical lines
        for xi, yi in zip(intersection_x, intersection_y):
            plt.scatter(xi, yi, color='red')
            plt.plot([xi, xi], [0, yi], linestyle='--', color='red')
            plt.text(xi, yi, f"({xi:.2f}, {yi:.2f})")

    else:
        # Only one equation → find x-intercepts
        sign_change_indices = np.where(np.diff(np.sign(y)))[0]

        for i in sign_change_indices:
            x_inter = x[i] - y[i] * (x[i+1] - x[i]) / (y[i+1] - y[i])
            plt.scatter(x_inter, 0, color='green')
            plt.text(x_inter, 0, f"{x_inter:.2f}")

    plt.axhline(0, color='black', linewidth=1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Equation Plot")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    equation1 = "(x-5)"
    equation2 = "x**3 - 3*x + 2"
    equation3 = 'np.sin(x)'
    plot_equation(equation2)
