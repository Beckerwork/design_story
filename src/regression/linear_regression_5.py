import matplotlib.pyplot as plt

from IPython.display import display
from regression.linear_regression import (
    get_independent_variable,
    get_dependent_variable,
    fit_regression_line,
)
from utils.colors import colors


def zeige_lineare_regression_5():
    independent_variable = get_independent_variable()
    dependent_variable = get_dependent_variable(independent_variable)

    fig, ax = plt.subplots(figsize=(7, 5))
    fig.canvas.header_visible = False
    ax.scatter(independent_variable, dependent_variable, color=colors['dark_blue'], label='Daten der Kinder')

    ml_slope, ml_intercept, ml_predictions, ml_mse = fit_regression_line(independent_variable, dependent_variable)
    regression_line, = ax.plot(independent_variable, ml_predictions, color=colors['green'], linestyle='-', label='',
                               visible=True)
    regression_line.set_label(
        f'Roboter Gerade: Output = {ml_slope[0]:.2f}'.replace('.', ',') +
        f' * Input + {ml_intercept:.2f}'.replace('.', ',') +
        f' (Fehlerwert: {ml_mse:.2f})'.replace('.', ','))

    ax.text(145.5, 22.5, "Sarah", fontsize=9, ha='left', color=colors['purple'])
    ax.scatter(145, 22.5, color=colors['purple'])

    ax.text(152.5, 23.8, "Ben", fontsize=9, ha='right', color=colors['purple'])
    ax.scatter(153, 23.5, color=colors['purple'])

    ax.set_xlabel('Körpergröße (cm)')
    ax.set_ylabel('Maximale Geschwindigkeit (km/h)')
    ax.set_title('Größe vs. maximale Geschwindigkeit', y=1.2)
    ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.2))
    ax.grid(True)
    plt.tight_layout()
    plt.show()
