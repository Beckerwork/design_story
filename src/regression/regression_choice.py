from ipywidgets import widgets
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np

from regression.linear_regression import fit_regression_line
from utils.colors import colors


def fmt_de(val):
    return f"{val:.2f}".replace('.', ',')


def get_independent_variable():
    return np.linspace(0, 200, 100)


def get_dependent_variable(independent_variable):
    rng = np.random.default_rng(34)
    offset = 10
    dependent_variable = (0.005 * independent_variable**2 +
                          rng.normal(loc=0, scale=14, size=len(independent_variable)) + offset)
    return dependent_variable


def regression_choice_2():
    fig, ax = plt.subplots(figsize=(7, 5))
    distances = get_independent_variable()
    times = get_dependent_variable(distances)
    ax.scatter(distances, times, color=colors['dark_blue'], label='Datenpunkte')

    linear_slope, linear_intercept, linear_predictions, linear_mse = fit_regression_line(distances, times)
    linear_line, = ax.plot(distances, linear_predictions, color=colors['green'], linestyle='-', label=f' ', visible=False, lw=2)

    quadratic_slope, quadratic_intercept, quadratic_predictions, quadratic_mse = fit_regression_line(distances, times, power=2)
    poly_line, = ax.plot(distances, quadratic_predictions, color=colors['orange'], linestyle='-', label=f' ', visible=False, lw=2)

    checkbox_linear = widgets.Checkbox(
        value=False,
        description='Zeige lineares Modell',
        disabled=False,
        indent=False
    )

    checkbox_poly = widgets.Checkbox(
        value=False,
        description='Zeige quadratisches Modell',
        disabled=False,
        indent=False
    )

    def update_lines(change):
        linear_line.set_visible(checkbox_linear.value)
        poly_line.set_visible(checkbox_poly.value)

        handles_lin, labels_lin = ax.get_legend_handles_labels()
        if checkbox_linear.value:
            labels_lin[1] = (f'Lineares Modell: y = {fmt_de(linear_slope[0])} * x + {fmt_de(linear_intercept)} (Fehlerwert: {fmt_de(linear_mse)})')
        else:
            labels_lin[1] = ''
        if checkbox_poly.value:
            labels_lin[2] = (f'Quadratisches Modell: y = {fmt_de(quadratic_slope[1])} * x^2 + {fmt_de(quadratic_slope[0])} * x + {fmt_de(quadratic_intercept)} (Fehlerwert: {fmt_de(quadratic_mse)})')
        else:
            labels_lin[2] = ''
        ax.legend(handles_lin, labels_lin, loc='lower left', bbox_to_anchor=(0.0, 1.08), borderaxespad=0)
        fig.canvas.draw()

    checkbox_linear.observe(update_lines, names='value')
    display(checkbox_linear)
    checkbox_poly.observe(update_lines, names='value')
    display(checkbox_poly)

    plt.xlabel('Strecke (m)')
    plt.ylabel('Zeit (s)')
    ax.set_title('Strecke vs. Zeit', pad=70)
    ax.legend(loc='lower left', bbox_to_anchor=(0.0, 1.08), borderaxespad=0)
    plt.subplots_adjust(top=0.72)
    plt.grid(True)
    fig.canvas.header_visible = False
    plt.show()
